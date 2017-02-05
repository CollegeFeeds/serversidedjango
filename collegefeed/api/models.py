from django.db import models

# Create your models here.
################### RESULTS ########################################
#Tables for M.phil Results-----------------------------
class mphilcounters(models.Model):
	mphilid=models.IntegerField(primary_key=True)
	mphiltitle=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.mphiltitle


class mphilresults(models.Model):
	title=models.TextField(unique=False)
	linkf=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.title
#---------------------------------------------------------

#Tables for Ncweb Results-----------------------------
class ncwebcounters(models.Model):
	ncwebid=models.IntegerField(primary_key=True)
	ncwebtitle=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.mphiltitle


class ncwebresults(models.Model):
	title=models.TextField(unique=False)
	linkf=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.title

#---------------------------------------------------

#Tables for UndergradResults-----------------------------
class undergradcounters(models.Model):
	undergradid=models.IntegerField(primary_key=True)
	udergradtitle=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.mphiltitle


class undergradresults(models.Model):
	title=models.TextField(unique=False)
	linkf=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.title

#-----------------------------------------------

#Tables for postgradresults-----------------------------
class postgradcounters(models.Model):
	postgradid=models.IntegerField(primary_key=True)
	postgradtitle=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.mphiltitle


class postgradresults(models.Model):
	title=models.TextField(unique=False)
	linkf=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.title
#--------------------------------------------------------
#Tables for DiplomaResults-----------------------------
class diplomacounters(models.Model):
	undergradid=models.IntegerField(primary_key=True)
	udergradtitle=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.mphiltitle


class diplomaresults(models.Model):
	title=models.TextField(unique=False)
	linkf=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.title

#-----------------------------------------------
##################### END OF RESULT MODELS####################

