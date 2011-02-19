# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BlogImage'
        db.create_table('posts_blogimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('src', self.gf('apps.utils.fields.ImageWithThumbsField')(blank=False)),
        ))
        db.send_create_signal('posts', ['BlogImage'])

        # Adding field 'BlogPost.created'
        db.add_column('posts_blogpost', 'created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 2, 18, 11, 25, 52, 441004)), keep_default=False)

        # Adding field 'BlogPost.modified'
        db.add_column('posts_blogpost', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2011, 2, 18), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'BlogImage'
        db.delete_table('posts_blogimage')

        # Deleting field 'BlogPost.created'
        db.delete_column('posts_blogpost', 'created')

        # Deleting field 'BlogPost.modified'
        db.delete_column('posts_blogpost', 'modified')


    models = {
        'posts.blogimage': {
            'Meta': {'object_name': 'BlogImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'src': ('apps.utils.fields.ImageWithThumbsField', [], {'blank': 'False'})
        },
        'posts.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_rendered': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 2, 18, 11, 25, 52, 441004)'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['posts']
