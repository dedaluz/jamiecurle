from django.db import models


class KettlebellWorkout(models.Model):
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return u'%s' % self.name
    

class Workout(models.Model):
    WORKOUT_A = 1
    WORKOUT_B = 2
    WORKOUT_CHOICES = (
        (WORKOUT_A, 'A'),
        (WORKOUT_B, 'B'),
    )
    type = models.PositiveSmallIntegerField(choices = WORKOUT_CHOICES)
    notes = models.TextField(blank=True)
    created = models.DateTimeField()
    
    def __unicode__(self):
        return u'Workout %s (%s)' % ( self.get_type_display(), self.created)
    

class BarbellSets(models.Model):
    exercise = models.ForeignKey(Exercise)
    workout = models.ForeignKey(Workout)
    total = models.PositiveSmallIntegerField()
    reps = models.PositiveSmallIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return u'%s - %s x %s @%s kg' % (self.exercise.name, self.total, self.reps, self.weight)
    
    
    