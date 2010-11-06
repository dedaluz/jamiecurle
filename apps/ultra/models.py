from django.db import models
from datetime import datetime


class Movement(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return '%s' % self.name
    

class WorkoutTemplate(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    start = models.DateField(default=datetime.now)
    finish = models.DateField(default=datetime.now)
    
    def __unicode__(self):
        return u'%s %s-%s' % (self.name, self.start.strftime('%b'), self.finish.strftime('%b %Y'))
    

class SetTemplate(models.Model):
    template = models.ForeignKey(WorkoutTemplate)
    movement = models.ForeignKey(Movement)
    total = models.PositiveSmallIntegerField(blank=True, null=True)
    reps = models.PositiveSmallIntegerField()
    
    def __unicode__(self):
        return '%s x %s' % (self.reps, self.movement.name)
    


class Workout(models.Model):
    workouttemplate = models.ForeignKey(WorkoutTemplate)
    notes = models.TextField(blank=True, null=True)
    completed = models.DateField(default=datetime.now)
    
    def __unicode__(self):
        return u'%s %s-%s' % (self.workouttemplate.name)
    
    
class Set(models.Model):
    movement = models.ForeignKey(Movement)
    total = models.PositiveSmallIntegerField(blank=True, null=True)
    reps = models.PositiveSmallIntegerField()
    
    def __unicode__(self):
        return '%s x %s' % (self.reps, self.movement.name)
    
#class CompletedWorkout(models.Model):
    