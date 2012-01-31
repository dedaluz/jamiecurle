title: "Model fields as a template in Django"
description: "I've found myself constantly wishing that I could use a model field as a template. Turns out it's really easy."
created: 2010-10-23 12:00:00
---

Ok, let's assume apps/blog/models.py

<code lang="python">
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField()
    
    class Meta:
        ordering=['-created']
    
    def __unicode__(self):
        return u'%s' % self.title

</code>

and templates/blog/object_detail.html

<code lang="django">
{% extends 'base.html' %}

{% block title %}{{object.title}} &ndash; {% endblock %}

{% block article %}
	{{object.content|linebreaks}}
{% endblock %}
</code>

So far this is all pretty standard.  Let's add a BlogImage model into the mix


<code lang="python">
class BlogImage(models.Model):
    blogpost = models.ForeignKey(BlogPost)
    src = models.ImageField(upload_to="uploads/blogimages/")
    
    def __unicode__(self):
        return u'%s' % self.src
</code>

So now you're writing your blog post and you decide that you want to have your image at a certain point in the content that you're writing.  If you're using the contrib admin app, you might think about doing something like this

<code lang="html">
Last year we took a holiday to the south of France. The weather was brilliant.

<img src="{{object.blogimage_set.all.0.src.url}}">

As you can see from the picture above, we all had a great time.
</code>

But that's not going to work for two reasons:

1. The blogpost.content field isn't a template. It will always be treated as text, because it's a textfield
2. There context isn't supplied to a models field, so it has no idea what to resolve "object" to

## My Solution

Solving this problem is actually remarkably easy.

The model isn't aware of the context in the way that a template is, so we need to render out the model field as if it was a template. To do this, we'll write a templatetag and put this code in 'myproject/apps/blog/templatetags/blog_tags.py'. I've called this tag UltraRender, feel free to name it something a little more semantic.

<code lang="python">
from django import template
register = template.Library()

class UltraRender(template.Node):

    def __init__(self, obj_and_field):
        self.obj = template.Variable(obj_and_field.split('.')[0])
        self.t = obj_and_field.split('.')[1]

    def render(self, context):
        obj = self.obj.resolve(context)
        t = template.Template(getattr(obj, self.t))
        rendered_field = t.render(context)
        return template.defaultfilters.linebreaks(rendered_field)
        
        
@register.tag
def ultrarender(parser, token):
    bits = token.contents.split()
    return UltraRender(bits[1])
</code>

The tag is used like this

<code lang="django">
{% extends 'base.html' %}
{% load blog_tags %}

{% block title %}{{object.title}} &ndash; {% endblock %}

{% block article %}
	{% ultrarender object.content %}
{% endblock %}
</code>

and it should result in something like this

![Screenshot](http://media.jamiecurle.com/uploads/2010/10/23/blogimage/Screenshot.850x600.jpg)

## Conclusion

It's a nice little twist on the template engine that so far has been working out very well for me. I've been using it on this site for a while now, though I've modified it quite a lot to take advantage of caching, syntax highlighting and all manner of other embellishments.  If you're interesting in seeing how I've pushed it around, take a look at the [source code of assets.py](http://github.com/jamiecurle/jamiecurle/blob/master/apps/assets/templatetags/assets.py)

If you'd like it, you can [download the sample code](http://github.com/jamiecurle/ultrarenderdemo/zipball/master) that I used when writing this blog post. It can be found on my  [ultrarenderdemo on github](http://github.com/jamiecurle/ultrarenderdemo)

