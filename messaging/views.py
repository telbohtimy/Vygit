from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render
from messaging.models import Message
from profiles.models import Profile
from django.contrib.auth.models import User
from messaging.forms import MessageForm
import uuid
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q

perPage=5
# Create your views here.
@login_required
def sendMessage(request,id):
	sender=request.user
	reciever=User.objects.get(pk=id)
	first = reciever.first_name
	last = reciever.last_name
	name = first+' '+last

	sentMessages = Message.objects.filter(sender = sender, reciever = reciever)
	recievedMessages = Message.objects.filter(sender = reciever, reciever = sender)
	messageList = sentMessages.union(recievedMessages).order_by('created')[:20]
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

@login_required
def inbox(request):
	# messageList = Message.objects.order_by('sender','reciever','-created').distinct('sender', 'reciever')
	messageList = Message.objects.filter(sender = request.user).values()
	return render(request,'inbox.html', {'messageList': messageList})
