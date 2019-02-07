#!/usr/bin/env python3
# encoding: utf-8

import os
import os.path
import re
from argparse import ArgumentParser
import sqlite3
import hashlib
import datetime
import shutil
import json

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
DASHES = '-' * 80
NOW_DASH = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
TODAY_DASH = NOW_DASH[:10]
EDITOR = 'code'


def _update_post_move(post):
    """ Update the post after move.
    There are two possible change.
    First, the declaration might be added/removed depending on whether the post is moved to the misc sub blog directory.
    Second, the slug of the post is updated to match the path of the post.
    """
    # slug = 'Slug: ' + _slug(os.path.basename(post)[11:])
    if blog_dir(post) == MISC:
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
        if line.startswith('Date: 2'):
            lines[i] = f'Date: {NOW_DASH}\n'
            break
    with open(post, 'w') as fout:
        fout.writelines(lines)


def blog_dir(post: str):
    dir_ = os.path.dirname(post)
    dir_ = os.path.dirname(dir_)
    return os.path.basename(dir_)


def _slug(title: str):
    return title.replace(' ', '-').replace('/', '-')


def _format_title(title, file_words):
    with open(file_words, 'r', encoding='utf-8') as fin:
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
    options = sqlite3.connect(':memory:').execute('pragma compile_options').fetchall()
    if ('ENABLE_FTS5',) in options:
        return 'fts5'
    return 'fts4'


