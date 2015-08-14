from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

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

    def associated_decks(self):
        decks = []
        for deck in self.decks.all():
            decks.append((deck.name, str(GroupDeck.objects.get(group = self, deck = deck).deadline)[:-9], str(GroupDeck.objects.get(group = self, deck = deck).weight), deck.pk)) #tuple (name, deadline, weight, pk)
        return decks

class UserGroup(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    ROLE_CHOICES = (
        ('1', 'teacher'), 
        ('2', 'student'))
    role = models.CharField(max_length = 1, choices = ROLE_CHOICES)

    def __unicode__(self):
        return "%s: %s (%s)" % (self.user, self.group, self.role)

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
    deck = models.ForeignKey(Deck)
    interval = models.IntegerField(default = 1440) #in minutes, 1440 = one day
    due = models.DateTimeField(default = datetime.now)
    ease_factor = models.FloatField(default = 2.50)
    LEARNING_STATE_CHOICES = (
        ('1', 'learning'), 
        ('2', 'relearning'), 
        ('3', 'acquired'))
    learning_state = models.CharField(max_length = 1, choices = LEARNING_STATE_CHOICES, default = '1')

    def __unicode__(self):
        return "%s: %s" % (self.user.username, self.card.front)