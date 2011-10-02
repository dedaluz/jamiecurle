# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Quote'
        db.create_table('quotes_quote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('quotes', ['Quote'])


    def backwards(self, orm):
        
        # Deleting model 'Quote'
        db.delete_table('quotes_quote')


    models = {
        'quotes.quote': {
            'Meta': {'object_name': 'Quote'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['quotes']
