from fabric.api import *


env.hosts = ['jamiecurle.com']
env.user = 'jcurle'


def deploy():
    local('git commit -a')
    run('cd sites/jamiecurle/jamiecurle/; git pull origin master; touch tmp/restart')
