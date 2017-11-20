# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import Blog_Boards

# Create your views here.

#home view page
def home(request):
	boards = Blog_Boards.objects.all()
	blog_board_names = list()

	for board in boards:
		blog_boards_names.append(board.name)

	response_html = '<br>'.join(blog_board_names)

	return HttpResponse(response_html)
