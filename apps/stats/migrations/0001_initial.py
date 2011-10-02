# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Visit'
        db.create_table('stats_visit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('http_referer', self.gf('django.db.models.fields.TextField')()),
            ('path_info', self.gf('django.db.models.fields.TextField')()),
            ('remote_addr', self.gf('django.db.models.fields.IPAddressField')(max_length=15, blank=True)),
            ('sessionid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('stats', ['Visit'])


    def backwards(self, orm):
        
        # Deleting model 'Visit'
        db.delete_table('stats_visit')


    models = {
        'stats.visit': {
            'Meta': {'object_name': 'Visit'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'http_referer': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path_info': ('django.db.models.fields.TextField', [], {}),
            'remote_addr': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'sessionid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['stats']
