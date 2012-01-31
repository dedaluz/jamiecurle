title: "Memcached on OSX without Macports"
description: "How to install memcached on a development machine running OSX."
created: 2010-09-19 00:00:00
---

_Edit: December 2010 : Since writing this post, I've discovered [Homebrew](https://github.com/mxcl/homebrew) and it's very reliable for installing OSX packages.  To install memcached using homebrew is as easy as `brew install memcached`_

For good or bad I don't use Macports - I've found that it's great, but it will always let me down just when I need it.

When developing this site in 2010 I solved something that I've been toying with for a while  - using the content of a model field as a template. It wasn't that difficult to solve and it's been very useful. However I found it was a little wasteful rendering the field as a template, the processing the result through textile and then passing that through pygments. I toyed with the idea of adding an extra model field and using signals to render the contents on save, however this also seemed a little wasteful.  The obvious solution was to save the contents in memcached. I could have quite easily just used memcached in production and used the dummy cache in development, but that would have been too easy.

### First get the code

First make a folder called 'src' in your home folder and download the code into it

<code lang="bash">
cd $HOME
mkdir src
cd src
curl -O http://memcached.googlecode.com/files/memcached-1.4.5.tar.gz
curl -O http://monkey.org/~provos/libevent-1.4.14b-stable.tar.gz
</code>

### Install libevent

Libevent is required before you can installed memcached so lets install that

<code lang="bash">
tar xzvf libevent-1.4.14b-stable.tar.gz
cd libevent-1.4.14b-stable
./configure
make
sudo make install
</code>

### Install Memcached

Now that libevent is installed, we can now install memcached

<code lang="bash">
cd ../
tar xzvf memcached-1.4.5.tar.gz
cd memcached-1.4.5
./configure
make 
sudo make install
</code>

###  Quick Test

Memcached is now installed so let's test it.   Start up memcached 

<code lang="bash">
memcached
</code>

That'll start up a memcached process that we can telnet into. In a new terminal window/tab telnet into memcached

<code lang="bash">
telnet localhost 11211
stats
quit
</code>

After typing stats memcached should return the statistics about the process.  We could actually stop there as we've now get memcached installed and working, but I think it's a it messy running like this. Launchctl is the preferred ( or enforced )  method of running services on OSX so lets set that up.

If you need to stop that memcached process you started, hit ctrl + c

###  Running memcached with launchctl

Please note, I'm not an expert in this if it works, it's good enough for me, so if you have a better way of doing this let me know in the comments. In order to control memcached with launchctl we need a plist file. Let's create the plist file in the right place

<code lang="bash">
sudo touch /Library/LaunchDaemons/org.memcached.plist
sudo vi /Library/LaunchDaemons/org.memcached.plist
</code>

Here's one I made earlier, it might not be pretty but it gets the job done.

<code lang="xml">
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>memcached</string>
    <key>Program</key>
    <string>/usr/bin/memcached</string>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
</code>


**edit**

As "crap" kindly pointed out in the comments a small change to the plist will get memcached to run at boot. I didn't have a problem using the above, but if you do then this may offer help for you...

<code lang="xml">
<plist version="1.0">
<dict>
        <key>Label</key>
        <string>memcached</string>
        <key>Program</key>
        <string>/usr/bin/memcached</string>
        <key>ProgramArguments</key>
        <array> 
        <string>memcached</string> 
            <string>-u</string> 
            <string>root</string>
        </array>
        <key>RunAtLoad</key>
        <true></true>
    </dict>
</plist>
</code>

Copy in the above contents into the plist file and save – now we're ready to test. 

<code lang="bash">
launchctl load /Library/LaunchDaemons/org.memcached.plist
telnet localhost 11211
stats
</code>

and you should see some output like this

<code lang="bash">
STAT pid 7498
STAT uptime 40
STAT time 1284905866
STAT version 1.2.8
STAT pointer_size 64
STAT rusage_user 0.004227
STAT rusage_system 0.015816
STAT curr_items 0
STAT total_items 0
STAT bytes 0
STAT curr_connections 4
STAT total_connections 6
STAT connection_structures 5
STAT cmd_flush 0
STAT cmd_get 0
STAT cmd_set 0
STAT get_hits 0
STAT get_misses 0
STAT evictions 0
STAT bytes_read 37
STAT bytes_written 562
STAT limit_maxbytes 67108864
STAT threads 2
STAT accepting_conns 1
STAT listen_disabled_num 0
END

</code>

You can now quit out of the telnet connect and stop memcached as follows

<code lang="bash">
quit
launchctl unload /Library/LaunchDaemons/org.memcached.plist
</code>

### It could be better..

I like to alias long commands so I don't waste my precious time on the plant typing overly verbose commands.  I've added the following to my $HOME/.bash_login file

<code lang="bash">
alias memcached_start="launchctl load /Library/LaunchDaemons/org.memcached.plist"
alias memcached_stop="launchctl unload /Library/LaunchDaemons/org.memcached.plist"
</code>

Now I can start and stop memcached easily.

That is all, goodbye.




