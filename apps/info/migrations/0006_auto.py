# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing M2M table for field stylesheets on 'Page'
        db.delete_table('info_page_stylesheets')

        # Removing M2M table for field scripts on 'Page'
        db.delete_table('info_page_scripts')

        # Removing M2M table for field images on 'Page'
        db.delete_table('info_page_images')


    def backwards(self, orm):
        
        # Adding M2M table for field stylesheets on 'Page'
        db.create_table('info_page_stylesheets', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_page', models.ForeignKey(orm['info.page'], null=False)),
            ('to_page', models.ForeignKey(orm['info.page'], null=False))
        ))
        db.create_unique('info_page_stylesheets', ['from_page_id', 'to_page_id'])

        # Adding M2M table for field scripts on 'Page'
        db.create_table('info_page_scripts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_page', models.ForeignKey(orm['info.page'], null=False)),
            ('to_page', models.ForeignKey(orm['info.page'], null=False))
        ))
        db.create_unique('info_page_scripts', ['from_page_id', 'to_page_id'])

        # Adding M2M table for field images on 'Page'
        db.create_table('info_page_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_page', models.ForeignKey(orm['info.page'], null=False)),
            ('to_page', models.ForeignKey(orm['info.page'], null=False))
        ))
        db.create_unique('info_page_images', ['from_page_id', 'to_page_id'])


    models = {
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
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['info']
