from django.contrib import admin
from models import Img, Css, Js

class ImgInline(admin.TabularInline):
    model = Img

class CssInline(admin.TabularInline):
    model = Css

class JsInline(admin.TabularInline):
    model = Js

admin.site.register(Img)
admin.site.register(Js)
admin.site.register(Css)
