# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Blog_Boards

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
	return render(request, 'new_topics.html', {'board' : board })

