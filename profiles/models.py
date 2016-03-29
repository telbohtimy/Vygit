from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    GENDER_CHOICES = (('M', 'Male'),
                      ('F', 'Female'))

    user = models.OneToOneField(User, editable=False)
    body = models.TextField(max_length=2048, blank=True)
    birthDate = models.DateField('birthDate',null=True, blank=True)
    gender = models.CharField(max_length=1, blank=True, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='media/profile_images', blank=True)
    city=models.CharField(max_length=128,blank=False)
    country=models.CharField(max_length=128,blank=False)
    address=models.CharField(max_length=128,blank=False)
    postalCode=models.CharField(max_length=6,blank=False)
    phoneNumber=models.IntegerField(blank=False)

    def get_image_path(self):
        return self.image.path
    
    def __unicode__(self):
        return str(self.user)
    def __str__(self):
        return str(self.user.username)

class Reviews(models.Model):
    RATINGS=(('0', '0'),
            ('0.5', '0.5'),
            ('1.0', '1.0'),
            ('1.5', '1.5'),
            ('2.0', '2.0'),
            ('2.5', '2.5'),
            ('3.0', '3.0'),
            ('3.5', '3.5'),
            ('4.0', '4.0'),
            ('4.5', '4.5'),
            ('5.0', '5.0'))
    body = models.TextField(max_length=500, blank=True)
    reviewer = models.ForeignKey(User, editable=False,related_name='reviewer')
    reviewed = models.ForeignKey(User, editable=False, related_name='reviewed')
    ratings = models.CharField(max_length=3, blank=False, choices=RATINGS)
    date=models.DateTimeField('date posted')

