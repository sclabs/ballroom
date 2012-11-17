from django.db import models
from django.contrib.auth.models import User

class Level(models.Model):
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

class Style(models.Model):
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

class Dance(models.Model):
    name = models.CharField(max_length=10)
    style = models.ForeignKey(Style, related_name='dances')

    def __unicode__(self):
        return self.style.name + self.name
    
class Position(models.Model):
    WEIGHT_CHOICES = (
        ('L', 'Left'),
        ('R', 'Right'),
        ('S', 'Split'),
    )
    HOLD_CHOICES = (
        ('SHH', 'Single Hand Hold'),
        ('DHH', 'Double Hand Hold'),
        ('CLO', 'Closed'),
        ('FAN', 'Fan'),
        ('RTR', 'Right-to-Right'),
        ('PRM', 'Promenade'),
        ('SHD', 'Shadow'),
        ('FAW', 'Fallaway'),
        ('OTH', 'Other'),
    )
    lead_weight = models.CharField(max_length=1, choices=WEIGHT_CHOICES)
    follow_weight = models.CharField(max_length=1, choices=WEIGHT_CHOICES)
    hold = models.CharField(max_length=3, choices=HOLD_CHOICES)
    inside_partner = models.NullBooleanField(null=True)

    def __unicode__(self):
        return 'lead on %s, follow on %s, hold is %s, inside partner is %s' % (lead_weight, follow_weight, hold, inside_partner)

class Figure(models.Model):
    name = models.CharField(max_length=50)
    dance = models.ForeignKey(Dance, related_name='figures')
    level = models.ForeignKey(Level, related_name='figures')
    cross_phrase = models.NullBooleanField(null=True)
    start_position = models.ForeignKey(Position, related_name='into_options')
    end_position = models.ForeignKey(Position, related_name='from_options')
    rotation = models.IntegerField()
    length = models.IntegerField()
    count = models.CharField(max_length=1000)
    alt_count = models.CharField(max_length=1000, blank=True)
    lead_steps = models.CharField(max_length=1000)
    follow_steps = models.CharField(max_length=1000)
    comment = models.TextField()

    def __unicode__(self):
        return self.name

class Routine(models.Model):
    title = models.CharField(max_length=50)
    figures = models.ManyToManyField(Figure, through='FigureInstance')
    creator = models.ForeignKey(User, related_name='routines_created')
    editors = models.ManyToManyField(User, related_name='routines_editable')
    description = models.TextField()

    def __unicode__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=50)
    routine = models.ForeignKey(Routine, related_name='videos')
    link = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.title

class Profile(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name='profiles')
    friends = models.ManyToManyField('self')
    favorites = models.ManyToManyField(Routine, related_name='favorited_by')

    def __unicode__(self):
        return self.name

class FigureInstance(models.Model):
    figure = models.ForeignKey(Figure, related_name='instances')
    routine = models.ForeignKey(Routine, related_name='figure_instances')
    index = models.IntegerField()

    def __unicode__(self):
        return "%s at index %i in %s" % (self.figure.name, self.index, self.routine.name)

class Annotation(models.Model):
    routine = models.ForeignKey(Routine, related_name='annotations')
    start = models.CharField(max_length=10)
    end = models.CharField(max_length=10)
    message = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s from %s to %s in %s" % (self.message, self.start, self.end, self.routine.title)
