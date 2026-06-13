from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=99,primary_key=True)
    phone=models.IntegerField(max_length=12)
    city=models.CharField(max_length=50)
    password=models.CharField(max_length=30)
    profile_pic=models.FileField(upload_to="user/" ,blank=True)

class Dietitian(models.Model):
    email=models.EmailField(max_length=100,primary_key=True)
    password=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    qualification=models.TextField(max_length=100)
    gender=models.CharField(max_length=30)
    experience=models.CharField(max_length=30)
    skills=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    registration_no=models.CharField(max_length=30)
    profile_pic=models.FileField(upload_to="dietitian/",blank=True)

class Feedback(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=150)
    rating=models.CharField(max_length=30)
    feedback=models.TextField()

class Dietitian_post(models.Model):
    name=models.CharField()
    email=models.EmailField()
    post=models.TextField()

class Contact(models.Model):
    first_name=models.CharField()
    last_name=models.CharField()
    email=models.EmailField()
    role=models.CharField()
    message=models.TextField()
    phone=models.CharField()
