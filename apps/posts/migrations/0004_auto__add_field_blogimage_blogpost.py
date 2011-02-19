# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'BlogImage.blogpost'
        db.add_column('posts_blogimage', 'blogpost', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['posts.BlogPost']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'BlogImage.blogpost'
        db.delete_column('posts_blogimage', 'blogpost_id')


    models = {
        'posts.blogimage': {
            'Meta': {'object_name': 'BlogImage'},
            'blogpost': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['posts.BlogPost']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'src': ('apps.utils.fields.ImageWithThumbsField', [], {'blank': 'False'})
        },
        'posts.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_rendered': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['posts']
