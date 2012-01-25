title: "The Django Sandwich Filling"
description: "A closer look at a typical setup, in a typical django project"
created: 2011-11-11 13:15:41
---

Following on from a post that I wrote about [Serving Django As a Nginx & Supervisord Sandwich With a Gunicorn Filling][0] I wanted to expand a little more on the contents of the filling - The Django Project.

Django isn't Rails (_GADZOOKS!_).  In the Django world configuration trumps convention. Pragmatically this has the effect that projects can vary from one to the other. The way that I'll explain in this post may not be the way that everyone does it. But it's how I do and it and it certainly plays very nice with the surrounding technologies and keeps everything nice and neat.  You can find the sample ['myproject'][2] project that I'll be referring to on [my github space][3].

Before we look at the individual files and folders in a typical django project however, I want to talk about the virtual environment because it is super important.

## The Virtual Environment

If you refer back to the [Serving Django As a Nginx & Supervisord Sandwich With a Gunicorn Filling][0] post and look at the diagram, you'll see that each django project lives in it's own little environment. This is made possible by [virtualenv][10] which is a super awesome utility for creating sandboxed python environments for each project.  Virtualenv itself is very easy to use, but it can be made super special by using [virtualenvwrapper][11] which just covers the whole experience in gold and silk. I've already blogged about installing [pip, virtualenv and virtualenvwrapper][12] before, so there is no need to mention it again.

The virtual environment is created so that each project has it's own sandboxed environment &ndash; but what exactly does that mean? Imagine you've got a server that you use to host client sites. The year is 2008 and Django 1.0 is released. You deploy a site for client X to your server and the site sits there, not doing much. Over time the client X doesn't want to pay to have upgrades performed so you only upgrade django to the 1.0.X releases.  Now fast forward to 2011. Client X's site is still there, but you've now got another client - Client A, whose website is built with Django 1.3  Now you've got a dilemma. You can't just upgrade the server to Django 1.3 because you can't be certain that client X's site will work. (_it probably will, but not without a few tweaks and pokes and Client X doesn't want to invest anymore in the project_). At the same time Client A's site won't run on Django 1.0 because you're using loads of features that weren't in the 1.0 release.

This is the world of pain that virtualenv does a supertastic job of preventing. By using virtualenv, the python environment for client X shares only a few system wide libraries with client A ( MySQLdb, memcached, PIL etc).

So when you look back at the diagram in the [Serving Django As a Nginx & Supervisord Sandwich With a Gunicorn Filling][0] and see each of the django project sandwich fillings, this is why they're all in a box. The box is the virtual environment - not their physical folders.

Now that we've cleared this up, I'll now break down, file by file and folder by folder what the parts of a typical django project look, smell and feel like.

