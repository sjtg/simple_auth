# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.shortcuts import render, redirect,  get_object_or_404

from .forms import NewTopicForm

from .models import Blog_Boards, Topic, Post

# Create your views here.

#home view page
def home(request):
	boards = Blog_Boards.objects.all()
    	return render(request, 'home.html', {'boards': boards})

#created topics function to list the topics within the board
def topics(request, pk):
	board = get_object_or_404(Blog_Boards, pk=pk)
	return render(request, 'topics.html', {'board':board})
	

#created new topic function, this will show  new topics in the dashboard 
def new_topics(request, pk):
	board = get_object_or_404(Blog_Boards, pk=pk)
	user = User.objects.first()

	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.board = board
			topic.starter = user
			topic.save()
			post = Post.objects.create(
				message = form.cleaned_date.get('message'),
				topic = topic,
				created_by = user
			)

			return redirect('topics', pk=board.pk)
	else:
		form = NewTopicForm()	

	return render(request, 'new_topics.html', {'board' : board, 'form':form })

