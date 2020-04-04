from django.db import models

# Create your models here.


class Headlines(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(max_length=500,null=True, blank=True)
    url = models.TextField(max_length=500)
    website_name = models.TextField(null=True, blank=True)
    timeStamp = models.TextField(null=True, blank=True)
    websiteIcon = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title

class World(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(max_length=500,null=True, blank=True)
    url = models.TextField(max_length=500)
    website_name = models.TextField(null=True, blank=True)
    timeStamp = models.TextField(null=True, blank=True)
    websiteIcon = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title

class Tech_news(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(max_length=500,null=True, blank=True)
    url = models.TextField(max_length=500)
    website_name = models.TextField(null=True, blank=True)
    timeStamp = models.TextField(null=True, blank=True)
    websiteIcon = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title


class Economy(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(max_length=500,null=True, blank=True)
    url = models.TextField(max_length=500)
    website_name = models.TextField(null=True, blank=True)
    timeStamp = models.TextField(null=True, blank=True)
    websiteIcon = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title

class Sports(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(max_length=500,null=True, blank=True)
    url = models.TextField(max_length=500)
    website_name = models.TextField(null=True, blank=True)
    timeStamp = models.TextField(null=True, blank=True)
    websiteIcon = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title



