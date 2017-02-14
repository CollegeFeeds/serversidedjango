from django.db import models

# Create your models here.
############################## A Table for various status such as status of change in news headline banners #################
class status(models.Model):
	banner_status=models.TextField(unique=False)

	def __unicode__(self):
		return "Status"
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
	 	return self.ncwebtitle


class ncwebresults(models.Model):
	title=models.TextField(unique=False)
	linkf=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.title

#---------------------------------------------------

#Tables for UndergradResults-----------------------------
class undergradcounters(models.Model):
	undergradid=models.IntegerField(primary_key=True)
	undergradtitle=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.undergradtitle


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
	 	return self.postgradtitle


class postgradresults(models.Model):
	title=models.TextField(unique=False)
	linkf=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.title
#--------------------------------------------------------
#Tables for DiplomaResults-----------------------------
class diplomacounters(models.Model):
	diplomaid=models.IntegerField(primary_key=True)
	diplomatitle=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.diplomatitle


class diplomaresults(models.Model):
	title=models.TextField(unique=False)
	linkf=models.TextField(unique=False)
	def __unicode__(self):
	 	return self.title

#-----------------------------------------------
##################### END OF RESULT MODELS####################


##################### Start Of DuBeat Scrapers ###################
class headlines(models.Model):
	title=models.TextField(unique=False)
	linkf=models.TextField(unique=False)
	imagelink=models.TextField(unique=False,default="null")
	def __unicode__(self):
	 	return self.title

#--------------------------------------------------------------------------
