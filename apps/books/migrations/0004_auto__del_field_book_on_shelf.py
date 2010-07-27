# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Book.on_shelf'
        db.delete_column('books_book', 'on_shelf')


    def backwards(self, orm):
        
        # Adding field 'Book.on_shelf'
        db.add_column('books_book', 'on_shelf', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)


    models = {
        'books.book': {
            'Meta': {'object_name': 'Book'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'photo': ('apps.utils.fields.ImageWithThumbsField', [], {'blank': 'False'}),
            'purchased': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['books']
