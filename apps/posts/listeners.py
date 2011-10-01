from django.contrib.markup.templatetags.markup import markdown


def render_content(sender, instance, **kwargs):
    from apps.posts.templatetags.posts_tags import render

    instance.content_rendered = render(instance.content)
    