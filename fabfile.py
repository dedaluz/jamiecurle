from fabric.api import *
import datetime
import os

def output():
    with settings(warn_only=True):
        local('wget -mk http://127.0.0.1:5000  --no-parent --directory-prefix=/Users/jcurle/Sites/jc_static')
    #local('mv /Users/jcurle/Sites/127.0.0.1/5000  /Users/jcurle/Sites/jc_static')


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

