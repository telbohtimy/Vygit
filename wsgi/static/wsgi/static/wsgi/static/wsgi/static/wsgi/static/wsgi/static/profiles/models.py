from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    GENDER_CHOICES = (('M', 'Male'),
                      ('F', 'Female'))

    user = models.OneToOneField(User, editable=False, on_delete=models.CASCADE)
    body = models.TextField(max_length=2048, blank=True)
    birthDate = models.DateField('birthDate',null=True, blank=False)
    gender = models.CharField(max_length=1, blank=False, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='media/profile_images', blank=True)
    city=models.CharField(max_length=128,blank=False)
    country=models.CharField(max_length=128,blank=False)
    address=models.CharField(max_length=128,blank=False)
    postalCode=models.CharField(max_length=7,blank=False)
    phoneNumber=models.CharField(max_length=30,blank=False)

    def get_image_path(self):
        return self.image.path
    
    def __unicode__(self):
        return str(self.user)
    def __str__(self):
        return str(self.user.username)


