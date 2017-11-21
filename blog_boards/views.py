# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import Blog_Boards

# Create your views here.

#home view page
def home(request):
	boards = Blog_Boards.objects.all()
    	return render(request, 'home.html', {'boards': boards})
