title: "Installing Xapian on webfaction"
description: "It's about time I documented how to install xapian on webfaction."
created: 2010-12-01 00:00:00
---

![Xapian Logo](http://media.jamiecurle.com/uploads/2010/12/01/blogimage/Xapian_Logo.850x600.jpg)

Haystack is a great search engine for django and it supports three backends

* Solr
* Whoosh
* Xapian

Xapian is the best choice for webfaction (for me) because it has many of the nice features of solr whilst not running like a daemon so it doesn't use up precious memory. Installing it can be an arse though so I thought I'd document the process.

## Download the xapian-core and xapian bindings.

Pretty straight forward stuff.

<code lang="bash">
mkdir src
cd src
http://oligarchy.co.uk/xapian/1.2.3/xapian-core-1.2.3.tar.gz
http://oligarchy.co.uk/xapian/1.2.3/xapian-bindings-1.2.3.tar.gz
tar -xzvf xapian-core-1.2.3.tar.gz
tar -xzvf xapian-bindings-1.2.3.tar.gz
</code>

## Install Xapian

We're in a shared environment so we don't have permission to install into the system folders. I'm going to install it into $HOME/local/xapian. It'll take a few minutes so it's the perfect time to grab a coffee or have an impromptu [power move rehearsal](http://www.youtube.com/watch?v=itq1GBROM_g)

<code lang="bash">
cd xapian-core-1.2.3
mkdir -p $HOME/local/xapian
./configure --prefix=$HOME/local/xapian/
make
make install
</code>

## Install Xapian Bindings

This is the one that always unsticks me.

I'll be using python2.6 from a virtualenv so I'm going to activate that one now. If you're not using a virtualenv then you don't need to do this. ( my virtual environment is called staging26, your's will be different)

<code lang="bash">
workon staging26
</code>

Now for the money shot. It should all go according to plan -- no errors.

<code lang="bash">
cd ../xapian-bindings-1.2.3
./configure --with-python --prefix=$HOME/local/xapian-bindings XAPIAN_CONFIG=$HOME/local/xapian/bin/xapian-config
make
make install
</code>

## Check it

Fire up the python shell and try to import the module

<code lang="bash">
$HOME/.virtualenvs/staging26/bin/python -c "import xapian"
</code>

No errors? [Bingo](http://www.youtube.com/watch?v=UMRo5XCKddQ)

## Just one last thing

What's that columbo? could it be that I've omitted to rebuild the index? Well yes it could, but make sure you're in the same directory as your django project!

<code lang="bash">
./manage.py rebuild_index
</code>

Fancy that.