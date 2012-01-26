import os
import yaml
import re
import markdown
import pygments
import calendar
import codecs
import memcache
from operator import itemgetter
from pygments import lexers, formatters
from BeautifulSoup import BeautifulSoup
from flask import Flask, render_template
from flaskext.markdown import Markdown


app = Flask(__name__)
Markdown(app)
mc = memcache.Client(['127.0.0.1:11211'], debug=0)

#
#
# filters




@app.template_filter('colour_for_date')
def colour_for_date(date):
    colours = [
        (255.0,27.7126443311),
        (245.578313253,34.2094985159),
        (203.248995984,49.2263282726),
        (154.297188755,61.2968854298),
        (95.9748995984,72.8323699422),
        (34.8704819277,75.0),
        (0.0,70.2606837,50),
        (7.51004016064,66.8215903765),
        (52.7921686747,56.165939981),
        (124.598393574,44.4600275525),
        (200.859437751,31.5213531977),
        (241.8062249,25.0),
    ]
    # get the month
    current = colours[date.month - 1 ]
    days_in_month = calendar.monthrange(date.year, date.month)
    days_in_month = days_in_month[1]
    # 
    try:
        next = colours[date.month]
    except IndexError:
        next = colours[0]
    hue_delta = next[0] - current[0]
    sat_delta = next[1] - current[1]
    hue_per_day = hue_delta / days_in_month
    sat_per_day = sat_delta / days_in_month
    hue = current[0] + (date.day * hue_per_day)
    sat = current[1] + (date.day * sat_per_day)
    
    return 'hsla(%s,%s%%,50%%, 1)' % (hue, sat)


@app.template_filter('archivedateformat')
def archivedateformat(value, format='%B %Y'):
    return value.strftime(format)

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%d %B %Y'):
    return value.strftime(format)

@app.template_filter('render')
def render(content):
    regex = re.compile(r'(<code(.*?)</code>)', re.DOTALL)
    code_blocks = []

    for i, m in enumerate(regex.finditer(content)):
        code = m.group(0)
        # if there is a lang attribute, use that
        if code.find('lang'):
            # get the language
            try:
                language = re.split(r'"|\'', code)[1]
                # fix some wonky lexers
                if language == 'conf': language = 'nginx'
                if language == 'regex': language = 'perl'
                # all goods
                lexer = pygments.lexers.get_lexer_by_name(language)
            except IndexError:
                lexer = pygments.lexers.guess_lexer(str(code))
        else:
            try: 
                lexer = pygments.lexers.guess_lexer(str(code))
            except ValueError:
                lexer = pygments.lexers.PythonLexer()
        # remove the code tags
        code = code.replace('</code>', '')
        code = code.replace('<code>', '')
        code = re.sub('<code(.*?)>', '', code)
        # create the pygmented code with the lexer
        pygmented_string = pygments.highlight(code, lexer, pygments.formatters.HtmlFormatter(linenos=True))
        # put the code blocks into the list for processintg later
        code_blocks.append(pygmented_string)
        # replace the <code> tags with placeholders that can be used to replace
        content = content.replace(m.string[m.start():m.end()], '{{CODE%s}}' % i)
    
    # now process as markdown
    content = markdown.markdown(content)
    # replaced placeholders with the actual code
    for i, code in enumerate(code_blocks):
        content = content.replace('<p>{{CODE%s}}</p>' % i, code)
        content = content.replace('{{CODE%s}}' % i, code)
    # return
    return content

#
# get post stuff
#
def get_post(slug, postdir="/Users/jcurle/Sites/jamiecurle/posts/"):
    key = str('get_post_%s' % slug.replace('.md', ''))
    print key
    cache = mc.get(key)
    if cache:
        return cache
    item = '%s%s' % (postdir, slug)
    with codecs.open(item, encoding='UTF-8') as md_file:
        contents = md_file.read()
    # split into yaml and markdown
    parts = contents.split('---')
    header = yaml.load(parts[0])
    content = markdown.markdown(parts[1])
    try:
        tags = header['tags']
    except KeyError:
        tags = []
    # now append a dict wit the info to posts
    post = {
        'url': '/posts/%s/' % item.split('/').pop().split('.')[0],
        'title': header['title'],
        'description': header['description'],
        'created': header['created'],
        'tags': tags,
        'content': content
    }
    mc.set(key, post)
    return post


def get_md_files(postdir="/Users/jcurle/Sites/jamiecurle/posts/"):
    cache = mc.get('get_md_files')
    if cache:
        return cache
    ls = [] # list of all markdown files
    for thing in os.listdir(postdir):
        try:
            ext = thing.split('.').pop()
            if ext == 'md':
                ls.append(thing)
        except IndexError:
            pass
    mc.set('get_md_files', ls)
    return ls

def get_posts(postdir="/Users/jcurle/Sites/jamiecurle/posts/"):
    cache = mc.get('get_posts')
    if cache:
        print 'cache'
        return cache
    #
    md_files = get_md_files()
    posts = [] # list of posts
    # now render out the posts from the list
    posts = []
    for md in md_files:
        post = get_post(md)
        posts.append(post)
    # sort them by date
    sorted_posts = sorted(posts, key=itemgetter('created'), reverse=True)
    mc.set('get_posts', sorted_posts)
    return sorted_posts

def get_tags():
    cache = mc.get('get_tags')
    if cache:
        return cache
    posts = get_posts()
    tags = {}
    for post in posts:
        for tag in post['tags']:
            tags[tag] = tags.get(tag, 0 ) + 1
    
    mc.set('get_tags', tags)
    return tags

def get_dates():
    cache = mc.get('get_dates')
    if cache:
        return cache
    posts = get_posts()
    dates = {}
    for post in posts:
        key = post['created'].strftime('%Y_%d')
        try:
            dates[key][1] = dates[key][1] + 1
        except KeyError:
            dates[key] = [post['created'], 1]
    mc.set('get_dates', dates)
    return dates

#
#
# views
@app.route('/about.html')
def about():
    cache = mc.get('about')
    if cache:
        return cache
    about = render_template('about.html')
    mc.set('about', about)
    return about

@app.route("/blog.html")
def blog_index():
    cache = mc.get('blog_index')
    if cache:
        return cache
    posts = get_posts()
    html  = render_template('blog_index.html', posts=posts)
    mc.set('blog_index', html)
    return html

@app.route("/")
def index():
    posts = get_posts()
    return render_template('index.html', posts=posts)


@app.route("/posts/<slug>/")
def post(slug):
    key = str('post_%s' % slug)
    cache = mc.get('key')
    if cache:
        return cache
    post = get_post('%s.md' % slug )
    tags = get_tags()
    dates = get_dates()
    html = render_template('post.html', post=post, tags=tags, dates=dates)
    mc.set(key, html)
    return html

@app.route("/tags.html")
def tags():
    tags = get_tags()
    return render_template('tags.html',tags=tags)

@app.route("/tags/<tag>/")
def tag(tag):
    tagged_posts = [post for post in get_posts() if tag in post['tags']]
    return render_template('tag.html',
        tagged_posts=tagged_posts,
        tag=tag)

if __name__ == '__main__':
    app.run(debug=True)