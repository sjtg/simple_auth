# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

#created title of the blog 

class Blog_Boards(models.Model):
	name = models.CharField(max_length=60, unique=True)
	title  = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name


#created a topic class the handles all topics within the blog
class Topic(models.Model):
	title = models.CharField(max_length=255)
	last_uptate = models.DateTimeField(auto_now_add=True)
	board = models.ForeignKey(Blog_Boards,related_name='topics')
	starter = models.ForeignKey(User, related_name='topics') 


#created for posting blog post to the database
class Post(models.Model):
	message = models.TextField(max_length=2000)
	topic = models.ForeignKey(Topic, related_name='posts')
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(null=True)
	created_by = models.ForeignKey(User, related_name='posts')
	update_by = models.ForeignKey(User, null=True, related_name ='+')
