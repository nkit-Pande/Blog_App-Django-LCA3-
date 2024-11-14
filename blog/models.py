from django.db import models
class Service(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_name = models.CharField(max_length=100)
    blog_body = models.TextField()

class PersonalInfo(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    
