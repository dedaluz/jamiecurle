from django.conf import settings

def grid(request):
    return{
        'DISQUS_DEV' : getattr(settings, 'DISQUS_DEV', False),
        'GRID' : getattr(settings, 'GRID', False)
    }