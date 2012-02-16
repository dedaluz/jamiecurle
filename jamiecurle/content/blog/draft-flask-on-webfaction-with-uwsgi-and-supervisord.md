title: "Running Flask on Webfaction with uwsgi and supervisord"
description: "I've always used webfaction for hosting Django sites, but it really is a very, very flexible platform. Setting up Flask was a breeze."
created: 2012-01-15 07:59:59
tags:
  - development
  - flask
  - webfaction
---


If you're looking at all of this and thinking <q>Er, this all looks a little bit complicated</q> don't worry. It's quite straight forward and in practice we're only doing a few things. There could be a much easier way to do this if you weren't going to be hosting anything else on your webfaction account, however I am and this is how I do it :)

1. Setting up the environment and installing some stuff.
2. Getting the flask app up and running with supervisor
3. Connecting a custom webfaction application to our supervisor process

## 1. Setting Up The Environment

### Python 2.7

I wanted to make sure that I was using python2.7 ( _python2.5 which seems to be the default on webfaction_ ). A quick edit of `~/.bashrc` to alias python does the trick &hellip;

<code lang="bash">
alias python=python2.7
</code>

### Installing Pip, virtualenv and virtualenvwrapper

Using [pip][0], [virtualenv][1] and [virtualenvwrapper][2] is a no brainer if you're working with python. Pip is great for installing python packages, virtualenv gives you the ability to have seperate python applications have their own environment and virtualenvwrapper makes working with virtualenv a breeze.

Before you can install pip on webfaction you have to create the `~/lib/python2.7` directory because it doesn't exist by default &hellip;

<code lang="bash">
mkdir ~/lib/python2.7
</code>

Once that's done you can install pip using easy_install-2.7 &hellip;

<code lang="bash">
easy_install-2.7  pip
</code>

Then you can install virtualenv and virtualenvwrapper &hellip;

<code lang="python">
pip install virtualenv virtualenvwrapper
</code>

You'll have to do a little bit of jiggery pokery now to configure virtualenvwrapper. First things first you'll have to add a few commands to your `$HOME/.bashrc file` &hellip;

<code lang="bash">
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python2.7
source $HOME/bin/virtualenvwrapper.sh
</code>

And then finally reload your .bashrc file. Because this is the first time virtualenvwrapper will have been loaded into your shell, it'll create it's various scripts.

<code lang="bash">
source ~/bin/virtualenvwrapper.sh
</code>


### Installing supervisor

[Supervisor][3] is a tool for controlling processes. It's actually two tools. The first `supervisord` is the deamon that runs the processes. The second, `supervisorctl` allows you to control the processes (start, stop, reload) and perform admin (add, delete, update) on the processes. It's a really nice system that I've been using to [serve django with for a couple of years][6]

In this case we're going to use it to control a [uwsgi][4] process.  Installation with pip is easy &hellip;

<code lang="python">
pip install supervisor
</code>

Webfaction is a shared environment, so you can't go around installing things into there usual locations, so you have to do a little bit of fiddling with the supervisor configuration to get it to play nicely in the webfaction environment. If you try and run it with the command `supervisord` it will bork, complaining about a lack of configuration file.  I'm only overriding the [supervisors default configuration][7] that I need/want to. Here's my `$HOME/etc/supervisord.ini` config file &hellip;

<code lang="ini">
[unix_http_server]
file=/home/you/tmp/supervisor.sock
[supervisord]
logfile=/home/you/tmp/supervisord.log
logfile_maxbytes=10MB
pidfile=/home/you/tmp/supervisord.pid
[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
[supervisorctl]
serverurl=unix:///home/you/tmp/supervisor.sock
[include]
files = /home/you/conf/supervisor/*.ini
</code>

To make this config work, you'll have to create $HOME/tmp/ &hellip;

<code lang="bash">
mkdir $HOME/tmp
</code>

Now you'll be able to run it like so &hellip;

<code lang="bash">
supervisord -c /home/you/etc/supervisord.conf
</code>

It should start up without any problems. You can check that it's running with a quick command `ps auxw | grep supervisord` and you should see your supervisord process listed back at you.

It would also be prudent to try and connect to `supervisorctl`. You shouldn't see any errors when you do this. If you do, make sure that supervisord is running.  At this stage you'll see nothing terribly exciting.

<code lang="bash">
supervisorctl
</code>

<hr>

## 2 - Getting the flask app up and running with supervisor

It's time to start getting specific now and putting together the final application. 


### Put the project on the server.

[I use github] to store my code and I also use it to deploy. Getting the project onto the server is really simple.

<code lang="bash">
cd ~/sites/jamiecurle/
git clone git@github.com:jamiecurle/jamiecurle.git
</code>


### Create a Virtual Environment

Create a virtualenv for the flask app to live in, because my app is called `jamiecurle`, that's the name I'm going to use  &hellip;

<code lang="bash">
mkvirtualenv jamiecurle
</code>

This will create the virtualenv and automatically put your shell into it. Anything you do with pip from this point forward will only impact your virtualenvironment - perfect.

### Install the dependancies

Now that we have our virtualenvironment set up we can install the requirements for the project. My flask app has a few and they're all stored in a requirements.txt file. This will take a few minutes.

<code lang="bash">
cd ~/sites/jamiecurle/jamiecurle
pip install -r requirements.txt
</code>

### Load the config for the app into Supervisorctl

To make working with multiple sites easy, my supervisord config has this line in it &hellip; 

<code lang="ini">
[include]
files = /home/you/conf/supervisor/*.ini
</code>

I'm going to create symlink from my app to the `/home/you/conf/supervisor/` directory so that supervisor can read my config. I'm symlinking it and not copying it incase I do an update that changes the config file.

<code lang="bash">
ln -s /home/you/sites/jamiecurle/jamiecurle/supervisor.ini /home/you/conf/supervisor/jamiecurle.ini
</code>

Here's the config, I'll talk about the specifics a little later &hellip;

HAD TROUBLE WITH THE COMMAND

<code lang="ini">
[program:jc_flask]
command=uwsgi --socket 127.0.0.1:26331 --file runserver.py --callable app --processes 2 --venv /home/curle/.virtualenvs/jamiecurle/ 
directory=/home/curle/sites/jamiecurle/jamiecurle
user=jcurle
autostart=true
autorestart=true
redirect_stderr=true
stopsignal=QUIT
</code>


Now let's jump into supervisorctl and load up the config &hellip;

<code lang="bash">
supervisor
reread
add your_app
status
your_app      BACKOFF    can't find command 'uwsgi'
</code>

Partial su, 







[0]: http://pypi.python.org/pypi/pip
[1]: http://pypi.python.org/pypi/virtualenv
[2]: http://www.doughellmann.com/projects/virtualenvwrapper/
[3]: http://supervisord.org/
[4]: http://projects.unbit.it/uwsgi/
[6]: /blog/serving-django-as-nginx-and-supervisord-sandwich-with-a-gunicorn-filling/
[7]: http://supervisord.org/configuration.html
[8]: https://github.com/jamiecurle