from django import template
from profiles.models import Profile
from django.contrib.auth.models import User

register= template.Library()

@register.filter
def getProfile(user):
	profile=Profile.objects.get(user=user)
	return profile.id