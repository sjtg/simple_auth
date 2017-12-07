from django.contrib.auth.models import User
import django_filters

#from .models import  Blog_Boards

class UserFilter(django_filters.FilterSet):
	class Meta:
		model = User
		fields = ['username',   ]
