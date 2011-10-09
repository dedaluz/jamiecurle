# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'ScriptKiddie'
        db.delete_table('stats_scriptkiddie')

        # Adding model 'Script'
        db.create_table('stats_script', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('stats', ['Script'])


    def backwards(self, orm):
        
        # Adding model 'ScriptKiddie'
        db.create_table('stats_scriptkiddie', (
            ('path', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('stats', ['ScriptKiddie'])

        # Deleting model 'Script'
        db.delete_table('stats_script')


    models = {
        'stats.querystringparameter': {
            'Meta': {'object_name': 'QuerystringParameter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stats.Visit']"})
        },
        'stats.script': {
            'Meta': {'object_name': 'Script'},
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
