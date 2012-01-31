title: "HTML Syntax highlighting in InDesign"
description: "Using GREP styles inside of paragraph rules can go a long way towards syntax highlighing html"
created: 2010-10-10 08:39:41
---

![Indesign](http://media.jamiecurle.com/uploads/2010/10/10/blogimage/Indesign.850x600.jpg)

Whilst preparing some lessons I found myself doing something very silly – trying to do syntax highlighting by hand. Rather than taking myself out back and giving myself a good kicking I spent the time getting to fiddle with the GREP style feature of inDesign's paragraph styles.

##  Using GREP Style

![Grep Style](http://media.jamiecurle.com/uploads/2010/10/10/blogimage/Grep_Style.850x600.jpg)

From within the paragraph style that you want to use, choose GREP style from the options on the left hand side.  When you do that you'll be greeted with the following UI

![Greps](http://media.jamiecurle.com/uploads/2010/10/10/blogimage/Greps.850x600.jpg)

From here it's just a case adding some regular expressions to match the syntax and apply your selected character style to those matches.

I've used three regular expressions. The first matches tags with attributes, the second plain tags and the third matches comments.

This matches tags with attributes


<code lang="regex">
<!?/?\w+\s+[^>]*>
</code>


This one matches plain tags


<code lang="regex">
<(\/*)\w+>
</code>


This one matches comments


<code lang="regex">
<!-- .+ -->
</code>


Below you can see the styles in action, the tags are now automatically using the html syntax character style that I set up.

![Grep Styles in action](http://media.jamiecurle.com/uploads/2010/10/10/blogimage/Grep_Styles_in_action.850x600.jpg)

Whilst regular expressions aren't a mystery to me, neither are they my most familiar subject, however the ones above seem to get the job done. If you have a better way of doing them, please feel free to post a comment.


