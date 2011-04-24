from fabric.api import *

env.hosts = ['jamiecurle.com']
env.user = 'jcurle'

def deploy():
    local('git commit -a')
    local('git push origin master')
    run('cd sites/jamiecurle/jamiecurle/; git pull origin master')
    run('supervisorctl restart reflection')

