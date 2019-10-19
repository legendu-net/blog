#!/usr/bin/env python3
# encoding: utf-8

import os
import os.path
import re
import sqlite3
import datetime
import shutil
from pathlib import Path
import json
from typing import Union, Sequence, List

EN = 'en'
CN = 'cn'
HOME = 'home'
MISC = 'misc'
DECLARATION = '''
**
Things on this page are fragmentary and immature notes/thoughts of the author.
It is not meant to readers but rather for convenient reference of the author and future improvement.
**

'''
NOW_DASH = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
TODAY_DASH = NOW_DASH[:10]
BASE_DIR = Path(__file__).resolve().parent
FILE_WORDS = BASE_DIR / 'words.json'


def qmarks(n: Union[int, Sequence]) -> str:
    """Generate n question marks delimited by comma.
    """
    if isinstance(n, List) or isinstance(n, tuple):
        n = len(n)
    return ', '.join(['?'] * n)


def _changed(post: str, content: str) -> bool:
    with open(post, 'r') as fin:
        content_updated = fin.read()
    return content_updated != content


def _update_post_move(post):
    """ Update the post after move.
    There are 3 possible change.
    1. The declaration might be added/removed
    depending on whether the post is moved to the misc sub blog directory.
    2. The slug of the post is updated to match the path of the post.
    3. The title should be updated to match the file name.
    Both 2 and 3 will prompt to user for confirmation.
    """
    # slug = 'Slug: ' + _slug(os.path.basename(post)[11:])
    if _blog_dir(post) == MISC:
        with open(post, 'r', encoding='utf-8') as fin:
            lines = fin.readlines()
        index = [line.strip() for line in lines].index('')
        with open(post, 'w', encoding='utf-8') as fout:
            fout.writelines(lines[:index])
            fout.writelines(DECLARATION)
            fout.writelines(lines[index:])
    else:
        with open(post, 'r', encoding='utf-8') as fin:
            text = fin.read()
        text = text.replace(DECLARATION, '')
        # text = re.sub('\nSlug: .*\n', slug, text)
        with open(post, 'w', encoding='utf-8') as fout:
            fout.write(text)


def _update_time(post):
    with open(post, 'r', encoding='utf-8') as fin:
        lines = fin.readlines()
    for i, line in enumerate(lines):
        if line.startswith('Date: '):
            lines[i] = f'Date: {NOW_DASH}\n'
            break
    with open(post, 'w') as fout:
        fout.writelines(lines)


def _blog_dir(post: Path):
    """Get the corresponding blog directory (one of home, en, cn and misc)
    of a post.
    """
    return Path(post).parent.parent.stem


def _slug(title: str):
    return title.replace(' ', '-').replace('/', '-')


def _format_title(title):
    with open(FILE_WORDS, 'r', encoding='utf-8') as fin:
        words = json.load(fin)
    title = title.title()
    for word in words:
        title = title.replace(' ' + word[0] + ' ', ' ' + word[1] + ' ')
        if title.startswith(word[0] + ' '):
            title = title.replace(word[0] + ' ', word[1] + ' ')
        if title.endswith(' ' + word[0]):
            title = title.replace(' ' + word[0], ' ' + word[1])
    return title


def _fts_version():
    options = sqlite3.connect(':memory:') \
            .execute('pragma compile_options').fetchall()
    if ('ENABLE_FTS5', ) in options:
        return 'fts5'
    return 'fts4'