class Blogger:

    def __init__(self, db: str = ''):
        """Create an instance of Blogger.

        :param dir_: the root directory of the blog.
        :param db: the path to the SQLite3 database file.
        """
        self._fts = _fts_version()
        self._db = db if db else os.path.join(os.path.expanduser('~'), '.blogger.sqlite3')
        self._conn = sqlite3.connect(self._db)
        self._create_vtable_posts()
        self.root_dir = self._root_dir()

    def _root_dir(self):
        sql = 'SELECT path FROM posts LIMIT 1'
        row = self._conn.execute(sql).fetchone()
        if row:
            dir_ = os.path.dirname(row[0])
            dir_ = os.path.dirname(dir_)
            return os.path.dirname(dir_)
        return ''

    def _create_vtable_posts(self):
        sql = f'''
        CREATE VIRTUAL TABLE IF NOT EXISTS posts USING {self._fts} (
            path, dir, status, date, author, slug, title, category, tags, content
        )
        '''
        self._conn.execute(sql)

    def _create_table_srps(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS srps (
            path, dir, status, date, author, slug, title, category, tags, content
        )
        '''
        self._conn.execute(sql)

    def reload_posts(self, root_dir: str):
        self._create_vtable_posts()
        self._conn.execute('DELETE FROM posts')
        # self._conn.commit()
        for dir_ in (HOME, CN, EN, MISC):
            self._load_posts(os.path.join(root_dir, dir_, 'content'))
        self._conn.commit()
        self.root_dir = self._root_dir()

    def _load_posts(self, post_dir):
        if not os.path.isdir(post_dir):
            return
        for post in os.listdir(post_dir):
            if post.endswith('.markdown'):
                post = os.path.join(post_dir, post)
                self._load_post(post)

    def _load_post(self, post):
        with open(post, 'r') as fin:
            lines = fin.readlines()
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
        for i in range(0, index):
            line = lines[i]
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
        # parse content index to end
        content = ''.join(lines[index:])
        sql = '''
        INSERT INTO posts (
            path, dir, status, date, author, slug, title, category, tags, content
        ) VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
        '''
        self._conn.execute(sql, [post, blog_dir(post), status, date, author, slug, title, category, tags, content])

    def delete(self, post):
        os.remove(post)
        sql = 'DELETE FROM posts WHERE path = ?'
        self._conn.execute(sql, [post])
        self._conn.commit()

    def move(self, post, target):
        if target in (EN, CN, MISC):
            target = os.path.join(self.root_dir, target, 'content', os.path.basename(post))
        if post == target:
            return
        shutil.move(post, target)
        _update_post_move(target)
        sql = 'DELETE FROM posts WHERE path = ?'
        self._conn.execute(sql, [post])
        self._load_post(target)
        self._conn.commit()

    def edit(self, post, editor):
        with open(post, 'r', encoding='utf-8') as f:
            hash0 = hashlib.md5(f.read().encode('utf-8')).hexdigest()
        os.system(editor + ' "' + post + '"')
        with open(post, 'r', encoding='utf-8') as f:
            hash1 = hashlib.md5(f.read().encode('utf-8')).hexdigest()
        if hash1 != hash0:
            with open(post, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                if line.startswith('Date: 2'):
                    lines[i] = 'Date: {NOW_DASH}\n'
                    break
            with open(post, 'w', encoding='utf-8') as f:
                f.writelines(lines)
        sql = 'DELETE FROM posts WHERE path = ?'
        self._conn.execute(sql, [post])
        self._load_post(post)
        self._conn.commit()

    def _create_post(self, post, title):
        file_words = os.path.join(self.root_dir, 'words.json')
        with open(post, 'w', encoding='utf-8') as fout:
            fout.writelines('Status: published\n')
            fout.writelines(f'Date: {NOW_DASH}\n')
            fout.writelines('Author: Benjamin Du\n')
            fout.writelines('Slug: {}\n'.format(title.replace(' ', '-').replace('/', '-')))
            fout.writelines(f'Title: {_format_title(title, file_words)}\n')
            fout.writelines('Category: Programming\n')
            fout.writelines('Tags: programming\n')
            if blog_dir(post) == MISC:
                    fout.writelines(DECLARATION)

    def add(self, title, dir_) -> str:
        file = self.find_post(title, dir_)
        if not file:
            file = f'{TODAY_DASH}-{_slug(title)}.markdown'
            file = os.path.join(self.root_dir, dir_, 'content', file)
            self._create_post(file, title)
        self._load_post(file)
        sql = 'DELETE FROM srps'
        self._conn.execute(sql)
        sql = 'INSERT INTO srps SELECT * FROM posts WHERE path = ?'
        self._conn.execute(sql, [file])
        self._conn.commit()
        return file

    def find_post(self, title, dir_):
        """Find existing post matching the given title.

        :return: Return the path of the existing post if any, otherwise return empty string.
        """
        # find all posts and get rid of leading dates
        sql = 'SELECT path FROM posts WHERE path LIKE ? AND dir = ?'
        row = self._conn.execute(sql, [f'%{_slug(title)}.markdown', dir_]).fetchone()
        if row:
            return row[0]
        return ''

    def search(self, phrase: str):
        self._create_table_srps()
        self._conn.execute('DELETE FROM srps')
        sql = '''
            INSERT INTO srps
            SELECT * FROM posts WHERE posts MATCH '{}' ORDER BY rank
            '''.format(phrase)
        self._conn.execute(sql)
        self._conn.commit()

    def path(self, id_: int):
        sql = 'SELECT path FROM srps WHERE rowid = ?'
        result = self._conn.execute(sql, [id_]).fetchone()
        if result:
            return result[0]
        return ''

    def fetch(self, n: int):
        sql = 'SELECT rowid, * FROM srps LIMIT {}'.format(n)
        return self._conn.execute(sql).fetchall()

    def query(self, sql: str):
        return self._conn.execute(sql).fetchall()

    def publish(self, dirs):
        """Publish the specified blog to GitHub.
        """
        for dir_ in dirs:
            self._publish(dir_)

    def _publish(self, dir_):
        # pelican
        os.system(f'cd "{os.path.join(self.root_dir, dir_)}" && pelican . -s pconf_sd.py')
        # git push
        os.system(f'cd "{self.root_dir}" && ./git.sh {dir_}')
        print('\n' + DASHES)
        print('Please consider COMMITTING THE SOURCE CODE as well!')
        print(DASHES + '\n')

    def tags(self, dir_: str = '', where=''):
        sql = '''
            select distinct
                category
            from
                posts
            {where}
            order by
                category
            '''
        if where:
            sql = sql.format(where=where)
        else:
            # todo you can support quicker specific filtering in future
            sql = sql.format(where=where)
        cats = (row[0] for row in self._conn.execute(sql).fetchall())
        return cats

    def categories(self, dir_: str = '', where=''):
        sql = '''
            select distinct
                category
            from
                posts
            {where}
            order by
                category
            '''
        if where:
            sql = sql.format(where=where)
        else:
            # todo you can support quicker specific filtering in future
            sql = sql.format(where=where)
        cats = (row[0] for row in self._conn.execute(sql).fetchall())
        return cats


def query(blogger, args):
    rows = blogger.query(' '.join(args.sql))
    for row in rows:
        print(row)


def delete(blogger, args):
    if args.index:
        args.file = blogger.path(args.index)
    if args.file:
        blogger.delete(args.file)


def move(blogger, args):
    if args.index:
        args.file = blogger.path(args.index)
    if args.file:
        blogger.move(args.file, args.target)


def edit(blogger, args):
    if args.index:
        args.file = blogger.path(args.index)
    if args.file:
        if not shutil.which(args.editor):
            args.editor = 'vim'
        blogger.edit(args.file, args.editor)


def search(blogger, args):
    blogger.search(' '.join(args.phrase))
    show(blogger, args)


def show(blogger, args):
    for row in blogger.fetch(args.n):
        print('{id}: {path}'.format(id=row[0], path=row[1]))


def reload(blogger, args):
    blogger.reload_posts(args.root_dir)


def add(blogger, args):
    file = blogger.add(' '.join(args.title), args.sub_dir)
    blogger.edit(file, args.editor)


def publish(blogger, args):
    blogger.publish(args.sub_dirs)


def categories(blogger, args):
    cats = blogger.categories(dir_=args.sub_dir, where=args.where)
    for cat in cats:
        print(cat)


def parse_args(args=None, namespace=None):
    """Parse command-line arguments for the blogging util.
    """
    parser = ArgumentParser(
        description='Write blog in command line.')
    subparsers = parser.add_subparsers(help='Sub commands.')
    # parser for the category command
    parser_cat = subparsers.add_parser('cats', aliases=['c'], help='list all categories.')
    parser_cat.add_argument(
        '-w',
        '---where',
        dest='where',
        default='',
        help='a user-specified filtering condition.')
    parser_cat.add_argument(
        '-d',
        '---dir',
        dest='sub_dir',
        default='',
        help='the sub blog directory to list categories; by default list all categories.')
    parser_cat.set_defaults(func=categories)
    # parser for the reload command
    parser_reload = subparsers.add_parser('reload', aliases=['r'], help='reload information of posts.')
    parser_reload.add_argument(
        '-d',
        '--root-dir',
        dest='root_dir',
        default=os.getenv('blog_dir'),
        help='the root directory of the blog.')
    parser_reload.set_defaults(func=reload)
    # parser for the show command
    parser_list = subparsers.add_parser('list', aliases=['l'], help='list last search results.')
    parser_list.add_argument(
        '-n',
        dest='n',
        type=int,
        default=10,
        help='number of matched records to show.')
    parser_list.set_defaults(func=show)
    # parser for the search command
    parser_search = subparsers.add_parser('search', aliases=['s'], help='search for posts.')
    parser_search.add_argument(
        'phrase',
        nargs='+',
        help='the phrase to match posts.')
    parser_search.add_argument(
        '-n',
        dest='n',
        type=int,
        default=10,
        help='number of matched records to show.')
    parser_search.set_defaults(func=search)
    # parser for the add command
    parser_add = subparsers.add_parser('add', aliases=['a'], help='add a new post.')
    parser_add.add_argument(
        '-v',
        '--vim',
        dest='editor',
        action='store_const',
        const='vim',
        default=EDITOR,
        help='edit the post using vim.')
    parser_add.add_argument(
        '-e',
        '--en',
        dest='sub_dir',
        action='store_const',
        const=EN,
        default=MISC,
        help='create a post in the en sub blog directory.')
    parser_add.add_argument(
        '-c',
        '--cn',
        dest='sub_dir',
        action='store_const',
        const=CN,
        help='create a post in the cn sub blog directory.')
    parser_add.add_argument(
        'title',
        nargs='+',
        help='title of the post to be created.')
    parser_add.set_defaults(func=add)
    # parser for the edit command
    parser_edit = subparsers.add_parser('edit', aliases=['e'], help='edit a post.')
    parser_edit.add_argument(
        '-v',
        '--vim',
        dest='editor',
        action='store_const',
        const='vim',
        default=EDITOR,
        help='edit the post using vim.')
    parser_edit.add_argument(
        '-i',
        '--index',
        dest='index',
        type=int,
        help='rowid in the search results.')
    parser_edit.add_argument(
        '-f',
        '--file',
        dest='file',
        help='path of the post to be edited.')
    parser_edit.set_defaults(func=edit)
    # parser for the move command
    parser_move = subparsers.add_parser('move', aliases=['m'], help='move a post.')
    parser_move.add_argument(
        '-i',
        '--index',
        dest='index',
        type=int,
        help='rowid in the search results.')
    parser_move.add_argument(
        '-f',
        '--file',
        dest='file',
        help='path of the post to be moved.')
    parser_move.add_argument(
        '-t',
        '--target',
        dest='target',
        default=MISC,
        help='path of destination file')
    parser_move.add_argument(
        '-c',
        '--cn',
        dest='target',
        action='store_const',
        const=CN,
        help='move to the cn sub blog directory.')
    parser_move.add_argument(
        '-e',
        '--en',
        dest='target',
        action='store_const',
        const=EN,
        help='move to the en sub blog directory.')
    parser_move.add_argument(
        '-m',
        '--misc',
        dest='target',
        action='store_const',
        const=MISC,
        help='move to the misc sub blog directory.')
    parser_move.set_defaults(func=move)
    # parser for the publish command
    parser_publish = subparsers.add_parser('publish', aliases=['p'], help='publish the blog.')
    parser_publish.add_argument(
        '-c',
        '--cn',
        dest='sub_dirs',
        action='append_const',
        const=CN,
        default=[HOME],
        help='add the cn sub blog directory into the publish list.')
    parser_publish.add_argument(
        '-e',
        '--en',
        dest='sub_dirs',
        action='append_const',
        const=EN,
        help='add the en sub blog directory into the publish list.')
    parser_publish.add_argument(
        '-m',
        '--misc',
        dest='sub_dirs',
        action='append_const',
        const=MISC,
        help='add the misc sub blog directory into the publish list.')
    parser_publish.set_defaults(func=publish)
    # parser for the remove command
    parser_delete = subparsers.add_parser('delete', aliases=['d'], help='remove a post/page.')
    parser_delete.add_argument(
        '-i',
        '--index',
        dest='index',
        type=int,
        help='rowid of the file (in the search results) to delete.')
    parser_delete.add_argument(
        '-f',
        '--file',
        dest='file',
        help='path of the post to delete.')
    parser_delete.set_defaults(func=delete)
    # parser for the query command
    parser_query = subparsers.add_parser('query', aliases=['q'], help='run a SQL query.')
    parser_query.add_argument(
        'sql',
        nargs='+',
        help='the SQL to run')
    parser_query.set_defaults(func=query)
    # parse and run
    return parser.parse_args(args=args, namespace=namespace)


if __name__ == '__main__':
    blogger = Blogger()
    args = parse_args()
    args.func(blogger, args)
