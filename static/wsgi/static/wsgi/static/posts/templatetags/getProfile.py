from django import template
from profiles.models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

register= template.Library()

@register.filter
def getProfile(user):
	try:
		profile=Profile.objects.get(user=user)
		return profile.id
	except:
		return HttpResponseRedirect('/')