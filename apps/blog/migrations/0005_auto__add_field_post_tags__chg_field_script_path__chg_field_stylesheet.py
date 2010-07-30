# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Post.tags'
        db.add_column('blog_post', 'tags', self.gf('tagging.fields.TagField')(default=''), keep_default=False)

        # Changing field 'Script.path'
        db.alter_column('blog_script', 'path', self.gf('django.db.models.fields.FilePathField')(path='/Users/jcurle/Sites/jamiecurle/templates/blog/js', max_length=100, recursive=True))

        # Changing field 'StyleSheet.path'
        db.alter_column('blog_stylesheet', 'path', self.gf('django.db.models.fields.FilePathField')(path='/Users/jcurle/Sites/jamiecurle/templates/blog/css', max_length=100, recursive=True))


    def backwards(self, orm):
        
        # Deleting field 'Post.tags'
        db.delete_column('blog_post', 'tags')

        # Changing field 'Script.path'
        db.alter_column('blog_script', 'path', self.gf('django.db.models.fields.FilePathField')(path='%s/blog/js', max_length=100, recursive=True))

        # Changing field 'StyleSheet.path'
        db.alter_column('blog_stylesheet', 'path', self.gf('django.db.models.fields.FilePathField')(path='%s/blog/css', max_length=100, recursive=True))


    models = {
        'blog.photo': {
            'Meta': {'object_name': 'Photo'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'photo': ('apps.utils.fields.ImageWithThumbsField', [], {'blank': 'False'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Post']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'blog.post': {
            'Meta': {'object_name': 'Post'},
            'comments': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scripts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['blog.Script']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '2'}),
            'stylesheets': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['blog.StyleSheet']", 'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'blog.script': {
            'Meta': {'object_name': 'Script'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.FilePathField', [], {'path': "'/Users/jcurle/Sites/jamiecurle/templates/blog/js'", 'max_length': '100', 'recursive': 'True'})
        },
        'blog.stylesheet': {
            'Meta': {'object_name': 'StyleSheet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.FilePathField', [], {'path': "'/Users/jcurle/Sites/jamiecurle/templates/blog/css'", 'max_length': '100', 'recursive': 'True'})
        }
    }

    complete_apps = ['blog']
