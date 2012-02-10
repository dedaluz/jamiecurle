from fabric.api import *
import datetime
import os
import memcache



def clear_cache(key=None):
    mc = memcache.Client(['127.0.0.1:11211'], debug=0)
    if key is None:
        mc.flush_all()
    else:
        mc.delete(key)


def compress_css():
    with lcd('jamiecurle/static/css/'):
        local('cssprefixer about.css devices.css global.css syntax.css --minify > production.css')

def deploy(message=None):
    if message is not None:
        local('git add -A')
        local('git commit -a -m "%s"' % message)
        local('git push origin master')

    maintenance()
    run('cd sites/jamiecurle/jamiecurle/; git pull origin master')
    run('cd /home/jcurle/sites/jamiecurle/jamiecurle/; /home/jcurle/.virtualenvs/jamiecurle/bin/python manage.py syncdb --migrate')
    run('supervisorctl restart jamiecurle')
    maintenance_end()

