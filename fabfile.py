from fabric.api import *
import datetime
import os
import memcache

env.hosts = ['curle.webfactional.com']
env.user = 'curle'



def clear_cache_dev(key=None):
    mc = memcache.Client(['127.0.0.1:11211'], debug=0)
    if key is None:
        mc.flush_all()
    else:
        mc.delete(key)

def compress_css():
    with lcd('/Users/jcurle/Sites/jamiecurle/jamiecurle/static/css/'):
        local('cssprefixer about.css devices.css global.css syntax.css --minify > production.css')

def mem():
    run('ps -u curle -o pid,rss,command')

def restart_nginx():
    run('nginx -s reload')

def clear_cache():
    run('/home/curle/.virtualenvs/jamiecurle/bin/python2.7 -c "import memcache;MC = memcache.Client([\'unix:/home/curle/tmp/memcached.sock\'], debug=0);MC.flush_all()"')
    #run('rm /home/curle/tmp/memcached.sock;')
    #run('memcached -d -m 10m -s /home/curle/tmp/memcached.sock')


def deploy(message=None):
    # compress css
    compress_css()
    # commit and push to github
    if message is not None:
        local('git add -A')
        local('git commit -a -m "%s"' % message)
        local('git push origin master')
    #maintenance()
    run('cd sites/jamiecurle/jamiecurle/; git pull origin master')
    # restart the app
    run('touch /home/curle/sites/jamiecurle/uwsgi')
    # restart_nginx
    restart_nginx()
    #maintenance_end()
    clear_cache()

