# -*- coding: utf-8 -*-
import MySQLdb
import re
import shutil
import os
import sys
from PIL import Image
import cStringIO
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.encoding import smart_unicode
from apps.posts.models import BlogPost, BlogImage
from apps.posts.templatetags.posts_tags import render

ORIGINAL_IMAGE_PATH  = '/Volumes/Wild Ol Backup Bill/ManualBackups/jamiecurle-migrate'
NEW_IMAGE_PATH = '/Users/jcurle/Sites/jamiecurle/media/'




def generate_thumb(img, thumb_size, format, path):
    """
    Generates a thumbnail image and returns a ContentFile object with the thumbnail
    
    Parameters:
    ===========
    img         File object
    
    thumb_size  desired thumbnail size, ie: (200,120)
    
    format      format of the original image ('jpeg','gif','png',...)
                (this format will be used for the generated thumbnail, too)
    """
    
    img.seek(0) # see http://code.djangoproject.com/ticket/8222 for details
    image = Image.open(img)
    
    # Convert to RGB if necessary
    if image.mode not in ('L', 'RGB', 'RGBA'):
        image = image.convert('RGB')
        
    # get size
    thumb_w, thumb_h = thumb_size
    
    
    # If you want to generate a square thumbnail
    if thumb_w == thumb_h:
        # quad
        xsize, ysize = image.size
        # get minimum size
        minsize = min(xsize,ysize)
        # largest square possible in the image
        xnewsize = (xsize-minsize)/2
        ynewsize = (ysize-minsize)/2
        # crop it
        image2 = image.crop((xnewsize, ynewsize, xsize-xnewsize, ysize-ynewsize))
        # load is necessary after crop                
        image2.load()
        # thumbnail of the cropped image (with ANTIALIAS to make it look better)
        image2.thumbnail(thumb_size, Image.ANTIALIAS)
    else:
        # not quad
        image2 = image
        image2.thumbnail(thumb_size, Image.ANTIALIAS)
    
    #io = cStringIO.StringIO()
    # PNG and GIF are the same, JPG is JPEG
    if format.upper()=='JPG':
        format = 'JPEG'
    elif format.upper()=='TIF':
        format = 'TIFF'
    
    image2.save(path, format, quality=90)

def upload_path(instance, filename):
    filename = filename.replace('..', '.')
    return  "uploads/%s/%s/%s" % ('%s' % instance.blogpost.created.strftime("%Y/%m/%d"), instance.__class__.__name__.lower(), filename )



