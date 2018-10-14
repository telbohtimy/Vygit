from django.db import models
from profiles.models import Profile
import uuid


# Create your models here.
# Create your models here.
class Message(models.Model):
	sender = models.ForeignKey(Profile, related_name='sender', on_delete=models.CASCADE)
	reciever = models.ForeignKey(Profile, related_name='reciever', on_delete=models.CASCADE)
	body = models.TextField(max_length=1000, blank=True)
	created = models.DateTimeField('date created')
	read = models.BooleanField()
	group = models.UUIDField(default=uuid.uuid4, editable=False)
	def __str__(self):
		return str(self.body)