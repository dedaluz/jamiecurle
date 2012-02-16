title: "Bottle & Supervisord"
description: "Deploying bottle using supervisor is surprisingly painless."
created: 2010-10-06 08:02:09
---

![Bottle](/media/2010/10/06/blogimage/Bottle.850x600.jpg)

I made a [url shortner using bottle](http://github.com/jamiecurle/bottle-shorturl/ "url shortner using bottle") for my own personal amusement and I wanted to put it into use. I'm not expecting a lot of traffic to it so I've opted to use the server that ships with bottle. I may change that to use [Gunicorn](http://gunicorn.org/ "gunicorn") at some point though.

##  Supervisor Conf

Add the following to your /etc/supervisord.conf file. I've changed the paths because yours will be different.


<code lang="ini">
[program:yourappname]
command=/path/to/python /path/to/bottleapp/yourapp.py
directory=/path/to/bottleapp/
user=yourusername
autostart=true
autorestart=true
redirect_stderr=true

</code>


The first path in the command value refer to your python path or your virtualenv python path.  Once that's done you just have to start & stop supervisord.


<code lang="bash">
$ killall supervisord
$ supervisord 
</code>


A quick look into the supervisorctl program should show that the new service is running


<code lang="bash">
$ supervisorctl
jamiecurle                       RUNNING    pid 12374, uptime 0:07:16
jmcrl                            RUNNING    pid 12375, uptime 0:07:16
supervisor> 

</code>


Splendid,  now quit out of supervisorctl and we're ready to set up nginx

##  Nginx

For those that haven't heard of [Nginx]( http://nginx.or/g "Nginx") ( _pronouced en-jin-ex_ ), it's a web server that is very fast and much leaner than [Apache](http://www.apache.org/ "Apache")

You could use any webserver for this step, as all we're going to be doing is proxying requests from port 80 to our application port, which defaults to 8080 for bottle.

If you're using Debian or Debian variant such as Ubuntu and you've installed Nginx using apt, then you'll have a funky config file layout like apache.  All we're going to do is add a config file for a virtualhost. Because I'm using Ubuntu, I'm going to make that file in /etc/nginx/sites-available. You'll probably have to sudo this because you might not shouldn't have permission to write into the /etc/ directory.  You should call your file something nice and semantic such as 'mydomain.com'


<code lang="bash">
$ sudo touch /etc/nginx/sites-available/mydomain.com
</code>


Now it's just a case of supplying the correct config information for our virtual host and restarting Nginx.


<code lang="conf">
server{
	server_name mydomain.com;
	root /path/to/root/;
	location / {
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header Host $http_host;
		proxy_redirect off;
		proxy_pass http://127.0.0.1:8080;
		break;
      }
}

</code>


The above code is telling nginx x that for all requests for jmcrl.com to forward them to http://127.0.0.1:8080- which is where we've configured supervisord to run our bottle app.

##  Debian / Unbuntu Jiggery Pokery

As I mentioned above on Debian & Debian variants the layout for nginx config is like that of Apache, with one difference - there's no command (a2ensite) for enabling and deactivating your available sites.  

Fear not, all the command done (or appeared to do that I noticed) was create or remove symlinks between sites-available and site-enabled. So if your using Debian or a Debian variant then you'll have to do the following step to get Nginx to pick up your config file.


<code lang="bash">
$ sudo ln -s /etc/nginx/sites-available/mydomain.com /etc/nginx/sites-enabled/mydomain.com
</code>


##  Restart Nginx

Almost done now, we just need to restart Nginx.


<code lang="bash">
$ sudo ln -s /etc/nginx/sites-available/mydomain.com /etc/nginx/sites-enabled/mydomain.com
</code>


Once this is done, visit your url and behold. Or in my case, be redirected as this is the default behavior for [bottle-shorturl](http://github.com/jamiecurle/bottle-shorturl/ "url shortner using bottle") when no id is supplied.

##  Bottle Logo

I wanted a nice Bottle logo for this post and I couldn't find a decent hi-res one, so I remade the logo in Illustrator. You can download the [bottle vector logo](http://jcurle.s3.amazonaws.com/media/bottle.logo.ai  "Bottle Vector Logo") for use in your Bottle projects.
