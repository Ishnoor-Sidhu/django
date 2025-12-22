from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50)
    phone_no = models.IntegerField(max_length=10)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=100)
    
    img=models.ImageField(upload_to='contact_images/', null=True, blank=True)


    def __str__(self):
        return self.full_name   
    
class Registeration(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username