title: "Serving Django as a Nginx & Supervisord Sandwich with a Gunicorn Filling."
description: "I've toyed with a few ways of serving Django applications, but finally I've got one that I think is super tasty and nice and lean."
created: 2011-11-10 11:39:31
---

When serving Django it's easy to feel like there are too many technologies involved. At first it's hard to know which parts do what. In an attempt to straighten out some confusion for you this post outlines how I do it. 

At the heart of this setup there are three technologies and they're organised like a sandwich.

![Django App Sandwich](http://media.jamiecurle.com/uploads/2011/11/10/blogimage/django.sandwich.png)

### Nginx

Like Apache and Lighttpd, [Nginx][2] is a web server.

In the diagram above nginx is the web public facing web server that responds to HTTP requests from the outside world. In this setup nginx has two jobs.

1. To serve HTTP requests for the static media for a project's static media (normally on a domain such as http(s)://media.myproject.com)

2. To act as a proxy for HTTP requests for the application and to return the HTTP response.

Nginx is the top slice of bread.

### The Django Project
 
The django project is mixture of source code, a virtual environment, configuration files and static media. I'll go into more depth about this in a blog post at some point in the future. 

The django projects are run using [green unicorn][4] (gunicorn). It is a Python WSGI HTTP Server for UNIX. When you're working on your projects on your local development machine, you'll this command to serve the project&mdash;

<code lang="python">
/path/to/python /path/to/project/manage.py runserver
</code>

However [you're strongly warned against using the development server for production work][5]. So we're using gunicorn to serve the project; the command to do so looks very familiar &mdash;

<code lang="python">
/path/to/python /path/to/project/manage.py run_gunicorn -b 127.0.0.1:8001
</code>


Think of the django project as the sandwich filling between the two slices of bread.

### Supervisor

[Supervisor][3] is a process control system. Essentially is made up of two programs.

1. Supervisord is the daemon. It can run any process you want, but in this setup we're using it to run separate gunicorn processes for each django project.
2. Supervisorctl is control program and monitor. This is used to start, stop, reload, show the status of the processes and perform other useful operations.

What's really nice about using supervisor for handling gunicorn in this way is that you can start and stop individual projects. If client X needs to be restarted then client Y won't get any 502 proxy errors. 

Think of supervisor as the bottom slice of bread.

## More To Follow

I'll expand on these ideas with some actual examples including a really nice configuration for avoiding the dreaded 502 proxy error that can be encountered when starting and stoping gunicorn processes, but for now you might like to read more about [the django filling][6].


[1]: http://designcc.co.uk/
[2]: http://nginx.org/
[3]: http://supervisord.org/
[4]: http://gunicorn.org/
[5]: https://docs.djangoproject.com/en/dev/ref/django-admin/#runserver-port-or-address-port
[6]: http://jamiecurle.com/posts/the-django-sandwich-filling/


