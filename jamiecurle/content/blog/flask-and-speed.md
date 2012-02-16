title: "Flask & Speed."
description: "Site now running on Flask and it's faster than ever."
created: 2012-01-26 08:59:59
tags:
  - development
  - design
  - flask
---

This site is now running on Flask and hosted with [webfaction][0] on one of their Amsterdam machines. This is departure from the previous version which was running on Django and hosted on a [Zerigo VPS][1].


## Why Change?

I was really geared up to make this site a static site. I wanted to get away from having a stack dynamically processing content that hardly ever changed. I wanted to have a fast site. I wanted to be able to write in writing application, not a textarea.

A statically generated site seemed like the right choices. I tried [Hyde][1], [Jeckyl][2] and [Nanoc][3]; none hit the sweet spot. Hyde (python) is still in development, so the docs where a little thin, so eventually I gave up on it. Jeckyl and Nanoc (both ruby) are both fine pieces of software, but they just didn't do it for me. 

## Enter Flask

I thought about it, I was really after speed. Static was just the means of getting there. I came to the conclusion that I didn't care about how I got speed, as long as I got it. So I set about building a flask application that didn't use a database - it just reads markdown files.  That application is what you see before you and it's cached up to the hilt using memcache.




[0]: http://webfaction.com
[1]: https://www.zerigo.com/vps-servers
[2]: http://ringce.com/hyde
[3]: https://github.com/mojombo/jekyll
[4]: http://nanoc.stoneship.org/


