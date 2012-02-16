title: "OSX Lion iChat Lost The Connection / Disconnected unexpectedly"
description: "iChat on lion doesn't connect to your instant messaging account. "
created: 2011-10-07 11:12:13
---

Lion was the first apple OS that I didn't install as soon as I could get my hands on it. Snow leopard bit me hard and I was left with a machine that kept on crashing when I needed to do work. I vowed never to let that happen again.

Since installed Lion after the first update (10.7.1 ) everything has been tickety-boo, with one exception – iChat.

For some reason iChat simply refuses to connect to accounts. This is annoying because it's how I communicate with the mothership when I'm working from home. Many a time I've thought I was signed in and my colleagues were late, when the reality was that they where thinking the same of me.

There are two methods you can use to get iChat working again.

## Method One 

To cut a long story short type this command into the terminal ( Applications > Utilities > Terminal ) and you'll be able to connect your iChat to your instant messaging service of choice.

<code class="bash">
killall imagent
</code>

## Method Two

As Joe Clark pointed out in the comments you can also open up the Activity Monitor application (Applications > Utilities > Activity Monitor), do search for "imagent" and quit the process. 

![Activity Monitor](/media/2011/10/24/blogimage/m2.850x600.png)


Good times.