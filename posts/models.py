from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from profiles.models import Profile
# Create your models here.
class Post(models.Model):
	CONDITION=(('New','New'),
			('Slightly Used','Slightly Used'),
			('Used', 'Used'),
			('Very Used','Very Used'),
			('Bad','Bad'),
		)
	gameName=models.CharField(max_length=128,blank=False)
	console=models.CharField(max_length=128,blank=True)
	description=models.TextField(max_length=2048)
	author=models.ForeignKey(Profile)
	date=models.DateTimeField('date posted')
	condition=models.CharField(max_length=32,choices=CONDITION)
	image=models.ImageField(upload_to='media/post_images',blank=True)
	price=models.IntegerField(blank=False)

	def get_image_path(self):
		return self.image.path
	def __str__(self):
		return str(self.gameName)