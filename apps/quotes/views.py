# -*- coding: utf-8 -*-
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from models import Author, Quote


def author(request, author_slug):
    author = get_object_or_404(Author, slug=author_slug)
    
    return TemplateResponse(request, 'quotes/author.html',{
        'author' : author,
    })
    

def show(request, author_slug, quote_pk):
    author = get_object_or_404(Author, slug=author_slug)
    quote = get_object_or_404(Quote, pk=quote_pk, author=author)
    
    return TemplateResponse(request, 'quotes/show.html',{
        'quote' : quote,
        'author' : author,
    })
    
    
def index(request):
    quotes = Quote.objects.all()
    return TemplateResponse(request, 'quotes/index.html',{
        'quotes' : quotes,
    })
