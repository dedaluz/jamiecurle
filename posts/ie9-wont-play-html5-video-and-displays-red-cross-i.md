title: "IE9 Won't play HTML5 video  and displays a red cross instead"
description: "Damn you IE ( and VMWARE ) "
created: 2011-07-18 07:54:26
---

I thought the days of IE madness were over with IE9 but alas not.  Recently I've been working on a small project that is driven by video - html5 video to be precise.  Here's the code I was using ( this is part of a Django template if you were wondering )

<code lang="html">
 <video controls id="htmlvideo">
  <source src="{{video.h264}}" type='video/mp4; codecs="avc1.42E01E,mp4a.40.2"'>
  <source src="{{video.ogg}}"  type='video/ogg; codecs="theora, vorbis"'>
  <source src="{{video.webm}}"  type='video/webm; codecs="vp8, vorbis"'>
  <object id="flashvideo" width="600" height="400" data="http://releases.flowplayer.org/swf/flowplayer-3.2.7.swf" type="application/x-shockwave-flash">
    <param name="movie" value="http://releases.flowplayer.org/swf/flowplayer-3.2.7.swf" >
    <param name="allowfullscreen" value="true" />
    <param name="allowscriptaccess" value="always" />
    <param name="flashvars" value='config={"clip":{"url":"{{video.h264}}"}}'>
  </object>
</video>
</code>

I spent the best part of a Sunday afternoon and early Monday morning checking mime types, encoding to webm, investigating cross domain issues and generally cursing IE.

The above rendered fine in Safari, Opera, Firefox, Chrome and even IE7 and 8 got the flash fallback without a problem - but not IE9, that had a special treat install for me.



![IE9 red cross](http://media.jamiecurle.com/uploads/2011/07/18/blogimage/ie9before.850x600.jpg)


Do you see the madness - what is that red cross? My mime types are correct, the video plays in windows media player, but apparently not IE - curses.
After reinstalling a fresh copy of windows, contemplating dishing out $19.99 to browsercam and partitioning my trusty old school macbook pro for bootcamp I came accross this little gem - 
[IE9 HTML5 Video Doesn’t Work… in VMWare](http://clubajax.org/ie9-html5-video-doesnt-work-in-vmware/).

Apparently the issue is this

>Running Internet Explorer 9 in a VMware virtual machine
Internet Explorer 9 always uses software rendering in a VMWare virtual machine. This is due to a code bug in Internet Explorer introduced by recent changes in the rendering engine. The Internet Explorer team will be addressing this in a future update.


## Ok, so how do I fix it.

That's simple, but not that obvious. First you have to power off ( not suspend ) your virtual machine and then disable 3D acceleration.  When you've done this open up the vmware settings for your virtual machine and click on display.  You want to disable ( uncheck ) the acceleration of 3D graphics.


![Uncheck Accelerate 3D graphics](http://media.jamiecurle.com/uploads/2011/07/18/blogimage/checkbox.850x600.jpg)


When you've done that restart your virtual machine and you should be met with working video.

That's another 8 hours of my life lost to this IE.  I want to love IE, but it's like it goes out of it's way to be joy slayer.