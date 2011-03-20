from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

class FileWidget(forms.FileInput):
    
    def __init__(self, attrs=None):
        super(FileWidget, self).__init__(attrs)
    
    def render(self, name, value, attrs):
        if value:
            try:
                document_name = '%s' % value
                document_name = document_name.rsplit('/', 1)
                document_name.reverse()
                output = '<img src="%s"> %s' % (icon_for_file_extention(value), document_name[0]) 
            except Exception, e:
                output = u'<img src="%sicons/fileicons/small/_blank.png">' % settings.MEDIA_URL
        else:
            output =  super(forms.FileInput, self).render(name, value, attrs)
        return mark_safe(output)
    

def icon_for_file_extention(path, size="small"):
    
    full_path = '%s' % path
    path, ext = full_path.rsplit('.', 1)
    document_name = full_path.rsplit('/', 1)
    document_name.reverse()
    
    if ext == 'docx':
        ext = 'doc'
    
    extentions = ('aac','ai','aiff','avi','bmp','c','cpp','css',
        'dat','dmg','doc','dotx','dwg','dxf','eps','exe','flv','gif',
        'h','hpp','html','ics','iso','java','jpg','key','mid','mp3',
        'mp4','mpg','odf','ods','odt','otp','ots','ott','pdf','php',
        'ppt','psd','py','qt','rar','rb','rtf','sql','tga','tgz',
        'tiff','txt','wav','xls','xlsx','xml','yml','zip')
    
    if ext in extentions:
        return '%sicons/fileicons/%s/%s.png' % (settings.MEDIA_URL, size, ext)
    else:
        return '%sicons/fileicons/%s/_blank.png' % (settings.MEDIA_URL, size)


class ImageWidget(forms.FileInput):
    def __init__(self, attrs=None, template=None, width=92, height=92):
        self.width = width
        self.height = height
        super(ImageWidget, self).__init__(attrs)
    
    
    def render(self, name, value, attrs=None):
        if value:
            try:
                path = '%s' % value
                path, ext = path.rsplit('.', 1)
                output = u'<img src="%s%s.200x200.%s" width="100" height="100">' % (settings.MEDIA_URL ,path, ext)
            except Exception, e:
                output = u'<img src="%s%s" width="%s" height="%s">' % (settings.MEDIA_URL, value, self.width, self.height)
        else:
            output = super(forms.FileInput, self).render(name, value, attrs)
        
        return mark_safe(output)
    
