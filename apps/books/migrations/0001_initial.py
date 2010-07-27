# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Book'
        db.create_table('books_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('photo', self.gf('apps.utils.fields.ImageWithThumbsField')(blank=False)),
            ('status', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal('books', ['Book'])


    def backwards(self, orm):
        
        # Deleting model 'Book'
        db.delete_table('books_book')


    models = {
        'books.book': {
            'Meta': {'object_name': 'Book'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'photo': ('apps.utils.fields.ImageWithThumbsField', [], {'blank': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['books']
