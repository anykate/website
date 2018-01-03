from django.shortcuts import render
from .models import Comment
from .forms import CommentForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
	comments = Comment.objects.order_by('-date_created')
	return render(request, 'guestbook/index.html', {'comments':comments})

def addcomments(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			new_comment = Comment(name=request.POST['name'], comment = request.POST['comment'])
			new_comment.save()
			return redirect('guestbook:index')

	else:
		form = CommentForm()

	return render(request, 'guestbook/addcomments.html', {'form':form})
