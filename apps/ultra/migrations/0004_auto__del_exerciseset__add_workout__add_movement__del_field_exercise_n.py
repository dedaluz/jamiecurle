# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'ExerciseSet'
        db.delete_table('ultra_exerciseset')

        # Adding model 'Workout'
        db.create_table('ultra_workout', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('completed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('ultra', ['Workout'])

        # Adding model 'Movement'
        db.create_table('ultra_movement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('ultra', ['Movement'])

        # Deleting field 'Exercise.name'
        db.delete_column('ultra_exercise', 'name')

        # Adding field 'Exercise.workout'
        db.add_column('ultra_exercise', 'workout', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['ultra.Workout']), keep_default=False)

        # Adding field 'Exercise.movement'
        db.add_column('ultra_exercise', 'movement', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['ultra.Movement']), keep_default=False)

        # Adding field 'Exercise.sets'
        db.add_column('ultra_exercise', 'sets', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1), keep_default=False)

        # Adding field 'Exercise.reps'
        db.add_column('ultra_exercise', 'reps', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1), keep_default=False)

        # Adding field 'Exercise.load'
        db.add_column('ultra_exercise', 'load', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'ExerciseSet'
        db.create_table('ultra_exerciseset', (
            ('load', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('reps', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movement', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ultra.Exercise'])),
        ))
        db.send_create_signal('ultra', ['ExerciseSet'])

        # Deleting model 'Workout'
        db.delete_table('ultra_workout')

        # Deleting model 'Movement'
        db.delete_table('ultra_movement')

        # Adding field 'Exercise.name'
        db.add_column('ultra_exercise', 'name', self.gf('django.db.models.fields.CharField')(default='a', max_length=255), keep_default=False)

        # Deleting field 'Exercise.workout'
        db.delete_column('ultra_exercise', 'workout_id')

        # Deleting field 'Exercise.movement'
        db.delete_column('ultra_exercise', 'movement_id')

        # Deleting field 'Exercise.sets'
        db.delete_column('ultra_exercise', 'sets')

        # Deleting field 'Exercise.reps'
        db.delete_column('ultra_exercise', 'reps')

        # Deleting field 'Exercise.load'
        db.delete_column('ultra_exercise', 'load')


    models = {
        'ultra.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'load': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'movement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ultra.Movement']"}),
            'reps': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'sets': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ultra.Workout']"})
        },
        'ultra.movement': {
            'Meta': {'object_name': 'Movement'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'ultra.workout': {
            'Meta': {'object_name': 'Workout'},
            'completed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['ultra']
