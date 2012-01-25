title: "Chef, Fabric & Joy."
description: "I'm late the to the chef party, but it's a great party."
created: 2011-07-27 09:50:37
---

![Chef Logo](http://media.jamiecurle.com/uploads/2011/08/03/blogimage/OC_Chef_Logo.850x600.png)



At [c&c](http://designcc.co.uk) I seem(ed) to spend too much time either configuring hosting accounts or setting up servers - once the novelty wears off, it becomes a dull, boring and joyless task - not good.

We've used three hosting providers in the time we've been trading as c&c -

* Bytemark
* Webfaction
* Zerigo

The latter being the most used at this point in time because they have solid DNS service as well as a comprehensive suite of virtual machines and cloud based machines - they have been in many ways a fine host. Webfaction has served us equally well for the majority of client sites, but the problem is that with 30+ open accounts managing them all becomes a nightmare.  Depending on the project we tend decide early on if it's more of a virtual machine project or a shared hosting account.  Most of the recent projects have all been virtual machine projects and I grow weary of rebuilding servers from scratch - This is where my interest in tools such as [Chef](http://www.opscode.com/chef/), [Puppet](http://www.puppetlabs.com/) and [Fabric](http://fabfile.org) came back into play.

## Fabric

I have used Fabric before, but for some strange and unknown reason, I stopped using it.  Before I used fabric, part of my 'server setup' was to alias a few commands on the server's .bashrc file

<code lang="bash">
alias update="svn up ${HOME}/designcc/src/${USER}"
alias restart="${HOME}/webapps/app/apache2/bin/restart"
alias settings="vim ${HOME}/designcc/src/${USER}/settings.py"
</code>

This would quickly allow us to shell into a server and type update and be done with it.

<code lang="bash">
ssh username@projectname.webfactional.com
update
logout
</code>

This was fine, but fabric allows you to be much smarter with your time.

<code lang="bash">
fab deploy
</code>

For some reason the use of this in our projects fizzled out - a very foolish mistake, but I'm glad to say that it's back.

## Enter Chef

I lost a few days playing ( or rather, trying to get my head around the chef-server/ chef-node model) with chef-server before coming to conclusion that for my needs it was a bit overkill.  Within a just a few hours of playing around with chef-solo I had it taking a default plain vanilla ubuntu 10.10 server install from bare bones to fully configured as a django app server ready for projects.

[I've put the code up on github](https://github.com/jamiecurle/ubuntu-django-chef-solo-config) and you can check it out from there - It might run fine for you, but chances are you'll have to make some changes ( update iptables template with your IP and update the node.js file to contain the right information for your server.

Before I composed this cookbook it used to take me about 2-5 hours to configure a server for this use, now I have that down to 7 minutes and 30 seconds (ish) by simply using this one command

<code lang="bash">
fab install_environment
</code>

I can't begin to tell you how much joy that brings me.