class Command(BaseCommand):
    #args = '<poll_id poll_id ...>'
    help = 'migrates old blog posts'
    
    def handle(self, *args, **options):
        # destroy everything
        for p in BlogPost.objects.all():
            p.delete()
        
        for i in BlogImage.objects.all():
            i.delete()
        
        shutil.rmtree('/Users/jcurle/Sites/jamiecurle/media/uploads')
        
        # create the connection and grab the results
        db = MySQLdb.connect(host="localhost",user="designcc",db="jc_rails_import", cursorclass = MySQLdb.cursors.DictCursor)
        db.set_character_set('utf8')
        
        c = db.cursor()
        c.execute('SET NAMES utf8;')
        c.execute('SET CHARACTER SET utf8;')
        c.execute('SET character_set_connection=utf8;')
        sql = "select * from posts"
        c.execute(sql)
        results = c.fetchall()
        # build the posts
        for row in results:
            obj = BlogPost()
            obj.id = row['id']
            obj.title = row['title']
            obj.slug = row['url']
            obj.description = row['description']
            # do some replacing
            obj.content.encode('utf-8')
            obj.content = smart_unicode(row['body'])
            obj.created = row['created_at']
            obj.content_rendered = render(obj.content)
            obj.status = BlogPost.PUBLISHED
            obj.save()
            # do the tags
            sql = "select tag_id from taggings where taggable_id = %s" % obj.pk
            c.execute(sql)
            tag_rows = c.fetchall()
            for tag_row in tag_rows:
                sql = "select * from tags where id=%s" % tag_row['tag_id']
                c.execute(sql)
                tags = c.fetchall()
                for tag in tags:
                    obj.tags.add(tag['name'])
            # do the images that are in with markdowm
            md = re.compile(r'\!\[[\w\s\](\/\.]+\)')
            images = md.findall(obj.content)
            for i in images:
                title, path = i.split('(')
                title = title.replace('!', '').replace('[', '').replace(']', '')
                path = path.replace(')', '')
                # create a new blog image
                blogimage = BlogImage()
                blogimage.blogpost = obj
                # do the title
                blogimage.title = title
                # do the paths
                # get the filename
                filename = path.rsplit('/')
                filename.reverse()
                filename = filename[0]
                new_image_upload  = upload_path(blogimage, filename)
                blogimage.src = new_image_upload
                blogimage.save()
                # set the paths
                original_image_path = ORIGINAL_IMAGE_PATH + path
                new_image_path = NEW_IMAGE_PATH + new_image_upload
                # ensure that all of the directories exist
                dirs = new_image_path.split('/')
                # get rid of the filename
                dirs.pop()
                # now walk the three and create the dirs that don't exists
                path_so_far = ''
                for i,d in enumerate(dirs):
                    # skip the first iteration
                    if i == 0:
                        continue
                    # now set the path so far
                    path_so_far += '/%s' % d
                    if not os.path.exists(path_so_far):
                        os.mkdir(path_so_far)
                # copy the image into the right place
                shutil.copy(original_image_path , new_image_path)
                # now do the sizes
                for size in settings.IMAGE_SIZES:
                    (w,h) = size
                    #if i.src.width >= w and i.src.height >= h:
                    split = blogimage.src.name.rsplit('.',1)
                    thumb_name = '%s.%sx%s.%s' % (split[0],w,h,split[1])
                    thumb_content = generate_thumb(blogimage.src.file, size, split[1], '%s%s' % (settings.MEDIA_ROOT, thumb_name))
                # now update the markdown
                obj.content = obj.content.replace(path, blogimage.l)
            # save it
            obj.save()
            # do any images that I've mised that 
            inlineimg_re = re.compile('/files/[\d]+/[\w\.]+')
            inlineimgs = inlineimg_re.findall(obj.content)
            
            for i in inlineimgs:
                path = i
                # create a new blog image
                blogimage = BlogImage()
                blogimage.blogpost = obj
                # do the title
                blogimage.title = title
                # do the paths
                # get the filename
                filename = path.rsplit('/')
                filename.reverse()
                filename = filename[0]


                title = filename.replace('_', ' ')



                new_image_upload  = upload_path(blogimage, filename)
                blogimage.src = new_image_upload
                blogimage.save()
                # set the paths
                original_image_path = ORIGINAL_IMAGE_PATH + path
                new_image_path = NEW_IMAGE_PATH + new_image_upload
                # ensure that all of the directories exist
                dirs = new_image_path.split('/')
                # get rid of the filename
                dirs.pop()
                # now walk the three and create the dirs that don't exists
                path_so_far = ''
                for i,d in enumerate(dirs):
                    # skip the first iteration
                    if i == 0:
                        continue
                    # now set the path so far
                    path_so_far += '/%s' % d
                    if not os.path.exists(path_so_far):
                        os.mkdir(path_so_far)
                # copy the image into the right place
                shutil.copy(original_image_path , new_image_path)
                # now do the sizes
                for size in settings.IMAGE_SIZES:
                    (w,h) = size
                    #if i.src.width >= w and i.src.height >= h:
                    split = blogimage.src.name.rsplit('.',1)
                    thumb_name = '%s.%sx%s.%s' % (split[0],w,h,split[1])
                    thumb_content = generate_thumb(blogimage.src.file, size, split[1], '%s%s' % (settings.MEDIA_ROOT, thumb_name))
                # now update the markdown
                obj.content = obj.content.replace(path, blogimage.l)            
            
            
            # re-render the content
            obj.content_rendered = render(obj.content)
            obj.save()
                