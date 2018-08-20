from django.shortcuts import render
from django.db.models import Q
from review.models import Review
from django.http import HttpResponseRedirect

# Create your views here.
def deleteReview(request,id): #BROKEN NO ATTRIBUTE USER
	review=Review.objects.get(pk=id)
	idNumber=str(review.reviewed.id)
	if review.user!= request.user:
		HttpResponseRedirect('/profiles/'+idNumber+'/')
	Review.objects.filter(Q(id=id)).delete()
	return HttpResponseRedirect('/profiles/'+idNumber+'/')