class Blogger:
    """A class for managing blog.
    """
    POSTS_COLS = [ 
        'path',
        'dir',
        'status',
        'date',
        'author',
        'slug',
        'title',
        'category',
        'tags',
        'content',
        'empty',
        'updated',
        'name_title_mismatch'
    ]

    def __init__(self, db: str = ''):
        """Create an instance of Blogger.

        :param dir_: the root directory of the blog.
        :param db: the path to the SQLite3 database file.
        """
        self._fts = _fts_version()
        self._db = db if db else str(BASE_DIR / '.blogger.sqlite3')
        self._conn = sqlite3.connect(self._db)
        self._create_vtable_posts()

    def _create_vtable_posts(self):
        sql = f'''
            CREATE VIRTUAL TABLE IF NOT EXISTS posts USING {self._fts} (
                {', '.join(Blogger.POSTS_COLS)},
                tokenize = porter
            )
            '''
        self.execute(sql)

    def _create_table_srps(self):
        sql = 'CREATE TABLE IF NOT EXISTS srps (path)'
        self.execute(sql)

    def clear(self):
        """Remove the SQLite3 database.
        """
        os.remove(self._db)

    def commit(self):
        """Commit changes made to the SQLite3 database.
        """
        self._conn.commit()

    def update_category(self, post, category):
        """Change the category of the specified post to the specified category.
        """
        with open(post, 'r', encoding='utf-8') as fin:
            lines = fin.readlines()
        for i, line in enumerate(lines):
            if line.startswith('Category: '):
                lines[i] = f'Category: {category}\n'
                break
        with open(post, 'w') as fout:
            fout.writelines(lines)
        sql = 'UPDATE posts SET category = ? WHERE path = ?'
        self.execute(sql, [category, post])

    def update_tags(self, post, from_tag, to_tag):
        """Update the tag from_tag of the post to the tag to_tag.
        """
        with open(post, 'r', encoding='utf-8') as fin:
            lines = fin.readlines()
        for i, line in enumerate(lines):
            if line.startswith('Tags: '):
                tags = (tag.strip() for tag in line[5:].split(','))
                tags = (to_tag if tag == from_tag else tag for tag in tags)
                lines[i] = 'Tags: ' + ', '.join(tags)
                break
        with open(post, 'w') as fout:
            fout.writelines(lines)
        sql = 'UPDATE posts SET tags = ? WHERE path = ?'
        self.execute(sql, [tags + ',', post])

    def reload_posts(self):
        """Reload posts into the SQLite3 database.
        """
        self._create_vtable_posts()
        self.execute('DELETE FROM posts')
        for dir_ in (HOME, CN, EN, MISC):
            self._load_posts(BASE_DIR / dir_ / 'content')
        self.commit()

    def _load_posts(self, post_dir: str):
        if not os.path.isdir(post_dir):
            return
        for post in Path(post_dir).iterdir():
            if post.suffix in ('.markdown', '.ipynb'):
                self._load_post(post)

    def _load_post(self, post: Union[str, Path]):
        post = Path(post)
        suffix = post.suffix
        if suffix == '.ipynb':
            record = self._parse_ipynb_post(post)
        elif suffix == '.markdown':
            record self._parse_markdown_post(post)
        else:
            raise ValueError(f'{post} is not a .markdown or .ipynb file.')
        sql = '''
            INSERT INTO posts (
                {', '.join(Blogger.POSTS_COLS)},
            ) VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            '''
        self.execute(sql, record)

    def _parse_ipynb_post(self, post: Path) -> List[str]:
        content = post.read_text()
        cells = json.loads(content)['cells']
        empty = 1 if len(cells) <= 1 else 0
        if cells[0]['cell_type'] != 'markdown':
            raise SyntaxError(f'The first cell of the notebook {post} is not a markdown cell!')
        meta = cells[0]['source']
        status = ''
        date = ''
        author = ''
        slug = ''
        title = ''
        category = ''
        tags = ''
        for line in meta:
            if not re.search('^- [a-zA-Z]+:', line):
                raise SyntaxError(f'The meta line {line} of the notebook {post} does not confront to the format "- MetaField: Value"!')
            if line.startswith('- Status:'):
                status = line[9:].strip()
                continue
            if line.startswith('- Date:'):
                status = line[7:].strip()
                continue
            if line.startswith('- Author:'):
                status = line[9:].strip()
                continue
            if line.startswith('- Slug:'):
                status = line[7:].strip()
                continue
            if line.startswith('- Title:'):
                status = line[8:].strip()
                continue
            if line.startswith('- Category:'):
                status = line[11:].strip()
                continue
            if line.startswith('- Tags:'):
                status = line[7:].strip()
                continue
        name_title_mismatch = self._is_name_title_mismatch(post, title)
        return [
            post,
            _blog_dir(post),
            status,
            date,
            author,
            slug,
            title,
            category,
            tags,
            content,
            empty,
            0,
            name_title_mismatch,
        ]

    def _parse_markdown_post(self, post: Path) -> List[str]:
        with post.open() as fin:
            lines = fin.readlines()
        index = 0
        for index, line in enumerate(lines):
            if not re.match('[A-Za-z]+: ', line):
                break
        # parse meta data 0 - index (exclusive)
        status = ''
        date = ''
        author = ''
        slug = ''
        title = ''
        category = ''
        tags = ''
        for line in lines[:index]:
            if line.startswith('Status: '):
                status = line[8:].strip()
            elif line.startswith('Date: '):
                date = line[6:].strip()
            elif line.startswith('Author: '):
                author = line[8:].strip()
            elif line.startswith('Slug: '):
                slug = line[6:].strip()
            elif line.startswith('Title: '):
                title = line[7:].strip()
            elif line.startswith('Category: '):
                category = line[10:].strip()
            elif line.startswith('Tags: '):
                tags = line[6:].strip()
                if not tags.endswith(','):
                    tags = tags + ','
        # parse content index to end
        content = ''.join(lines)
        empty = self._is_ess_empty(lines[index:])
        name_title_mismatch = self._is_name_title_mismatch(post, title)
        return [
            post,
            _blog_dir(post),
            status,
            date,
            author,
            slug,
            title,
            category,
            tags,
            content,
            empty,
            0,
            name_title_mismatch,
        ]

    def _is_ess_empty(self, lines: List[str]) -> int:
        """Check whether the lines are essentially empty.
        :param lines: A list of lines.
        """
        content = ''.join(line.strip() for line in lines)
        is_empty = re.sub(r'\*\*.+\*\*', '', content).replace('**', '') == ''
        return 1 if is_empty else 0

    def _is_name_title_mismatch(self, path: Path, title: str) -> int:
        """Check whether the file anme and the title of the post does not match.
        :param path: The path of the post.
        :param title: The title of the post.
        :return: 1 if mismatch and 0 otherwise.
        """
        title_new = _format_title(self.file_name(path).replace('-', ' '))
        title_old = title.replace('-', ' ')
        return 1 if title_old != title_new else 0

    def trash(self, posts: Union[str, List[str]]):
        """Move the specified posts to the trash directory.
        :param posts:
        """
        if isinstance(posts, str):
            posts = [posts]
        path_ = BASE_DIR / 'trash'
        if not os.path.isdir(path_):
            os.mkdir(path_)
        for post in posts:
            shutil.move(post, path_)
        sql = f'''
            DELETE FROM posts 
            WHERE 
                path in ({qmarks(posts)})
            '''
        self.execute(sql, posts)

    def move(self, post, target):
        """Move a post to the specified location.
        """
        post = Path(post)
        if target in (EN, CN, MISC):
            target = BASE_DIR / target / 'content' / post.name
        if post == target:
            return
        shutil.move(post, target)
        _update_post_move(target)
        sql = 'UPDATE posts SET path = ?, dir = ? WHERE path = ?'
        self.execute(sql, [target, _blog_dir(target), post])

    def _reg_param(self, param):
        if isinstance(param, (int, float, str)):
            return param
        return str(param)

    def execute(self, operation: str, parameters=()):
        parameters = [self._reg_param(param) for param in parameters]
        return self._conn.execute(operation, parameters)

    def edit(self, posts: Union[str, List[str]], editor: str) -> None:
        """Edit the specified posts using the specified editor.
        """
        if not isinstance(posts, list):
            posts = [posts]
        self._update_updated(updated=1, posts=posts)
        posts = ' '.join(f"'{post}'" for post in posts)
        os.system(f'{editor} {posts}')

    def _create_post(self, post, title):
        with open(post, 'w', encoding='utf-8') as fout:
            fout.writelines('Status: published\n')
            fout.writelines(f'Date: {NOW_DASH}\n')
            fout.writelines('Author: Benjamin Du\n')
            fout.writelines('Slug: {}\n'.format(
                title.replace(' ', '-').replace('/', '-')))
            fout.writelines(f'Title: {_format_title(title)}\n')
            fout.writelines('Category: Programming\n')
            fout.writelines('Tags: programming\n')
            if _blog_dir(post) == MISC:
                fout.writelines(DECLARATION)

    def _update_updated(self, updated: int, posts: List[Path]):
        """Update the "updated" filed.
        :param updated: The value (1 or 0) to update the "updated" filed to.
        :param posts:
        """
        posts = [str(post) for post in posts]
        sql = f'UPDATE posts SET updated = ? WHERE path in ({qmarks(posts)})'
        self.execute(sql, [updated] + posts)

    def _delete_updated(self) -> None:
        sql = 'DELETE FROM posts WHERE updated = 1'
        self.execute(sql)

    def update(self):
        """Update information of the changed posts.
        """
        sql = 'SELECT path, content FROM posts WHERE updated = 1'
        rows = self.execute(sql).fetchall()
        posts_same = [post for post, content in rows if not _changed(post, content)]
        self._update_updated(updated=0, posts=posts_same)
        self._delete_updated()
        posts_updated = [post for post, content in rows if _changed(post, content)]
        for path in posts_updated:
            _update_time(path)
            self._load_post(path)

    def clean_srps(self):
        """Clean contents of the table srps.
        """
        sql = 'DELETE FROM srps'
        self.execute(sql)

    def add(self, title: str, dir_: str) -> str:
        """Add a new post with the given title.
        """
        file = self.find_post(title, dir_)
        if not file:
            file = f'{TODAY_DASH}-{_slug(title)}.markdown'
            file = BASE_DIR / dir_ / 'content' / file
            self._create_post(file, title)
            self._load_post(file)
        print(f'\nThe following post is added.\n{file}\n')
        return file

    def find_post(self, title, dir_):
        """Find existing post matching the given title.

        :return: Return the path of the existing post if any,
        otherwise return empty string.
        """
        # find all posts and get rid of leading dates
        sql = 'SELECT path FROM posts WHERE path LIKE ? AND dir = ?'
        row = self.execute(
            sql, [f'%{_slug(title)}.markdown', dir_]).fetchone()
        if row:
            return row[0]
        return ''

    def empty_post(self, dry_run=False):
        """Find all empty posts into the table srps.
        """
        self._create_table_srps()
        self.execute('DELETE FROM srps')
        sql = f'''
            INSERT INTO srps
            SELECT path
            FROM posts
            WHERE empty = 1
            '''
        if dry_run:
            print(sql)
            return
        self.execute(sql)
        self.commit()

    def find_name_title_mismatch(self, dry_run=False):
        self._create_table_srps()
        self.execute('DELETE FROM srps')
        sql = f'''
            INSERT INTO srps
            SELECT path
            FROM posts
            WHERE name_title_mismatch = 1 AND dir <> 'cn'
            '''
        if dry_run:
            print(sql)
            return
        self.execute(sql)
        self.commit()

    def search(self, phrase: str, filter_: str = '', dry_run=False):
        """Search for posts containing the phrase.
        :param phrase: The phrase to search for in posts.
        :param filter_: Extra filtering conditions.
        """
        self._clear_srps()
        conditions = []
        if phrase:
            conditions.append(f"posts MATCH '{phrase}'")
        if filter_:
            filter_ = conditions.append(filter_)
        where = ' AND '.join(conditions)
        if where:
            where = 'WHERE ' + where
        sql = f'''
            INSERT INTO srps
            SELECT path
            FROM posts
            {where}
            ORDER BY rank
            '''
        if dry_run:
            print(sql)
            return
        self.execute(sql)
        self.commit()

    def _clear_srps(self):
        self._create_table_srps()
        self.execute('DELETE FROM srps')

    def last(self, n: int):
        """Get last (according to modification time) n posts.
        :param n: The number of posts to get.
        """
        self._clear_srps()
        sql = f'''
            insert into srps
            select path
            from posts
            where 
            '''
        self.execute(sql)
        self.commit()

    def path(self, idx: Union[int, List[int]]) -> List[str]:
        if isinstance(idx, int):
            idx = [idx]
        sql = f'SELECT path FROM srps WHERE rowid in ({qmarks(idx)})'
        return [row[0] for row in self.execute(sql, idx).fetchall()]

    def fetch(self, n: int):
        """Fetch search results.

        :param n: the number of results to fetch.
        """
        sql = 'SELECT rowid, path FROM srps LIMIT {}'.format(n)
        return self.execute(sql).fetchall()

    def query(self, sql: str, params: Sequence = ()):
        return self.execute(sql, params).fetchall()

    def tags(self, dir_: str = '', where=''):
        sql = 'SELECT tags FROM posts {where}'
        if where:
            sql = sql.format(where=where)
        else:
            # todo you can support quicker specific filtering in future
            sql = sql.format(where=where)
        cursor = self.execute(sql)
        tags = {}
        row = cursor.fetchone()
        while row is not None:
            for tag in row[0].split(','):
                tag = tag.strip()
                if tag == '':
                    continue
                if tag in tags:
                    tags[tag] += 1
                else:
                    tags[tag] = 1
            row = cursor.fetchone()
        return sorted(tags.items(), key=lambda pair: pair[1], reverse=True)

    def categories(self, dir_: str = '', where=''):
        sql = '''
            SELECT
                category,
                count(*) as n
            FROM
                posts
            {where}
            GROUP BY
                category
            ORDER BY
                n desc
            '''
        if where:
            sql = sql.format(where=where)
        else:
            # todo you can support quicker specific filtering in future
            sql = sql.format(where=where)
        cats = (row for row in self.execute(sql).fetchall())
        return cats

    def match_post_title(self, post):
        post_name = self.file_name(post)
        title = self.post_title(post)
        slug_name = title.lower().replace(' ', '-')
        with open(post, 'r') as fin:
            lines = fin.readlines()
        for index, line in enumerate(lines):
            if line.startswith('Slug: '):
                lines[index] = f'Slug: {slug_name}\n'
        with open(post, 'w') as fout:
                fout.writelines(lines)   
        post_name_new = post.replace(post_name, slug_name)
        os.rename(post, post_name_new)

    def match_post_name(self, post):
        title_name = _format_title(self.file_name(post).replace('-', ' '))
        slug_name = title_name.lower().replace(' ', '-')
        with open(post, 'r') as fin:
            lines = fin.readlines()
        for index, line in enumerate(lines):
            if line.startswith('Title: '):
                lines[index] = f'Title: {title_name}\n'
            elif line.startswith('Slug: '):
                lines[index] = f'Slug: {slug_name}\n'          
        with open(post, 'w') as fout:
            fout.writelines(lines)

    def post_title(self, post: Path) -> str:
        """Get the title of the post.
        :param post: The Path object of the post.
        :return: The title of the post.
        """
        suffix = post.suffix
        if suffix == '.ipynb':
            return self._post_title_ipynb(post)
        if suffix == '.markdown':
            return self._post_title_markdown(post)
        raise ValueError(f'{post} is not a .markdown or .ipynb file.')

    def _post_title_ipynb(self, post: Path):
        # TODO: dedup the code 
        content = post.read_text()
        cell = json.loads(content)['cells'][0]
        if cell['cell_type'] != 'markdown':
            raise SyntaxError(f'The first cell of the notebook {post} is not a markdown cell!')
        meta = cell['source']
        for line in meta:
            if not re.search('^- [a-zA-Z]+:', line):
                raise SyntaxError(f'The meta line {line} of the notebook {post} does not confront to the format "- MetaField: Value"!')
            if line.startswith('- Title:'):
                return line[8:].strip()
        raise SyntaxError(f'No title in the post {post}!')

    def _post_title_markdown(self, post: Path) -> str:
        with post.open() as fin:
            for line in fin:
                if line.startswith('Title: '):
                    return line[7:].strip()
        raise SyntaxError(f'No title in the post {post}!')

    def file_name(self, post: Path) -> str:
        return post.stem[11:]