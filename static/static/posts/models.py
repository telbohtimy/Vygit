from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from profiles.models import Profile
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.
class Post(models.Model):
	CONDITION=(('New','New'),
			('Slightly Used','Slightly Used'),
			('Used', 'Used'),
			('Very Used','Very Used'),
			('Bad','Bad'),
		)
	gameName=models.CharField(max_length=128,blank=False)
	console=models.CharField(max_length=128,blank=False)
	description=models.TextField(max_length=2048)
	author=models.ForeignKey(Profile, on_delete=models.CASCADE)
	date=models.DateTimeField('date posted')
	dateUpdated = models.DateTimeField('date updated', blank = True, null = True)
	condition=models.CharField(max_length=32,choices=CONDITION,blank=False)
	image=models.ImageField(upload_to='media/post_images',blank=True)
	price=models.DecimalField(max_digits=8,decimal_places=2,blank=False, validators=[MinValueValidator(Decimal('0.01'))])

	def get_image_path(self):
		return self.image.path
	def __str__(self):
		return str(self.gameName)