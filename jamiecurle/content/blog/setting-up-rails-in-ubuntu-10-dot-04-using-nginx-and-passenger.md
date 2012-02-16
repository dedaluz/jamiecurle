title: "Setting up Rails in Ubuntu 10.04 using Nginx and Passenger"
description: "My VPS has been set up for Django, here's what I had to do to get it set up for rails."
created: 2010-12-19 00:00:00
---

![Rails on Ubuntu](/media/2010/12/19/blogimage/Rails_on_Ubuntu.850x600.jpg)

I blogged yesterday about [switching this site from Django to Rails](/blog/2010/12/django-rails.html) because I think it's time that I got to know Rails. I've been ignoring it too long and I'm sick of being a one trick pony (pun intended). So when I woke up at 6:40am ( benefits of going to bed very early ) I though it would be a good idea to deploy a 'hello world' rails app onto my VPS.  Aside from an experience with rails back in 2005 (apache & cgi, very very slow), this is my first attempt at deploying a rails app.

[The Pragmatic guide to installing rails & ruby on mac](http://pragmaticstudio.com/blog/2010/9/23/install-rails-ruby-mac)  translates to installing on Ubuntu very well, though there are a few minor deviations you'll have to make.

Before we start we're going to need some tools. I'm a little amazed I hadn't needed most of these already when setting my server up for Django.

<code lang="bash">
$ sudo apt-get install gcc sqlite3 libsqlite3-dev zlibc libzlib-dev libmysqld-dev libmysqlclient-dev
</code>

Time to install [Ruby Version Manager (RVM)](http://rvm.beginrescueend.com/), being used to virtualenv, this makes me feel right at home.

<code lang="bash">
$ bash < <( curl http://rvm.beginrescueend.com/releases/rvm-install-head )
</code>

Then append to .bashrc to give me access to rvm

<code lang="bash">
[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm"
</code>

Just check everything is as it should be

<code lang="bash">
$ type rvm | head -n1
rvm is a function
</code>

Now install Ruby version 1.9.2

<code lang="bash">
$ rvm install 1.9.2
</code>

At this stage [the Pragmatic guide](http://pragmaticstudio.com/blog/2010/9/23/install-rails-ruby-mac) suggests checking the ruby version, but when I did this I was greeted with 

<code lang="bash">
$ ruby -v
-bash: ruby: command not found
</code>

Easily fixed by setting the default version using rvm, I suspect the command not found error is because there was no version of ruby installed  - clue is in the title!

<code lang="bash">
$ rvm --default ruby-1.9.2-p0
$ ruby -v
ruby 1.9.2p0 (2010-08-18 revision 29036) [i686-linux]
</code>

[The Pragmatic guide](http://pragmaticstudio.com/blog/2010/9/23/install-rails-ruby-mac) suggests checking the version of gems

<code lang="bash">
$ gem -v
1.3.7
</code>

Now we can get busy installing gems that are going to be needed by rails.

<code lang="bash">
$ gem install sqlite3-ruby mysql
</code>

And now for rails and once it's installed, check the version.

<code lang="bash">
$ gem install rails
$ rails -v
Rails 3.0.3
</code>

All set up, let's install passenger which we'll be using to deploy my simple app.  I don't want to touch the system by using apt-get to install, so I'll do it from source

<code lang="bash">
$ mkdir $HOME/src
$ cd src
$ wget wget http://rubyforge.org/frs/download.php/73563/passenger-3.0.1.tar.gz
$ tar xzvf passenger-3.0.1.tar.gz
$ cd passenger-3.0.1
$ ./bin/passenger-install-nginx-module
 * GNU C++ compiler... not found
 * The 'make' tool... found at /usr/bin/make
 * A download tool like 'wget' or 'curl'... found at /usr/bin/wget
 * Ruby development headers... found
 * OpenSSL support for Ruby... not found
 * RubyGems... found
 * Rake... found at /home/jcurle/.rvm/wrappers/ruby-1.9.2-p0/rake
 * rack... found
 * Curl development headers with SSL support... not found
 * OpenSSL development headers... not found
 * Zlib development headers... not found
</code>

Hmm, I'm missing some things

<code lang="bash">
$ sudo apt-get install build-essential libopenssl-ruby libcurl4-openssl-dev libssl-dev zlib1g-dev
</code>

Build ruby again so we have ssl support

<code lang="bash">
$ rvm install 1.9.2
</code>

Hmm, still no biscuit. Google to the rescue, [thank you Seth Ladd](http://blog.sethladd.com/2007/03/installing-openssl-support-for-ruby-on.html).

<code lang="bash">
$ cd .rvm/src/ruby-1.9.2-p0/ext/openssl/
$ ruby extconf.rb
$ make
$ make install 
$ cd $HOME/src/passenger-3.0.1
</code>

Now we can install passenger. The install promised to leave my config files alone, but just incase I backed them up. Using a custom compiled version of nginx is ok with me, all the apt-get installed version has been doing is proxying gunicorn for my Django apps.  

In the install process I selected option 1 and I installed it to $HOME/local/nginx

<code lang="bash">
$ ./bin/passenger-install-nginx-module
</code>

All good, time to move my config files from my original nginx install to the custom one.

<code lang="bash">
$ sudo mv /etc/nginx/sites-available/*.com $HOME/local/nginx/vhosts/*
</code>

Now tell my new nginx to include them

<code lang="javascript">
http {
*
*  blah blah blah
*
*
   include /path/to/local/nginx/conf/vhosts/*;
}
</code>

Now it's just a case of stopping the apt-get installed nginx and starting my own. I still have to do this as root,  because I'll be running it on port 80. Whilst I'm at it, I'll also remove the apt-get version of nginx

<code lang="bash">
$ sudo /etc/init.d/nginx stop
$ sudo $HOME/local/nginx/sbin/nginx
</code>

Finally, now I'm able to create a hello world rails app and deploy it. Here's the config for my nginx vhost

<code lang="javascript">
server{
  server_name hello.jamiecurle.com;
  root /path/to/hello/public;
  autoindex on;
  passenger_enabled on;
}
</code>

Restart nginx,  [create a little rails app](//hello.jamiecurle.com/), set the root in config/routes.rb, restart my rails app ( touch tmp/restart.txt) and I'm done.

![A little basic app](/media/2010/12/19/blogimage/A_little_basic_app.850x600.jpg)

This was my first experience of deploying a rails app. I know I'm bringing in a lot of experience from my time working with Django, so it would be unfair to say that rails installs easier, but on the whole there was only a little pain. Once everything is up and running I have to say that passenger makes deployment a joy, actually more joyful than using supervisord and gunicorn. 

What get's me really excited though is that there are services like [Heroku](http://heroku.com/) that I can use for some of my more fanciful adventures without firing up VPS's all over the place.

Breakfast Time - Not so chunky bacon and eggs.
