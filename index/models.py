from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    teacher_id = models.CharField(max_length = 64) #register as teacher then choose a teacher_id, that will be the url students use to sign up for classes
    ###extension### teacher_id is built from first_name and last_name, with number added if not unique
    student_id = models.CharField(max_length = 64) #if registering as student, need to enter student_id (edX uses the username)
    ###extension### add timezone support

    def __unicode__(self):
        return self.user.username

class Deck(models.Model):
    name = models.CharField(max_length = 256, unique = True)

    def __unicode__(self):
        return self.name

class Group(models.Model): #'Groups' == classes
    name = models.CharField(max_length = 256)
    decks = models.ManyToManyField(Deck, through = 'GroupDeck')
    users = models.ManyToManyField(User, through = 'UserGroup')

    def __unicode__(self):
        return self.name

class UserGroup(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    ROLE_CHOICES = (
        ('1', 'teacher'), 
        ('2', 'student'))
    role = models.CharField(max_length = 1, choices = ROLE_CHOICES)

    def __unicode__(self):
        return "%s: %s" % (self.user, self.group)

class GroupDeck(models.Model):
    group = models.ForeignKey(Group)
    deck = models.ForeignKey(Deck)
    deadline = models.DateTimeField()
    weight = models.IntegerField() #in percentages, weights for all GroupDecks associated with a Group must add to 100

    def __unicode__(self):
        return "%s: %s" % (self.group, self.deck)

class Card(models.Model):
    front = models.TextField()
    front_additional = models.TextField(null = True)
    back = models.TextField()
    back_additional = models.TextField(null = True)
    example = models.TextField(null = True)
    deck = models.ForeignKey(Deck)
    students = models.ManyToManyField(User, through = 'StudentCard')

    def __unicode__(self):
        return "%s / %s" % (self.front, self.back)

class StudentCard(models.Model):
    user = models.ForeignKey(User)
    card = models.ForeignKey(Card)
    interval = models.IntegerField() #in minutes
    ease_factor = models.FloatField() #base ease_factor 1.00
    LEARNING_STATE_CHOICES = (
        ('1', 'learning'), 
        ('2', 'relearning'), 
        ('3', 'acquired'))
    learning_state = models.CharField(max_length = 1, choices = LEARNING_STATE_CHOICES, default = 1)

    def __unicode__(self):
        return "%s: %s" % (self.user, self.card)