from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'guestbook/index.html', {})

def addcomments(request):
	return render(request, 'guestbook/addcomments.html', {})
