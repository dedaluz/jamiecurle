title: "Installing Pip, Virtualenv & VirtualenvWrapper on OS X"
description: "It's good form to create isolated virtual environments for each django project. But before you can do this, you need to install some stuff."
created: 2011-01-12 10:33:53
---

I can't ever imagine how I managed without [virtualenv](http://pypi.python.org/pypi/virtualenv), I really can't.  Having each django project or python mind-fart in it's own little sandbox is brilliant because it doesn't matter what version of anything you have, there'll be no "inter-project-versioning-clashes". However, before you can enjoy the good times there are a few things you'll need to do first. Don't worry though because you only have to do this once.

First things first, open up a terminal.

## Pip

We're going to use [pip](http://pypi.python.org/pypi/pip) to install [virtualenv](http://pypi.python.org/pypi/virtualenv) and [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/) so we need to install that first.

Installing pip is easy, but note that we're going to use sudo because we want pip installed system wide.

<code lang="bash">
sudo easy_install pip
</code>

Let's check the install.  

<code lang="bash">
pip
</code>

It should come back with something like this 

<code lang="bash">
Usage: pip COMMAND [OPTIONS]
pip: error: You must give a command (use "pip help" to see a list of commands)
</code>

Very good, let's install virtualenv.

## Virtualenv

We can now install virtualenv, again we're doing this system wide.

<code lang="bash">
sudo pip install virtualenv
</code>

Let's check that

<code lang="bash">
virtualenv
</code>

And it should come back with a lot of output. It'll start something like this, but I've omitted most of it.

<code lang="bash">
virtualenv
You must provide a DEST_DIR
...
</code>

## VirtualenvWrapper

Now install virtualenvwrapper, again this is systemwide.

<code lang="bash">
sudo pip install virtualenvwrapper
</code>

Here's where you have to do something a little different. In your home directory make a folder called .virtualenvs, If you don't do this virtualenvwrapper will whinge at you

<code lang="bash">
cd $HOME
mkdir .virtualenvs
</code>

You now need to have your shell loadup the virtualenvwrapper.sh script. To do this we're going to add a line into your .bash_login file. I like to use vi for things like this but you could use anything you want to edit the file.  Here's how to open it up in vi

<code lang="bash">
vi .bash_login
</code>

Now add the following line ( remember to press 'i' to get into insert mode) into the bottom of your file. This will load up the virtualenvwrapper.sh script into your terminal windows. This will give you the power of virtualenvwrapper.  Once you've added the line you should write and quit out of vi.  ( escape, colon, w, q, return)

<code lang="bash">
source /usr/local/bin/virtualenvwrapper.sh
</code>

Now close your terminal window/tab and open up a new one.  (_There are other ways to reload your .bash_login, but this one is the quickest. for me_) Because is the first time that the virtualenvwrapper script has ran it may output some  stuff.

Now lets check it.  You should be able to just type, m,k,v and then tab and it should autocomplete.

<code lang="bash">
mkvirtualenv
</code>

It should spit some stuff back at you. 

If it does then you've cracked it.  Welcome to good times. 

From here on out the [documentation for virtualenvwrapper](http://www.doughellmann.com/docs/virtualenvwrapper/) will be your best friend.


   [1]: http://pypi.python.org/pypi/virtualenv
   [2]: http://pypi.python.org/pypi/pip
   [3]: http://www.doughellmann.com/projects/virtualenvwrapper/
   [4]: http://www.doughellmann.com/docs/virtualenvwrapper/


