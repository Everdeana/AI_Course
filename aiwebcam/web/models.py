from django.db import models

# Create your models here.
class WebUser(models.Model):
	names = models.CharField(max_length=40)
	telnos = models.CharField(max_length=50)
	
	def __str__(self):
		return self.names