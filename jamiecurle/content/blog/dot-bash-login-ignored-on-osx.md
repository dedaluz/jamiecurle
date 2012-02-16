title: ".bash_login ignored on OSX"
description: "I spent half an hour wondering why .bash_login wasn't being loaded into my bash shells."
created: 2010-10-06 00:00:00
---

![Trouble Shooting](/media/2010/10/06/blogimage/Trouble_Shooting.850x600.jpg)

I opened up a terminal for my days work and I dutifully went to type


<code lang="bash">
$ workon tass
</code>


and I was met with a 


<code lang="bash">
$ -bash: workon: command not found
</code>


Odd - I'd been using this command without incident for months.  Time to implement my [bulletproof troubleshooting skills](/blog/4-Bulletproof-Troubleshooting)

## Solution

The night before I was experimenting with restructured text and as part of those cahoots, I'd created a .bash_profile file which was being loaded into my bash shell instead of my usual .bash_login file.

Simply put contents of .bash_profile into .bash_login and then delete .bash_profile.

et viola and everything works

<code lang="bash">
$ workon 
TextMate    bottle      core2       flask       jmcrl       pgce        tass        ultrahtml   
bluesky     core        fitfit      jamiecurle  mongokit    sproutcore  ultragrow   web2py 
</code>


Fin & back to work.