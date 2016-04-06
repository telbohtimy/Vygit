from django.db import models
from profiles.models import Profile

# Create your models here.
class Review(models.Model):
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
    reviewer = models.ForeignKey(Profile, related_name='reviewer')
    reviewed = models.ForeignKey(Profile, related_name='reviewed')
    ratings = models.CharField(max_length=3, blank=False, choices=RATINGS)
    date=models.DateTimeField('date posted')