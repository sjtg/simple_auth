# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect,  get_object_or_404

from .forms import NewTopicForm, PostForm

from .models import Blog_Boards, Topic, Post

from django.db.models import Count

from .filters import UserFilter

# Create your views here.

#home view page
def home(request):
	boards = Blog_Boards.objects.all()
    	return render(request, 'home.html', {'boards': boards})

#created topics function to list the topics within the board
def topics(request, pk):
	board = get_object_or_404(Blog_Boards, pk=pk)
	topics = board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
	return render(request, 'topics.html', {'board':board, 'topics' : topics})


#created new topic function, this will show  new topics in the dashboard
@login_required
def new_topics(request, pk):
	board = get_object_or_404(Blog_Boards, pk=pk)
	#user = User.objects.first()

	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.board = board
			topic.starter = request.user
			topic.save()
			Post.objects.create(
				message = form.cleaned_data.get('message'),
				topic = topic,
				created_by = request.user
			)

			return redirect('topic_posts', pk=pk, topic_pk=topic.pk)
	else:
		form = NewTopicForm()

	return render(request, 'new_topics.html', {'board' : board, 'form':form })


def topic_posts(request, pk, topic_pk):
	topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
	topic.views += 1
	topic.save()
	return render(request, 'topic_posts.html', {'topic' : topic})


@login_required
def reply_topic(request, pk, topic_pk):
	topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.topic = topic
			post.created_by = request.user
			post.save()
			return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
	else:
		form = PostForm()
	return render(request, 'reply_topic.html', {'topic' : topic, 'form':form})


#created a search function 
def search(request):
	user_list = User.objects.all()
	user_filter = UserFilter(request.GET, queryset=user_list)
	return render(request, 'user_list.html', {'filter': user_filter})
