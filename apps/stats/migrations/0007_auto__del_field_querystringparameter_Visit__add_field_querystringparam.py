# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'QuerystringParameter.Visit'
        db.delete_column('stats_querystringparameter', 'Visit_id')

        # Adding field 'QuerystringParameter.visit'
        db.add_column('stats_querystringparameter', 'visit', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['stats.Visit']), keep_default=False)


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'QuerystringParameter.Visit'
        raise RuntimeError("Cannot reverse this migration. 'QuerystringParameter.Visit' and its values cannot be restored.")

        # Deleting field 'QuerystringParameter.visit'
        db.delete_column('stats_querystringparameter', 'visit_id')


    models = {
        'stats.querystringparameter': {
            'Meta': {'object_name': 'QuerystringParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stats.Visit']"})
        },
        'stats.spider': {
            'Meta': {'object_name': 'Spider'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'stats.visit': {
            'Meta': {'object_name': 'Visit'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'http_referer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_spider': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'path_info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'remote_addr': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'sessionid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['stats']
