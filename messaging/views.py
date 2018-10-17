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
from django.db.models import Avg, Max, Min

perPage=5
# Create your views here.
@login_required
def sendMessage(request,id):
	sender=request.user
	reciever=User.objects.get(pk=id)
	first = reciever.first_name
	last = reciever.last_name
	name = first+' '+last

	Message.objects.filter(sender = reciever, reciever = sender).update(read= True)
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
	messageList = []
	sentList = Message.objects.filter(sender = request.user).values("reciever").distinct()
	recievedList = Message.objects.filter(reciever = request.user).values("sender").distinct()
	ids = sentList.union(recievedList)
	userList = User.objects.filter(id__in=ids)
	for user in userList.all():
		sentMessages = Message.objects.filter(sender = request.user, reciever = user)
		recievedMessages = Message.objects.filter(sender = user, reciever = request.user)
		messageList.append(sentMessages.union(recievedMessages).order_by('-created')[0])
	return render(request,'inbox.html', {'messageList': messageList})
