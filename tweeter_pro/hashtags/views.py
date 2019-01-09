# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from .models import HashTag

# Create your views here.

class HashTagView(View):
	def get(self , request , hashtag , *args ,**kwargs):
		obj , Created = HashTag.objects.get_or_create(tag=hashtag)
		return render(request,"hashtags/tag_view.html",{"obj":obj })
     
		