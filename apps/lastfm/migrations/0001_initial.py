# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Scrobble'
        db.create_table('lastfm_scrobble', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('streamable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('artist_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('artist_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('artist_mid', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('album_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('album_mid', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('lastfm', ['Scrobble'])


    def backwards(self, orm):
        
        # Deleting model 'Scrobble'
        db.delete_table('lastfm_scrobble')


    models = {
        'lastfm.scrobble': {
            'Meta': {'ordering': "['-played_on']", 'object_name': 'Scrobble'},
            'album_mid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'album_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'artist_mid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'artist_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'artist_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'streamable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['lastfm']
