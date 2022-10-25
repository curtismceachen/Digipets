from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime

SPECIES = (
    ('H', 'Huskey'),
    ('C', 'Corgi'),
    ('O', 'Otter')
)

PERSONALITIES = (
    ('T', 'Timid'),
    ('B', 'Brave'),
    ('N', 'Naughty'),
    ('C', 'Calm'),
    ('J', 'Jolly'),
    ('Q', 'Quirky'),
    ('S', 'Sassy')
)

class Digipet(models.Model):
  name = models.CharField(max_length=50)
  species = models.CharField(max_length=10, choices=SPECIES, default=SPECIES[0][0])
  personality = models.CharField(max_length=20, choices=PERSONALITIES, default=PERSONALITIES[0][0])
  image = models.CharField(max_length=250, default = "/static/digipets/assets/animals/corgi/1.svg")
  birthday = models.DateField('Birthday')
  mood = models.CharField(max_length=20, default = 'hungry')
  user = models.ForeignKey(User, on_delete=models.CASCADE)


  def __str__(self):
    return f'{self.name} {self.get_personality_display()}'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'digipet_id': self.id})

  def feed (self):
    self.last_feed = self.get_time()

  def get_time(self):
	  return datetime.datetime.now()

