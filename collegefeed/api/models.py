from django.db import models

# Create your models here.
# A model for Mphil results
class mphilresults(models.Model):
	id=models.AutoField(primary_key=True)
	title=models.TextField(unique=False)
	linkf=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.title

class mphilcounters(models.Model):
	mphilid=models.IntegerField(primary_key=True)
	mphiltitle=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.mphiltitle

