title: "Typekit: a few ideas."
description: "I love type kit, but there are a few things I would do to improve the experience of setting up and playing with kits."
created: 2012-02-19 16:00:00
tags:
  - design
  - typekit
---


## Default domains

Having to register domain for a kit is a pain and often involves a wait that, although short, does slow down momentum when working. When I'm working locally in development I often have to enter the same domains over and over again. 

It would be great if we could specify a list of domains that are able to access all kits, by default, all of the time.

## Ask for forgiveness, not permission.

Having a list of domains that are able to access a kit makes sense. You don't want paying customer X having non-paying scumbag Y being able to use their kit. But the current system assumes that you can't access a kit, until you prove you can.

What if this was flipped on its head? Typekit would assume you had permission to access the kit by default (yay, no more 403 errors) and then monitored abuse and blacklisted domains based on usage patterns. If you found a valid domain was blacklisted, then you could easy whitelist it easily by registering it against a kit.

When working with digital tools, it's faster (and better imho) to ask ["forgiveness rather than for permission"][0]. 


## If domains must stay, then adapt a better UI.

The current UI for adding domains is not great. Once you've entered more than one domain then you quickly have to click into the input box and key through the values to see what domains are registered. Here's an example &hellip;

![The Current Typekit UI for adding domains](/static/blog/2012/02/19/typekit/ui1.png)

In the crude mockup below the domains are listed below each other making it much easier to see what domains are registered to a kit &hellip; 

![An example of a better UI for adding domains](/static/blog/2012/02/19/typekit/ui2.png)

## Publish Faster

I'm probably getting into fantasy world here, but it would be terrific if kits published a *lot* faster. I suspect the delay is likely caused by having to publish onto a CDN and/or cache invalidation, but it would make experimenting with different faces more joyful. Ideally I'd want to be able to hit the publish button, dump my browser cache and immediately be able to reload the new kit.

![One does not simply](/static/blog/2012/02/19/typekit/one-does-not-simply.png)

Or can you &hellip;



[0]: http://en.wikipedia.org/wiki/Grace_Hopper#Anecdotes