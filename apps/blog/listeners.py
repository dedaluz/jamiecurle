from django.contrib.markup.templatetags.markup import markdown
from django.conf import settings


def render_content(sender, instance, **kwargs):
    from apps.blog.templatetags.blog_tags import render
    instance.content_rendered = render(instance.content)
    