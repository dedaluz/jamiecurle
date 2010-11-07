# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Exercise'
        db.delete_table('ultra_exercise')

        # Deleting model 'Workout'
        db.delete_table('ultra_workout')

        # Adding model 'SetTemplate'
        db.create_table('ultra_settemplate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ultra.WorkoutTemplate'])),
            ('movement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ultra.Movement'])),
            ('total', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('reps', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('ultra', ['SetTemplate'])

        # Adding model 'WorkoutTemplate'
        db.create_table('ultra_workouttemplate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('start', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('finish', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('ultra', ['WorkoutTemplate'])


    def backwards(self, orm):
        
        # Adding model 'Exercise'
        db.create_table('ultra_exercise', (
            ('load', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ultra.Workout'])),
            ('reps', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('sets', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ultra.Movement'])),
        ))
        db.send_create_signal('ultra', ['Exercise'])

        # Adding model 'Workout'
        db.create_table('ultra_workout', (
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('completed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('ultra', ['Workout'])

        # Deleting model 'SetTemplate'
        db.delete_table('ultra_settemplate')

        # Deleting model 'WorkoutTemplate'
        db.delete_table('ultra_workouttemplate')


    models = {
        'ultra.movement': {
            'Meta': {'object_name': 'Movement'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'ultra.settemplate': {
            'Meta': {'object_name': 'SetTemplate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ultra.Movement']"}),
            'reps': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ultra.WorkoutTemplate']"}),
            'total': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'ultra.workouttemplate': {
            'Meta': {'object_name': 'WorkoutTemplate'},
            'finish': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['ultra']
