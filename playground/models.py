from django.db import models
from django.utils import timezone

# Create your models here.
#Models in Django  ---> Table ----> Sheets

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=225)
    content = models.TextField( )
    author = models.CharField(max_length=13)
    slug = models.CharField(max_length=130)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + 'by' + self.author
    
class carbooking(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    srno = models.IntegerField(default=0)
    days = models.IntegerField()
    phone = models.CharField(max_length=13)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class hotelbooking(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    srno = models.IntegerField(default=0)
    night = models.IntegerField()
    phone = models.CharField(max_length=13)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
class tourbooking(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    person = models.IntegerField()
    srno = models.IntegerField(default=0)
    phone = models.CharField(max_length=13)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
