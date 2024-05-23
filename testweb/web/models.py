from django.db import models

# Create your models here.

class Test1(models.Model):
	title = models.CharField(max_length=100)
	tel = models.CharField(max_length=100)

	def __str__(self):
		return self.title