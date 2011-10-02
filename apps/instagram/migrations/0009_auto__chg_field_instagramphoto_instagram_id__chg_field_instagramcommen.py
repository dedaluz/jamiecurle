# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'InstagramPhoto.instagram_id'
        db.alter_column('instagram_instagramphoto', 'instagram_id', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'InstagramComment.instagram_id'
        db.alter_column('instagram_instagramcomment', 'instagram_id', self.gf('django.db.models.fields.CharField')(max_length=255))


    def backwards(self, orm):
        
        # Changing field 'InstagramPhoto.instagram_id'
        db.alter_column('instagram_instagramphoto', 'instagram_id', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'InstagramComment.instagram_id'
        db.alter_column('instagram_instagramcomment', 'instagram_id', self.gf('django.db.models.fields.PositiveIntegerField')())


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
            'instagram_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'instagramphoto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['instagram.InstagramPhoto']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'instagram.instagramphoto': {
            'Meta': {'ordering': "['-created']", 'object_name': 'InstagramPhoto'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'instagram_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '6', 'blank': 'True'}),
            'like_count': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'location_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '6', 'blank': 'True'}),
            'low_resolution': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'standard_resolution': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
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
