# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Page.tags'
        db.add_column('info_page', 'tags', self.gf('tagging.fields.TagField')(default=''), keep_default=False)

        # Adding field 'Page.status'
        db.add_column('info_page', 'status', self.gf('django.db.models.fields.SmallIntegerField')(default=2), keep_default=False)

        # Adding field 'Page.featured'
        db.add_column('info_page', 'featured', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)

        # Adding field 'Page.comments'
        db.add_column('info_page', 'comments', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True), keep_default=False)

        # Adding field 'Page.created'
        db.add_column('info_page', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime.now(), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Page.tags'
        db.delete_column('info_page', 'tags')

        # Deleting field 'Page.status'
        db.delete_column('info_page', 'status')

        # Deleting field 'Page.featured'
        db.delete_column('info_page', 'featured')

        # Deleting field 'Page.comments'
        db.delete_column('info_page', 'comments')

        # Deleting field 'Page.created'
        db.delete_column('info_page', 'created')


    models = {
        'info.page': {
            'Meta': {'object_name': 'Page'},
            'comments': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'image_set'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['info.Page']"}),
            'scripts': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'js_set'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['info.Page']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '2'}),
            'stylesheets': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'css_set'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['info.Page']"}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['info']
