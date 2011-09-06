# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'InstagramPhoto'
        db.create_table('instagram_instagramphoto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('instagram_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('like_count', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('user_full_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('low_resolution', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('thumbnail', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('standard_resolution', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=6)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=6)),
            ('location_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('location_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('instagram', ['InstagramPhoto'])

        # Adding model 'InstagramComment'
        db.create_table('instagram_instagramcomment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('instagramphoto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['instagram.InstagramPhoto'])),
        ))
        db.send_create_signal('instagram', ['InstagramComment'])


    def backwards(self, orm):
        
        # Deleting model 'InstagramPhoto'
        db.delete_table('instagram_instagramphoto')

        # Deleting model 'InstagramComment'
        db.delete_table('instagram_instagramcomment')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'instagram.instagramcomment': {
            'Meta': {'object_name': 'InstagramComment'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instagramphoto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['instagram.InstagramPhoto']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'instagram.instagramphoto': {
            'Meta': {'object_name': 'InstagramPhoto'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instagram_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '6'}),
            'like_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'location_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '6'}),
            'low_resolution': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'standard_resolution': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'user_full_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        },
        'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_items'", 'to': "orm['taggit.Tag']"})
        }
    }

    complete_apps = ['instagram']
