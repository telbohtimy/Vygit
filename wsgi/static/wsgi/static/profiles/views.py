from django.shortcuts import render,render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.models import User
from profiles.forms import UserForm, ProfileForm, EditProfile, EditUser
from profiles.models import Profile
from review.models import Review
from review.forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.db.models import Q
from django.utils import timezone

# Create your views here.
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            #if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')
        #else:
            #return HttpResponse("This user has not been enabled by the admin yet.<br/><a href=\"/login/\">Login</a>")
        else:
            return render(request, 'login.html', {"error_message":"error_message"})
    else:
        return render(request, 'login.html', {},  RequestContext(request))

def register(request):
    '''
    TO DO:
    Authenticate email
    '''
    if request.method == 'POST':
        formUser = UserForm(data=request.POST)
        formProfile=ProfileForm(data=request.POST)
        if formUser.is_valid() and formProfile.is_valid():
            password1=formUser.cleaned_data['password']
            password2=request.POST.get('password2')
            first_name=formUser.cleaned_data['first_name']
            last_name=formUser.cleaned_data['last_name']
            email=formUser.cleaned_data['email']
            if(password1!=password2):
                return render(request, 'register.html', {'formUser': formUser, 'formProfile':formProfile,'passwordError':'passwordError'})
            if User.objects.filter(username = email).exists():
                return render(request, 'register.html', {'formUser': formUser, 'formProfile':formProfile, 'error_message':'error_message'})
            user = formUser.save()
            user.set_password(user.password)
            user.is_active = False
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=email
    
            body=formProfile.cleaned_data['body']
            birthDate=formProfile.cleaned_data['birthDate']
            gender=formProfile.cleaned_data['gender']
            city=formProfile.cleaned_data['city']
            country=formProfile.cleaned_data['country']
            address=formProfile.cleaned_data['address']
            postalCode=formProfile.cleaned_data['postalCode']
            phoneNumber=formProfile.cleaned_data['phoneNumber']
            try:
                image = request.FILES['image']
            except:
                image=""
            user.save()
            newProfile=Profile(user=user,body=body,birthDate=birthDate,gender=gender,city=city,address=address,postalCode=postalCode,phoneNumber=phoneNumber,country=country,image=image)
            newProfile.save()
            return HttpResponseRedirect('/profiles/login')
    else:
        formUser = UserForm()
        formProfile=ProfileForm()
    return render(request, 'register.html', {'formUser': formUser, 'formProfile':formProfile})


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')

def authorPage(request, id):
    try:
        authorPage=Profile.objects.get(pk=id)
        if authorPage.image:
            scale=scaleImage(400, authorPage.image.height)
            width=scale*authorPage.image.width
            height=scale*authorPage.image.height
        else:
            width=0
            height=0
        ReviewList = Review.objects.filter(Q(reviewed=authorPage)).order_by('-date')
        reviewed=authorPage
        flag=''
        if request.user.is_authenticated():
            reviewer=Profile.objects.get(user=request.user)
            if Review.objects.filter(reviewer = reviewer).filter(reviewed=reviewed).exists():
                flag='flag'
        if request.method=='POST':
            if reviewer==reviewed:
                return HttpResponseRedirect('/profiles/'+str(id)+'/')
            reviewForm=ReviewForm(data=request.POST)
            if reviewForm.is_valid():
                body=reviewForm.cleaned_data['body']
                rating=reviewForm.cleaned_data['ratings']
                date=timezone.now()
                newReview=Review(reviewer=reviewer,reviewed=reviewed,body=body,ratings=rating,date=date)
                newReview.save()
        else:
            reviewForm=ReviewForm()
    except Profile.DoesNotExist:
        raise Http404("This profile does not exist")
    return render(request,"author.html",{"authorPage":authorPage,'reviewForm': reviewForm, 'ReviewList':ReviewList,'width':width,'height':height,'flag':flag})


@login_required
def editProfile(request,id):
    try:
        profile=Profile.objects.get(pk=id)
        currentUser=profile.user
        if profile.image:
            scale=scaleImage(200, profile.image.width)
            width=scale*profile.image.width
            height=scale*profile.image.height
        else:
            width=0
            height=0
        if(currentUser!=request.user):
            return HttpResponseRedirect('/')
        if request.method == 'POST':
            formProfile=EditProfile(instance=profile,data=request.POST)
            formUser = EditUser(instance=currentUser,data=request.POST)
            if formUser.is_valid() and formProfile.is_valid():
                profile.user.first_name=formUser.cleaned_data['first_name']
                profile.user.last_name=formUser.cleaned_data['last_name']
                profile.body=formProfile.cleaned_data['body']
                profile.birthDate=formProfile.cleaned_data['birthDate']
                profile.gender=formProfile.cleaned_data['gender']
                profile.city=formProfile.cleaned_data['city']
                profile.country=formProfile.cleaned_data['country']
                profile.address=formProfile.cleaned_data['address']
                profile.postalCode=formProfile.cleaned_data['postalCode']
                profile.phoneNumber=formProfile.cleaned_data['phoneNumber']
                newclear = request.POST.get('clear')
                try:
                    image = request.FILES['image']
                    profile.image=image
                except:
                    if (profile.image == None):
                        profile.image=""
                    elif (newclear == "on"):
                        profile.image=""
                profile.user.save()
                profile.save()
                return HttpResponseRedirect('/profiles/'+str(id)+'/')
        else:
            formProfile=EditProfile(instance=profile)
            formUser = EditUser(instance=currentUser)
    except Profile.DoesNotExist:
        raise Http404("This profile does not exist")
    return render(request, 'register.html', {'formUser': formUser, 'formProfile':formProfile,'edit':'edit','profile':profile,'width':width,'height':height})


def scaleImage(factor, width):
    scale=int(width/factor)
    if scale==0:
        return 1
    return 1/scale

def aboutView(request):
   return render_to_response('about.html')