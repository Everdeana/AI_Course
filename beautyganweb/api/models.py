from django.db import models

# Create your models here.
class RefModels(models.Model):
	names = models.CharField(max_length=100)
	image = models.CharField(max_length=500)
	item = models.CharField(max_length=50)
	shop = models.CharField(max_length=500)
	doc = models.CharField(max_length=500)
	dates = models.CharField(max_length=20)
	
	def __str__(self):
			return self.names	