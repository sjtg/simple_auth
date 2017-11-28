# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login as auth_login

from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect

# Create your views here.

#signup function allows the users to create an account
def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_login(request, user)
			return redirect('home')
	return render(request, 'signup.html', {'form' : form})
