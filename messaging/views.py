from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render
from messaging.models import Message
from profiles.models import Profile
from messaging.forms import MessageForm
import uuid
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.
@login_required
def sendMessage(request,id):
	currentUser = request.user
	sender=Profile.objects.get(user=currentUser)
	reciever=Profile.objects.get(pk=id)
	first = reciever.user.first_name
	last = reciever.user.last_name
	name = first+' '+last

	sentMessages = Message.objects.filter(sender = sender, reciever = reciever)
	recievedMessages = Message.objects.filter(sender = reciever, reciever = sender)
	messageList = sentMessages.union(recievedMessages).order_by('created')
	if request.method == 'POST':
		form = MessageForm(data=request.POST)
		if form.is_valid():
			created=timezone.now()
			body=form.cleaned_data['body']
			group= uuid.uuid4()
			newMessage=Message(sender = sender, reciever = reciever, body= body, created= created, read = False, group = group )
			newMessage.save()
			return HttpResponseRedirect('/messages/sendMessage/'+str(id)+'/')
	else:
		form = MessageForm()

	return render(request, 'sendMessage.html', {'form': form, 'name':name, 'messageList':messageList })