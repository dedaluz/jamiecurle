# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Img.license_url'
        db.delete_column('assets_img', 'license_url')

        # Deleting field 'Img.description'
        db.delete_column('assets_img', 'description')

        # Deleting field 'Img.author'
        db.delete_column('assets_img', 'author')


    def backwards(self, orm):
        
        # Adding field 'Img.license_url'
        db.add_column('assets_img', 'license_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Img.description'
        db.add_column('assets_img', 'description', self.gf('django.db.models.fields.TextField')(default=datetime.date(2010, 8, 24), blank=True), keep_default=False)

        # Adding field 'Img.author'
        db.add_column('assets_img', 'author', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)


    models = {
        'assets.css': {
            'Meta': {'object_name': 'Css'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '10'}),
            'path': ('django.db.models.fields.FilePathField', [], {'path': "'/Users/jcurle/Sites/jamiecurle/templates/assets/css'", 'max_length': '100', 'recursive': 'True'}),
            'stylesheets': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['info.Page']", 'null': 'True', 'blank': 'True'})
        },
        'assets.img': {
            'Meta': {'object_name': 'Img'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['info.Page']", 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '10'}),
            'src': ('apps.utils.fields.ImageWithThumbsField', [], {'blank': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'assets.js': {
            'Meta': {'object_name': 'Js'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '10'}),
            'path': ('django.db.models.fields.FilePathField', [], {'path': "'/Users/jcurle/Sites/jamiecurle/templates/assets/js'", 'max_length': '100', 'recursive': 'True'}),
            'scripts': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['info.Page']", 'null': 'True', 'blank': 'True'})
        },
        'blog.post': {
            'Meta': {'object_name': 'Post'},
            'comments': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '2'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'books.book': {
            'Meta': {'object_name': 'Book'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'purchased': ('django.db.models.fields.DateField', [], {}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'info.page': {
            'Meta': {'object_name': 'Page'},
            'comments': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '2'}),
            'sticky': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['assets']
