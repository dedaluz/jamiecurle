# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Css.stylesheets'
        db.delete_column('assets_css', 'stylesheets_id')

        # Adding field 'Css.content_type'
        db.add_column('assets_css', 'content_type', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['contenttypes.ContentType']), keep_default=False)

        # Adding field 'Css.object_id'
        db.add_column('assets_css', 'object_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=1), keep_default=False)

        # Deleting field 'Img.images'
        db.delete_column('assets_img', 'images_id')

        # Adding field 'Img.content_type'
        db.add_column('assets_img', 'content_type', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['contenttypes.ContentType']), keep_default=False)

        # Adding field 'Img.object_id'
        db.add_column('assets_img', 'object_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=1), keep_default=False)

        # Adding field 'Img.description'
        db.add_column('assets_img', 'description', self.gf('django.db.models.fields.TextField')(default=1, blank=True), keep_default=False)

        # Adding field 'Img.license_url'
        db.add_column('assets_img', 'license_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Img.author'
        db.add_column('assets_img', 'author', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Deleting field 'Js.scripts'
        db.delete_column('assets_js', 'scripts_id')

        # Adding field 'Js.content_type'
        db.add_column('assets_js', 'content_type', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['contenttypes.ContentType']), keep_default=False)

        # Adding field 'Js.object_id'
        db.add_column('assets_js', 'object_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=1), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Css.stylesheets'
        db.add_column('assets_css', 'stylesheets', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['info.Page'], null=True, blank=True), keep_default=False)

        # Deleting field 'Css.content_type'
        db.delete_column('assets_css', 'content_type_id')

        # Deleting field 'Css.object_id'
        db.delete_column('assets_css', 'object_id')

        # Adding field 'Img.images'
        db.add_column('assets_img', 'images', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['info.Page'], null=True, blank=True), keep_default=False)

        # Deleting field 'Img.content_type'
        db.delete_column('assets_img', 'content_type_id')

        # Deleting field 'Img.object_id'
        db.delete_column('assets_img', 'object_id')

        # Deleting field 'Img.description'
        db.delete_column('assets_img', 'description')

        # Deleting field 'Img.license_url'
        db.delete_column('assets_img', 'license_url')

        # Deleting field 'Img.author'
        db.delete_column('assets_img', 'author')

        # Adding field 'Js.scripts'
        db.add_column('assets_js', 'scripts', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['info.Page'], null=True, blank=True), keep_default=False)

        # Deleting field 'Js.content_type'
        db.delete_column('assets_js', 'content_type_id')

        # Deleting field 'Js.object_id'
        db.delete_column('assets_js', 'object_id')


    models = {
        'assets.css': {
            'Meta': {'object_name': 'Css'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '10'}),
            'path': ('django.db.models.fields.FilePathField', [], {'path': "'/Users/jcurle/Sites/jamiecurle/templates/assets/css'", 'max_length': '100', 'recursive': 'True'})
        },
        'assets.img': {
            'Meta': {'object_name': 'Img'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
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
            'path': ('django.db.models.fields.FilePathField', [], {'path': "'/Users/jcurle/Sites/jamiecurle/templates/assets/js'", 'max_length': '100', 'recursive': 'True'})
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
