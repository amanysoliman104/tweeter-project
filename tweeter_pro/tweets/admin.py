# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .forms import TweetModelForm

from .models import Tweet
# Register your models here
class TweetModelAdmin(admin.ModelAdmin):
	class Meta:
		model=Tweet
	#form =TweetModelForm

admin.site.register(Tweet,TweetModelAdmin)


