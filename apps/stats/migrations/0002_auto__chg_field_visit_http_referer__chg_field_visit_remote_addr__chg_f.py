# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Visit.http_referer'
        db.alter_column('stats_visit', 'http_referer', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Visit.remote_addr'
        db.alter_column('stats_visit', 'remote_addr', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True))

        # Changing field 'Visit.sessionid'
        db.alter_column('stats_visit', 'sessionid', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Visit.path_info'
        db.alter_column('stats_visit', 'path_info', self.gf('django.db.models.fields.TextField')(null=True))


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Visit.http_referer'
        raise RuntimeError("Cannot reverse this migration. 'Visit.http_referer' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Visit.remote_addr'
        raise RuntimeError("Cannot reverse this migration. 'Visit.remote_addr' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Visit.sessionid'
        raise RuntimeError("Cannot reverse this migration. 'Visit.sessionid' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Visit.path_info'
        raise RuntimeError("Cannot reverse this migration. 'Visit.path_info' and its values cannot be restored.")


    models = {
        'stats.visit': {
            'Meta': {'object_name': 'Visit'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'http_referer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path_info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'remote_addr': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'sessionid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['stats']
