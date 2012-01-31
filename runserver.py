# -*- coding: utf-8 -*-
from flaskext.markdown import Markdown
from jamiecurle import create_app
from jamiecurle.helpers import url, filter
app = create_app(__name__)

if app.config['DEBUG']:
    app.debug = True

#
#
# extentions
Markdown(app)
#
#
# tmp urls  for 301- can be removed once SE's have updated
url(app, '/posts/', 'modules.blog.views.blog_redirect')
url(app, '/posts/<int:year>/<int:month>/', 'modules.blog.views.blog_redirect')
url(app, '/posts/<string:slug>/', 'modules.blog.views.blog_redirect')
#
#
# urls
url(app, '/about.html', 'views.about')
url(app, '/blog.html', 'modules.blog.views.blog_index')
url(app, '/blog/<int:year>/<int:month>/', 'modules.blog.views.blog_archive')
url(app, '/blog/<string:slug>/', 'modules.blog.views.blog_post')
url(app, '/tags.html', 'modules.blog.views.blog_tags')
url(app, '/tags/<string:tag>/', 'modules.blog.views.blog_tagged')
url(app, '/projects.html', 'modules.projects.views.project_index')
url(app, '/', 'views.home')
#
#
# template filters
filter(app, 'colour_for_date', 'modules.blog.filters.colour_for_date')
filter(app, 'archivedateformat', 'modules.blog.filters.archivedateformat')
filter(app, 'datetimeformat', 'modules.blog.filters.datetimeformat')
filter(app, 'render', 'modules.blog.filters.render')



app.run()
