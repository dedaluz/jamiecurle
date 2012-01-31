title: "Responsive (again) "
description: "I couldn't stand the old version of the site."
created: 2011-10-03 08:49:12
---

I couldn't stand the old version of the site, so I made a new responsive one that is based on some of the things I've been inspired by and other things that I'm becoming more and more interested in.


## Responsive

The last iteration of the site was not responsive in any form. It should have been. The [rails version that I put live in January was][0] was, but it was my first crack at a responsive design and it was messy and I've learned a few things about it since then. 


## What's up with the coloured borders?

The colours relate to the average temperate and sunlight hours in [my part of the world][1]. The colours are calculated from a [dataset][2] that contains temperature information from the past one hundred years.

The colours are expressed as HSLa where a zero value for Hue represents the temperature and the saturation represents the sunlight hours. 

The idea to do this came from Brian Suda's 2011 DIBI presentation on [Visualizing Data][3]. He put forward that data should tell a story and have a narrative.  On this site it's not the main plot, but an interesting sub plot.

## Project &ldquo;Reclaim My Data&rdquo;

I'm going to blog about this more as the project evolves, but it's about reclaiming the data that I've been frivolusly giving to various tech companies in exchange for solving various problems for me.  

With this version of the site, I'm now sucking down [my tweets][6] from Twitter, [my bookmarks][7] from Pinboard, [my scrobbles ][8] from last.fm and my instagrams from Instagram. Right now I'm not doing anything with this data, but I'm very much looking forward to.

Finally I'm collecting my own stats and I've parted ways with Google Analytics. I'm now using [a little bit of Django middleware] that I wrote to logs (most) request objects so I can interrogate them later.

## Reflection and Learning.

As part of my MA the first semester had me design and develop a reflection model that I used to develop my professional practice. To aid this I designed and developed an [entire separate application][4] that I used dutifully for  a number of months, based on [this reflection model][5].  

On reflection however, this model was incredibly contrived and didn't fit in with my practice properly. My new plan is to use this blog for reflective practice. I want to align it with the data that I've been reclaiming above and provide a cowpath for a reflection model based on my current habits.

## Still Todo

Lots and lots so keep your eyes peeled.


[0]: http://jamiecurle.com/blog/the-switch-has-been-made/
[1]: http://maps.google.co.uk/maps?q=blyth+northumberland+england&ll=55.116085,-1.516113&spn=13.149213,24.147949&oe=utf-8&hnear=Blyth,+United+Kingdom&gl=uk&t=m&z=6&vpsrc=6
[2]: http://www.metoffice.gov.uk/climate/uk/stationdata/durhamdata.txt
[3]: http://lanyrd.com/2011/dibi/sfrmb/
[4]: http://reflection.jamiecurle.com
[5]: http://d.pr/Oq1Q
[6]: http://twitter.com/jamiecurle
[7]: http://pinboard.in/u:jamiecurle
[8]: http://www.last.fm/user/jamiecURLe
[9]: https://github.com/jamiecurle/jamiecurle/tree/master/apps/stats