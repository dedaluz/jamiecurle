# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ExerciseSet'
        db.create_table('ultra_exerciseset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reps', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('movement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ultra.Exercise'])),
            ('load', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('ultra', ['ExerciseSet'])

        # Adding model 'Exercise'
        db.create_table('ultra_exercise', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('ultra', ['Exercise'])


    def backwards(self, orm):
        
        # Deleting model 'ExerciseSet'
        db.delete_table('ultra_exerciseset')

        # Deleting model 'Exercise'
        db.delete_table('ultra_exercise')


    models = {
        'ultra.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'ultra.exerciseset': {
            'Meta': {'object_name': 'ExerciseSet'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'load': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'movement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ultra.Exercise']"}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'reps': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['ultra']
