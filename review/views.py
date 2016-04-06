from django.shortcuts import render
from django.db.models import Q
from review.models import Review
from django.http import HttpResponseRedirect

# Create your views here.
def deleteReview(request,id):
	#Add an assert statement to make sure user and review author are the same
	review=Review.objects.get(pk=id)
	idNumber=str(review.reviewed.id)
	Review.objects.filter(Q(id=id)).delete()
	return HttpResponseRedirect('/profiles/'+idNumber+'/')