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
def createMessage(request,id):
	currentUser = request.user
	reciever=Profile.objects.get(pk=id)
	first = reciever.user.first_name
	last = reciever.user.last_name
	name = first+' '+last
	if request.method == 'POST':
		form = MessageForm(data=request.POST)
		if form.is_valid():
			sender=Profile.objects.get(user=currentUser)
			created=timezone.now()
			body=form.cleaned_data['body']
			group= uuid.uuid4()
			newMessage=Message(sender = sender, reciever = reciever, body= body, created= created, read = False, group = group )
			newMessage.save()
			return HttpResponseRedirect('/profiles/'+str(id)+'/')
	else:
		form = MessageForm()

	return render(request, 'createMessage.html', {'form': form, 'name':name })