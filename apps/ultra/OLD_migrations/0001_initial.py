# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'KettlebellWorkout'
        db.create_table('ultra_kettlebellworkout', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('ultra', ['KettlebellWorkout'])

        # Adding model 'Exercise'
        db.create_table('ultra_exercise', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('ultra', ['Exercise'])

        # Adding model 'Workout'
        db.create_table('ultra_workout', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('ultra', ['Workout'])

        # Adding model 'BarbellSets'
        db.create_table('ultra_barbellsets', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ultra.Exercise'])),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ultra.Workout'])),
            ('total', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('reps', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('ultra', ['BarbellSets'])


    def backwards(self, orm):
        
        # Deleting model 'KettlebellWorkout'
        db.delete_table('ultra_kettlebellworkout')

        # Deleting model 'Exercise'
        db.delete_table('ultra_exercise')

        # Deleting model 'Workout'
        db.delete_table('ultra_workout')

        # Deleting model 'BarbellSets'
        db.delete_table('ultra_barbellsets')


    models = {
        'ultra.barbellsets': {
            'Meta': {'object_name': 'BarbellSets'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ultra.Exercise']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'reps': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'total': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ultra.Workout']"})
        },
        'ultra.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'ultra.kettlebellworkout': {
            'Meta': {'object_name': 'KettlebellWorkout'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'ultra.workout': {
            'Meta': {'object_name': 'Workout'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['ultra']
