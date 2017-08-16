from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.

class Task(models.Model):
	title = models.CharField(max_length=140)
	create_time = models.DateTimeField(default=timezone.now)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.title