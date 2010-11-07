# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Movement'
        db.create_table('ultra_movement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('ultra', ['Movement'])

        # Adding model 'WorkoutTemplate'
        db.create_table('ultra_workouttemplate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('start', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('finish', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('ultra', ['WorkoutTemplate'])

        # Adding model 'SetTemplate'
        db.create_table('ultra_settemplate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ultra.WorkoutTemplate'])),
            ('movement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ultra.Movement'])),
            ('total', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('reps', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('ultra', ['SetTemplate'])

        # Adding model 'Workout'
        db.create_table('ultra_workout', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workouttemplate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ultra.WorkoutTemplate'])),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('completed', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('ultra', ['Workout'])

        # Adding model 'Set'
        db.create_table('ultra_set', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ultra.Movement'])),
            ('total', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('reps', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('ultra', ['Set'])


    def backwards(self, orm):
        
        # Deleting model 'Movement'
        db.delete_table('ultra_movement')

        # Deleting model 'WorkoutTemplate'
        db.delete_table('ultra_workouttemplate')

        # Deleting model 'SetTemplate'
        db.delete_table('ultra_settemplate')

        # Deleting model 'Workout'
        db.delete_table('ultra_workout')

        # Deleting model 'Set'
        db.delete_table('ultra_set')


    models = {
        'ultra.movement': {
            'Meta': {'object_name': 'Movement'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'ultra.set': {
            'Meta': {'object_name': 'Set'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ultra.Movement']"}),
            'reps': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'total': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'ultra.settemplate': {
            'Meta': {'object_name': 'SetTemplate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ultra.Movement']"}),
            'reps': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ultra.WorkoutTemplate']"}),
            'total': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'ultra.workout': {
            'Meta': {'object_name': 'Workout'},
            'completed': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'workouttemplate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ultra.WorkoutTemplate']"})
        },
        'ultra.workouttemplate': {
            'Meta': {'object_name': 'WorkoutTemplate'},
            'finish': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['ultra']
