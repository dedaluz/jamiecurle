# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Tweet'
        db.create_table('twitter_tweet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('twitter_id', self.gf('django.db.models.fields.BigIntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('is_favourite', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('reply_to_status_id', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('reply_to_user_id', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('reply_to_user_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('retweet_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal('twitter', ['Tweet'])


    def backwards(self, orm):
        
        # Deleting model 'Tweet'
        db.delete_table('twitter_tweet')


    models = {
        'twitter.tweet': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Tweet'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_favourite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reply_to_status_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reply_to_user_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'reply_to_user_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'retweet_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'twitter_id': ('django.db.models.fields.BigIntegerField', [], {})
        }
    }

    complete_apps = ['twitter']
