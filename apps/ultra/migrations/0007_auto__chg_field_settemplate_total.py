# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'SetTemplate.total'
        db.alter_column('ultra_settemplate', 'total', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True))


    def backwards(self, orm):
        
        # Changing field 'SetTemplate.total'
        db.alter_column('ultra_settemplate', 'total', self.gf('django.db.models.fields.PositiveSmallIntegerField')())


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
            'total': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
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
