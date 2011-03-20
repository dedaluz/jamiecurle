import MySQLdb, re
from django.core.management.base import BaseCommand, CommandError
from apps.posts.models import BlogPost, BlogImage
from apps.posts.templatetags.posts_tags import render

class Command(BaseCommand):
    #args = '<poll_id poll_id ...>'
    help = 'migrates old blog posts'

    def handle(self, *args, **options):
        # destroy everything
        for p in BlogPost.objects.all():
            p.delete()
        
        for i in BlogImage.objects.all():
            i.delete()
        
        # create the connection and grab the results
        db=MySQLdb.connect(host="localhost",user="designcc",db="jc_rails_import", cursorclass = MySQLdb.cursors.DictCursor)
        c = db.cursor()
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
            obj.content = unicode(row['body'], errors='ignore')
            obj.created = row['created_at']
            obj.content_rendered = render(obj.content)
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
            # regex the images
            m = re.match('\!\[[\w\s\](\/\.]+\)', obj.content)
            
            if m is not None:
                print m.groups()
                for i in m.groups():
                    print i
                    
            
        print 'hai'