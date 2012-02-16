title: "Getting VLC to play dvdmedia files in OSX"
description: "Getting VLC to play dvdmedia files in OSX"
created: 2010-10-23 00:00:00
---

![VLC](/media/2010/10/23/blogimage/VLC.850x600.jpg)

Credit has to go to a user called 'raindancing' from [this thread in the videoLAN forums](http://forum.videolan.org/viewtopic.php?f=7&t=62834) for the plist correction and [Jason Clarke"](http://www.tuaw.com/bloggers/jason-clarke/ ) from the [terminal tips post on TUAW](http://www.tuaw.com/2009/06/11/terminal-tips-rebuild-your-launch-services-database-to-clean-up). 

## Edit VLC's Info.plist file

Open a finder window in /Applications.  Now right click on VLC and choose 'show package contents. Now open Info.plist in your favourite text editor.  

Now find the lines that look like this - should be around lines 7-8


<code lang="xml">
<key>CFBundleDocumentTypes</key>
<array>
</code>


Right below it add the following


<code lang="xml">
        <dict>
         <key>CFBundleTypeExtensions</key>
         <array>
            <string>dvdmedia</string>
         </array>
         <key>CFBundleTypeIconFile</key>
         <string>generic.icns</string>
         <key>LSHandlerRank</key>
         <string>Default</string>
         <key>CFBundleTypeMIMETypes</key>
         <array>
            <string></string>
         </array>
         <key>CFBundleTypeName</key>
         <string>DVD Bundle</string>
         <key>CFBundleTypeRole</key>
         <string>Editor</string>
         <key>LSTypeIsPackage</key>
         <true/>
      </dict>
</code>



## Rebuild Launch Services

Now you just need to rebuild the launch services database. Fire up a terminal and issue the following command.


<code lang="bash">
/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister -kill -r -domain local -domain system -domain user
</code>


It'll take a little while, but once it's done you'll be able to right click the dvdmedia files, choose 'open with' then locate VLC and you'll be able to select it.

Now you can watch the movies that you purchased, without being told that you're not permitted to skip silly things like the anti-piracy advert.

Which is silly, because if you think about, I'm not the one that needs to see that advert.  I'd rather see [this one](http://www.youtube.com/watch?v=8wRxfz_6E7o&NR=1)