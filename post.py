#!/usr/bin/python3
def draft(root="."):
    import os
    if type(root) == list:
        if len(root) == 0:
            draft()
            return
        #endif
        draft(" ".join(root))
        return
    #endif
    cdir = os.path.join(root, 'content')
    ps = [os.path.join(cdir, p) for p in os.listdir(cdir) if p.endswith(".md") or p.endswith(".markdown")]
    links = []
    index = None
    for p in ps:
        if p.endswith("index.markdown") or p.endswith("index.md"):
            index = p
            continue
        #end if
        parse_draft(p, links)
    #endfor
    links.sort(reverse=True)
    links = [slug[1] for slug in links]
    lines = meta_lines(index)
    lines.extend(links)
    open(index, 'w').writelines(lines)
#edef draft
def post(root="."):
    import os
    if type(root) == list:
        if len(root) == 0:
            post()
            return
        #endif
        post(" ".join(root))
        return
    #endif
    cdir = os.path.join(root, 'content')
    ps = [os.path.join(cdir, p) for p in os.listdir(cdir) if p.endswith(".md") or p.endswith(".markdown")]
    links = []
    index = None
    for p in ps:
        if p.endswith("index.markdown") or p.endswith("index.md"):
            index = p
            continue
        #end if
        parse_post(p, links)
    #endfor
    links.sort(reverse=True)
    links = [slug[1] for slug in links]
    lines = meta_lines(index)
    lines.extend(links)
    open(index, 'w').writelines(lines)
#edef post
def meta_lines(post):
    lines = open(post).readlines()
    n = len(lines)
    for i in range(n):
        line = lines[i].strip()
        if line == "":
            lines = lines[:i]
            break
        #end if
    #end for
    return lines
#end def meta_lines
def parse_draft(post, links):
    """@todo: Docstring for post.

    :arg1: @todo
    :returns: @todo

    """
    lines = open(post).readlines()
    status = "published"
    date = None
    title = None
    slug = None
    ntags = 4
    count = 0
    for line in lines:
        if line.startswith("Status: "):
            status = line[7:].strip()
            if status == "published":
                break
            #end if
            ++count
            if count >= ntags:
                break
            #end if
            continue
        #end if
        if line.startswith("Date: "):
            date = line[5:].strip()
            ++count
            if count >= ntags:
                break
            #end if
            continue
        #end if
        if line.startswith("Title: "):
            title = "[" + line[6:].strip() + "]"
            ++count
            if count >= ntags:
                break
            #end if
            continue
        #end if
        if line.startswith("Slug: "):
            slug = line[5:].strip()
            ++count
            if count >= ntags:
                break
            #end if
        #end if
    #end for
    if status == "published":
        return
    #end if
    if status != "draft":
        warnings.warn("Post \"" + post + "\" has invalid value for status!")
        return
    #end if
    links.append([date, "\n\n" + title + '(' + slug + ".html)"])
#end parse_draft

def parse_post(post, links):
    """@todo: Docstring for post.

    :arg1: @todo
    :returns: @todo

    """
    lines = open(post).readlines()
    date = None
    title = None
    slug = None
    ntags = 3
    count = 0
    for line in lines:
        if line.startswith("Date: "):
            date = line[5:].strip()
            ++count
            if count >= ntags:
                break
            #end if
            continue
        #end if
        if line.startswith("Title: "):
            title = "[" + line[6:].strip() + "]"
            ++count
            if count >= ntags:
                break
            #end if
            continue
        #end if
        if line.startswith("Slug: "):
            slug = line[5:].strip()
            ++count
            if count >= ntags:
                break
            #end if
        #end if
    #end for
    links.append([date, "\n\n" + title + '(' + slug + ".html)"])
#end def parse_post
if __name__ == '__main__':
    import sys
    sys.argv.pop(0)
    draft(sys.argv)
#endif

