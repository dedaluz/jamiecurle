# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Workout'
        db.delete_table('ultra_workout')

        # Deleting model 'KettlebellWorkout'
        db.delete_table('ultra_kettlebellworkout')

        # Deleting model 'Exercise'
        db.delete_table('ultra_exercise')

        # Deleting model 'BarbellSets'
        db.delete_table('ultra_barbellsets')


    def backwards(self, orm):
        
        # Adding model 'Workout'
        db.create_table('ultra_workout', (
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('type', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('ultra', ['Workout'])

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

        # Adding model 'BarbellSets'
        db.create_table('ultra_barbellsets', (
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ultra.Workout'])),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('total', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('reps', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ultra.Exercise'])),
        ))
        db.send_create_signal('ultra', ['BarbellSets'])


    models = {
        
    }

    complete_apps = ['ultra']
