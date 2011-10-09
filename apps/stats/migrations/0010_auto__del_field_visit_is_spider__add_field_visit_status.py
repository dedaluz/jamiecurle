# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Visit.is_spider'
        db.delete_column('stats_visit', 'is_spider')

        # Adding field 'Visit.status'
        db.add_column('stats_visit', 'status', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Visit.is_spider'
        db.add_column('stats_visit', 'is_spider', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Deleting field 'Visit.status'
        db.delete_column('stats_visit', 'status')


    models = {
        'stats.querystringparameter': {
            'Meta': {'object_name': 'QuerystringParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stats.Visit']"})
        },
        'stats.scriptkiddie': {
            'Meta': {'object_name': 'ScriptKiddie'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.TextField', [], {})
        },
        'stats.spider': {
            'Meta': {'object_name': 'Spider'},
            'disallow': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'stats.visit': {
            'Meta': {'object_name': 'Visit'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'http_referer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path_info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'remote_addr': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'sessionid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['stats']
