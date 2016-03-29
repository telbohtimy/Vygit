from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Post
from posts.forms import postForm, editForm
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
import re


# Create your views here.
def index(request):
	latestGameList = Post.objects.order_by('-date')[:5]
	context={'latestGameList': latestGameList}
	return render(request,'index.html', context)

def gamePage(request, id):
	try:
		gamePage=Post.objects.get(pk=id)
		if gamePage.image:
			scale=scaleImage(500, gamePage.image.width)
			width=scale*gamePage.image.width
			height=scale*gamePage.image.height
		else:
			width=0
			height=0
	except Post.DoesNotExist:
		raise Http404("This post does not exist")
	return render(request,"details.html",{"gamePage":gamePage,'width':width,'height':height})

@login_required
def posts(request):#Add a price

	if request.method == 'POST':
		form = postForm(data=request.POST)
		if form.is_valid():
			gameName=form.cleaned_data['gameName']
			condition=form.cleaned_data['condition']
			date=timezone.now()
			description=form.cleaned_data['description']
			console=form.cleaned_data['console']
			price=form.cleaned_data['price']
			currentUser=request.user
			author=Profile.objects.get(user=currentUser)
			try:
				image = request.FILES['image']
			except:
				image=""
			newPost=Post(gameName=gameName,description=description,console=console,condition=condition,date=date,author=author,price=price,image=image)
			newPost.save()
			return HttpResponseRedirect('/posts/')
	else:

		form = postForm()

	return render(request, 'postForm.html', {'form': form})

def myPosts(request,id):
	try:
		profile=Profile.objects.get(pk=id)
		latestGameList = Post.objects.filter(Q(author=profile)).order_by('-date')
		context={'latestGameList': latestGameList}
	except Profile.DoesNotExist:
		raise Http404("This profile does not exist")
	return render(request,'index.html', context)

@login_required
def editPost(request,id):
	try:
		post=Post.objects.get(pk=id)
		profile=Profile.objects.get(user=request.user)
		if post.image:
			scale=scaleImage(200, post.image.width)
			width=scale*post.image.width
			height=scale*post.image.height
		else:
			width=0
			height=0
		if(post.author!=profile):
			return HttpResponseRedirect('/posts/')
		if request.method == 'POST':
			form = editForm(instance=post,data=request.POST)
			if form.is_valid():
				post.gameName=form.cleaned_data['gameName']
				post.condition=form.cleaned_data['condition']
				post.description=form.cleaned_data['description']
				post.console=form.cleaned_data['console']
				post.price=form.cleaned_data['price']
				newclear = request.POST.get('clear')
				try:
					image = request.FILES['image']
					post.image=image
				except:
					if (post.image == None):
						post.image=""
					elif (newclear == "on"):
						post.image=""
						
				post.save()
				return HttpResponseRedirect('/posts/')
		else:
			form = editForm(instance=post)
	except Post.DoesNotExist:
		raise Http404("This post does not exist")


	return render(request, 'postForm.html', {'form': form,'edit':'edit','post':post,'width':width,'height':height})

def scaleImage(factor, width):
    scale=int(width/factor)
    return 1/scale

def normalize_query(query_string, findterms=re.compile(r'"([^"]+)"|(\S+)').findall,normspace=re.compile(r'\s{2,}').sub):
	return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def search(request):
    query_string = ''
    latestGameList = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        entry_query = get_query(query_string, ['description', 'gameName',])
        
        latestGameList = Post.objects.filter(entry_query).order_by('-date')
    else:
    	query_string="failed"
    context={ 'query_string': query_string, 'latestGameList': latestGameList}
    return render(request,'index.html', context)
def deletePost(request,id):
	 Post.objects.filter(Q(id=id)).delete()
	 return HttpResponseRedirect('/')