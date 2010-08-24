# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Attribution'
        db.create_table('assets_attribution', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('img', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['assets.Img'], unique=True)),
            ('license_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('assets', ['Attribution'])

        # Changing field 'Css.path'
        db.alter_column('assets_css', 'path', self.gf('django.db.models.fields.FilePathField')(max_length=100, path='/Users/jcurle/Sites/jamiecurle/templates/assets/css', null=True, recursive=True, blank=True))

        # Deleting field 'Img.description'
        db.delete_column('assets_img', 'description')

        # Deleting field 'Img.author'
        db.delete_column('assets_img', 'author')

        # Deleting field 'Img.license_url'
        db.delete_column('assets_img', 'license_url')

        # Changing field 'Js.path'
        db.alter_column('assets_js', 'path', self.gf('django.db.models.fields.FilePathField')(max_length=100, path='/Users/jcurle/Sites/jamiecurle/templates/assets/js', null=True, recursive=True, blank=True))


    def backwards(self, orm):
        
        # Deleting model 'Attribution'
        db.delete_table('assets_attribution')

        # Changing field 'Css.path'
        db.alter_column('assets_css', 'path', self.gf('django.db.models.fields.FilePathField')(path='/Users/jcurle/Sites/jamiecurle/templates/assets/css', max_length=100, recursive=True))

        # Adding field 'Img.description'
        db.add_column('assets_img', 'description', self.gf('django.db.models.fields.TextField')(default='meh', blank=True), keep_default=False)

        # Adding field 'Img.author'
        db.add_column('assets_img', 'author', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Img.license_url'
        db.add_column('assets_img', 'license_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True), keep_default=False)

        # Changing field 'Js.path'
        db.alter_column('assets_js', 'path', self.gf('django.db.models.fields.FilePathField')(path='/Users/jcurle/Sites/jamiecurle/templates/assets/js', max_length=100, recursive=True))


    models = {
        'assets.attribution': {
            'Meta': {'object_name': 'Attribution'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['assets.Img']", 'unique': 'True'}),
            'license_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'assets.css': {
            'Meta': {'object_name': 'Css'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '10'}),
            'path': ('django.db.models.fields.FilePathField', [], {'max_length': '100', 'path': "'/Users/jcurle/Sites/jamiecurle/templates/assets/css'", 'null': 'True', 'recursive': 'True', 'blank': 'True'})
        },
        'assets.img': {
            'Meta': {'object_name': 'Img'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '10'}),
            'src': ('apps.utils.fields.ImageWithThumbsField', [], {'blank': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'assets.js': {
            'Meta': {'object_name': 'Js'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '10'}),
            'path': ('django.db.models.fields.FilePathField', [], {'max_length': '100', 'path': "'/Users/jcurle/Sites/jamiecurle/templates/assets/js'", 'null': 'True', 'recursive': 'True', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['assets']
