from django import template
from messaging.models import Message
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

register= template.Library()

@register.filter
def getMessage(user):
	messageList = Message.objects.filter(reciever = user, read = False)
	if messageList:
		return True
	return False
