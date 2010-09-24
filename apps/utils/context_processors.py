from django.conf import settings

def grid(request):
    return{
        'GRID' : getattr(settings, 'GRID', False)
    }