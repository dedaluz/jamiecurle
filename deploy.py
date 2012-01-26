import os
import codecs
from distutils.dir_util import copy_tree
from markdown import markdown
from jinja2 import Environment, FileSystemLoader
from jc import app, get_posts, get_post, colour_for_date, datetimeformat,\
                render, get_md_files, archivedateformat, get_dates


ROOT = os.path.dirname(os.path.abspath(__file__))

env = Environment(loader=FileSystemLoader(os.path.join(ROOT, 'templates')))
env.filters['colour_for_date'] = colour_for_date
env.filters['datetimeformat'] = datetimeformat
env.filters['render'] = render
env.filters['markdown'] = markdown
env.filters['archivedateformat'] = archivedateformat


def deploy():
    # make output dir
    outdir = _mkdir('output')
    postsdir = _mkdir('output/posts')
    # do the index
    template = env.get_template('index.html')
    with codecs.open(os.path.join(outdir, 'index.html'), 'w+', encoding='UTF-8') as index:
        index.write(template.render())
    # About Me
    # do the index
    template = env.get_template('about.html')
    with codecs.open(os.path.join(outdir, 'about.html'), 'w+', encoding='UTF-8') as index:
        index.write(template.render())
    # make the blog archive
    posts = get_posts()
    template = env.get_template('blog_index.html')
    with codecs.open(os.path.join(outdir, 'blog.html'), 'w+', encoding='UTF-8') as index:
        index.write(template.render(posts=posts))
    # make each post in it's own directory
    md_files = get_md_files()
    for md_file in md_files:
        # make slug 
        slug = md_file.split('.')[0]
        # create the folder
        post_dir = _mkdir(os.path.join('output/posts/', slug))
        # render the post out as index.html
        template = env.get_template('post.html')
        with codecs.open(os.path.join(post_dir, 'index.html'), 'w+', encoding='UTF-8') as index:
            post = get_post('%s.md' % slug)
            index.write(template.render(post=post))
    # make each tag
    #
    #
    
    # do the about
    # copy the static folder to the outdir
    copy_tree(os.path.join(ROOT, 'static'), 
                os.path.join(outdir, 'static'))

def _mkdir(dir):
    path = os.path.join(ROOT, dir)
    if not os.path.exists(path):
        os.mkdir(path)
    return path

if __name__ == '__main__':
    deploy()