## myproject - The Top Level Directory
![Top Level Directories](http://media.jamiecurle.com/uploads/2011/11/11/blogimage/toplevel.850x600.png)

This folder contains a number of items &mdash;

### .gitignore

The [.gitignore][4] file contains number of file & folder pattern matches that I don't want to be included in my repository. There are a number of arguments for not including this file on a per project basis and using a global .gitignore file on your machine, but for my needs I prefer to put it in with the project. Doing so makes sure that no one else on the project accidentally adds a 200mb database dump or their settings_local.py file.

### fabfile.py

The [fabfile.py][5] contains a load of super helpful [fabric][6] commands that I would use to perform operations such as deploying, updating development databases and anything else that project required.  If you haven't checked out fabric you should, it saves you hours of tedious repetitious command typing and automates everything to be a neat and well oiled machine.

By far my most common use for fab is to define a command called deploy which

1. Runs all the tests on a project. And if they all pass; 
2. Add any new files to the git repository,
3. Commit the changes and pushes to the master origin
4. Ssh's into the remote server, pulls down the changes
5. Runs any migrations
6. Restarts the supervisor process

In another post for another time I'll go into this in more depth. There is just too much awesome in fabric for sharing space in this post!

### myproject
 
[myproject][7] is the actual django code that you work on. I'll describe this in much more depth later on.

### nginx.conf

[nginx.conf][8] is the configuration that would be used on the production / staging server. Normally I symlink the config files so that any changes that are made to the file are picked up by the nginx process after I issue &mdash;

<code lang="bash">
sudo nginx -s reload
</code>

Because nginx runs on port 80 there is no way of getting around reloading it ( that I know of ) without the sudo.

### supervisor.ini

[supervisor.ini][9] holds the configuration for the production / staging server supervisor process. As with the nginx configuration I would normally symlink this so that any changes can be picked up by issuing the following command &mdash;

<code lang="bash">
supervisorctl reread myproject
</code>

### django-admin.py startproject

If you created your project using &mdash;

<code lang="python">
./django-admin.py startproject myproject
</code>

Don't worry if it doesn't look like what I've described above. You won't have the any of the above files, you'll just have the folder called myproject. It is looking likely however that from [Django 1.4 this may change][1] and adopt a layout similar to the above.

### requirements.txt

[Requirements.txt][5a] holds the names of all of the packages that your project requires to run. We use pip to install the various components from the file and it provides a nice neat way of ensuring that everything that the environment requires is available.

It's not perfect however. For instance if you deploy to Ubuntu there are a number of python packages that are better off installed by using apt-get. This is simply because of the way that Ubuntu (or your flavour of linux) has had their software packaged.  Normally I leave out things like MySQLdb, Python Imaging Library, lxml from my requirements file and defer to apt-get for system wide installation of these packages. You'll have to experiment with what works best for you, but typically you'd expect to see various third party django apps in this file and perhaps the odd python package.

Using pip to install the components is a breeze, but you must, must must remember to activate your virtualenv first.

<code lang="bash">
workon myproject
pip install -U -r /path/to/requirements.txt
</code>

## myproject

![The Actual Django Project Layout](http://media.jamiecurle.com/uploads/2011/11/11/blogimage/myproject.myproject.850x600.png)

This is the motherload and where all of your hard work lives. For the sake of this blog post the myproject django project has only one application, a blog app.  But let's go over the contents one by by one.

###   &#095;&#095;init&#095;&#095;.py 

As I understand it people take issue with python for two main reasons. These files and the seemingly harsh rules on indentation ( which really get out of your way quickly once you learn their ways).  Python needs a directory to contain these files so that it knows that it is to treat the directory as a module and to be able to access the python files inside it.  For the sake of clarity however, I'll not mention the &#095;&#095;init&#095;&#095;.py  files again in this post, with one exception: the tests directory.

###  apps

This directory will contain all of the applications that you author and not third party repluggable applications (_they belong in the requirements.txt file for installation with pip_). I'll dissect the an example of an app later on.

###  static

This holds all of the static media for your site and typically you'd expect a to see a number of directories inside it such as css, js, img and others. As of Django 1.3 the static media from other applications will be deposited into the directory if you're using the [django.contrib.staticfiles][13] app. I do have to say however, that I'm still getting to know this beast so I may not be the best person to ask about it. 

###  templates

This directory contains all of the templates for your project. There's no hard rules about what you call your templates but it's a good idea to go with the grain and start with base.html and work your way up from there.

### You don't have to follow these names

The three directories I've mentioned above don't have to be called what I've named them. I could just have easily called them homer, susan and doubledash. However that wouldn't have made any sense to anyone reading the code and working on the project. This may be configuration over convention, but that doesn't mean we have to create more work for ourselves!

###  manage.py

This is standard issue file for a django project and it is invoked to do a number of tasks. Not least of which is the runserver command. In the four years that I've been using Django I've looked at this file for probably a minute at most. It stays out of my way and I stay out of its way. We have a great relationship.

### settings.py & settings_local.py

Love it or loathe it this is where the settings for your project are stored. The biggest challenge with this file is how to store the information that you need to, but without exposing usernames or password, or having everyone on the project overwrite each others settings. It can get messy, but there is a relatively easy way of doing this.

Typically in settings.py you configure everything that you need to get your project run. You'd define your [INSTALLED_APPS][27] and perhaps you've got some custom [MIDDLEWARE_CLASSES][28] or maybe you've got some custom [AUTHENTICATION_BACKENDS][29] or [TEMPLATE_CONTEXT_PROCESSORS][30]. Things like this that are going to be the same no matter what machine the project is on would go in your settings.py file.

What you almost certainly don't want to do is put usernames or passwords into this file for two main reasons.

1. They'll likely end up in version control - not great if your source code is available to the world.
2. Someone is going to change the details - this will impact your installation when you update your code.

To get around this I use an idea that wasn't mine, but is a fairly typical solution. I always have a file called settings_local.py. This file is excluded from version control so that we never commit in usernames, passwords, API keys or anything else that would cause pain. If you have a look at [settings.py][14] and scroll to the bottom you'll notice that it attempts to import * from settings_local. If it fails it raises an ImportError which is ignored and we move along without creating a scene.  So far I've been using this approach for just over a year and it's a charm.

This is the python way because [it is easier to ask for forgiveness than permission][15].

## urls.py

This is the root urlconf file. There's really not much more to say other than it'll likely just define a match for a homepage and then go onto include the other urlconf files from your apps. What I can say about the urls in Django is that they're a real pleasure to work with. Not only will they have you practising your regular expression skills ( _always a good thing_) but they're also a joy to work with.

If you're including other url patterns then it would be great idea to [use a namespace][25] to prevent named urls from clashing as your application grows. 

## Blog - A Sample App

![The Blog App](http://media.jamiecurle.com/uploads/2011/11/11/blogimage/blogapp_1.850x600.png)

I've really went to town on everything that I could think of in this app with the exception of migrations for [south][16] and search_indexes for [haystack][17].  This is an app on steroids and in most cases you won't normally have as many files as this in an app.  Here's what they all do

### admin.py

Admin.py defines the admin classes that are using in the double cool, if not slightly visually dated, django admin application.  The django admin is a very neat feat of engineering and one of the reasons I decided to really get into Django.

### forms.py

The admin is nice and for most situations it's OK to give to a client and use as a CMS but there is no escaping that as designer and developers we have to work with form data. Django has a very nice way of dealing with input django through it's forms.Forms code. It allows you to very quickly get up and running with forms that are based on the models that you define in models.py

### listeners.py

One of the not so talked about features of Django is the signals system that it has baked right into it. Signals allow you to attach listeners (they're just functions) to specific events such as when a blog post gets saved. For instance you might want to automatically send a tweet when you post a new blog post.  Without signals you'd have to find the code that processes the blog post and manually add the tweet code.  This gets very messy, very quickly; signals allow you to do away with this nonsense.

So the listeners.py file would contain listeners that you've defined. Huzzah.

#### _Edit 4th Jan 2012_

_After working closely with signals for the past month, I've came to realise that listeners.py should be called receivers.py. This is because the functions defined are technically receivers - not listeners_.

### management folder

Django makes it very easy to write custom commands that you can call using manage.py. From time to time this can be very useful if you have to run a periodic cron job or do something specific that you don't want tied to HTTP requests - sending email,  updating search indexes or running migrations. 

In the example I've created there is a file called do_something.py. As long as you do a few things correctly ( _e.g. have a file that contained a class called command, that extended BaseCommand and that the class exposed a method called handle()_) then you'd be able to do this

<code class="bash">
./manage.py do_something
</code>

Neato.

### models.py

This is the cornerstone of each app. This is the file that you define the data models in. 

The upside of doing this is that you don't have to write any SQL. For the most part the [Django ORM][18] will do a great job of abstracting the sql layer away from you and for 95% of use cases this is fine.  However this strength is also a weakness, because you do start to forget about the efficiency your queries and sometimes, it's just better to write raw sql. Recently an unchecked bit of functionality on a clients site was executing [just under 18,000 queries on a page][19] and taking over 30 seconds to run. Writing it as one carefully crafted piece of raw sql got it down to one query and 8 milliseconds.

Aside from that [Django models][20] are great and there is a lot of win to be had for little input.

### templatetags

This is the folder that you would put your [custom templatetags, filters and inclusiontags][21]. I'm going to go out on a limb here and state that I find custom template tags a messy (_but manageable_) affair compared to filters and inclusion tags. For most situations I'll try to use only filters and inclusion tags but sometimes there is no avoiding this.

Template tags are great ways of exposing bits of functionality that don't quite belong inside views. For instance you might have a side bar with the latest news items in it. This sidebar is display on numerous pages throughout the site and it makes no sense to clutter up each view with boilerplate. This is where you'd use a templatetag or an inclusion tag. Another use case that I use a lot is for archive navigation. In fact [I use it to generate the navigation on this page][22]

Filters are a much easier experience and their a really neat way of checking or returning certain values from passed 'things'. The only downside with filters is that they cannot have more than one argument.

Whatever you do with template tags however you must remember to write your &hellip;

### tests

Repeat after me

> Tests are important.
<br>
<br>
Tests are important.
<br>
<br>
Tests are important.

I never used to write tests and my code always used to break. As your application grows, the points of failure increase. I used to think that tested meant that myself or another person had prodded random bits of functionality with a mouse and decreed the application to be tested. I was a fool.

Now I write tests ( though admittedly not for this blog, but for all of my client work I do ). The upshot is that things still break, but fixing them is much easier and about 99% of the time we get to fix the bugs before they hit the production environment. 

Writing tests shouldn't be an afterthought either. Writing tests should be the first thing you do. I'm a big fan of using the django TestClient and writing the tests in more of a functional manner as opposed to unit tests. Recently I've also really warmed to the [Lettuce][23] style of writing tests for [behavior driven development][24] (BDD). I find that you don't have to use frameworks like lettuce to write BDD style tests. It's more of an approach than a technology and with that in mind, I still advocate the use of the Django test client - it just makes sense. I already know how to use it and it gets the job done.

A little earlier on I mentioned that I would omit the &#095;&#095;init&#095;&#095;.py files for each directory with the exception of the test directory. The reason is that by default the django test runner will only look for tests in the tests module. Given that we're using a directory called tests it technically doesn't contain any tests until we tell &#095;&#095;init&#095;&#095;.py to import them.  So in the &#095;&#095;init&#095;&#095;.py  in the tests folder you'll have to include each set of tests. In our example it would look like this

<code lang="python">
from test_all_views_respond_correctly import *
</code>

Now when you run the tests the runner will be able to find the tests and run them. Dapper.

p.s. Tests are important.

### urls.py

For each application you should have a urls.py and in this file you'll specify the views (_typically just plain functions_) that certain url patterns will trigger. This is one of the really nice features of django. You have total control over the urls.

I mentioned in the root url conf that if you're including other url files then you should [use namespaces][25] to prevent clashes as your application grows. As well as that you should also [name each of your url patterns][26]. If you use namespaces and named urls then it keeps your templates really clean because you can do stuff like this

<code class="html">
{% url blog:index %}
</code>

Once you've got a decent amount of applications in your project you'll thank yourself for starting off on the right foot.

### views.py

Guess what goes in here? That's right, your views.  

Views are nothing more than simple functions that take at least one argument ( request ) and must return an HttpReponse. They are the place that you should perform specific business logic such as processing forms, building spreadsheets or other.


## Conclusion

I hope this has been of some help to you. Most of the time you won't need all of these files in an application and you may even choose to structure your project differently than I have - that's cool.

If you have any ideas on how I can improve my approach or this post let me know in the comments.


[0]: http://jamiecurle.com/posts/serving-django-as-nginx-and-supervisord-sandwich-with-a-gunicorn-filling/
[1]: http://groups.google.com/group/django-developers/browse_thread/thread/44b70a37ff73298b
[2]: https://github.com/jamiecurle/myproject
[3]: https://github.com/jamiecurle/
[4]: https://github.com/jamiecurle/myproject/blob/master/.gitignore
[5]: https://github.com/jamiecurle/myproject/blob/master/fabfile.py
[5a]: https://github.com/jamiecurle/myproject/blob/master/requirements.txt
[6]: http://fabfile.org
[7]: https://github.com/jamiecurle/myproject/tree/master/myproject
[8]: https://github.com/jamiecurle/myproject/tree/master/nginx.conf
[9]: https://github.com/jamiecurle/myproject/tree/master/supervisor.ini
[10]: http://pypi.python.org/pypi/virtualenv
[11]: http://www.doughellmann.com/projects/virtualenvwrapper/
[12]: http://jamiecurle.com/posts/installing-pip-virtualenv-and-virtualenvwrapper-on-os-x/
[13]: https://docs.djangoproject.com/en/dev/howto/static-files/
[14]: https://github.com/jamiecurle/myproject/blob/master/fabfile.py
[15]: http://stackoverflow.com/questions/6092992/why-is-it-easier-to-ask-forgiveness-than-permission-in-python-but-not-in-java
[16]: http://south.aeracode.org/
[17]: http://haystacksearch.org/
[18]: https://docs.djangoproject.com/en/dev/topics/db/queries/
[19]: https://twitter.com/#!/jamiecurle/status/129599762688249856
[20]: https://docs.djangoproject.com/en/dev/topics/db/models/
[21]: https://docs.djangoproject.com/en/dev/howto/custom-template-tags/
[22]: https://github.com/jamiecurle/jamiecurle/blob/master/apps/blog/templatetags/blog_tags.py
[23]: http://lettuce.it
[24]: http://en.wikipedia.org/wiki/Behavior_Driven_Development
[25]: https://docs.djangoproject.com/en/dev/topics/http/urls/#url-namespaces
[26]: https://docs.djangoproject.com/en/dev/topics/http/urls/#naming-url-patterns
[27]: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
[28]: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
[29]: https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
[30]: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors




