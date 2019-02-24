# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render , get_object_or_404 ,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.views import View
from django.views.generic import DetailView
from .models import UserProfile
from django.views.generic.edit import FormView
from .forms import UserRegisterForm

# Create your views here.
User=get_user_model()

class UserRegisterView(FormView):
    template_name='acounts/user_register_form.html'
    form_class=UserRegisterForm
    success_url='/login'


    def form_valid(self, form):
        username=form.cleaned_data.get("username")
        email=form.cleaned_data.get("email")
        password=form.cleaned_data.get("password")
        new_user=User.objects.create(username=username,email=email)
        new_user.set_password(password)
        new_user.save()
        return super(UserRegisterView,self).form_valid(form)


class UserDetailView(DetailView):
    template_name='acounts/user_detail.html'
    queryset=User.objects.all()


    def get_object(self):
        return get_object_or_404(User,username__iexact=self.kwargs.get("username"))#kwargs catch username that in url (?P<username>[\w.@+-]+)\

    def get_context_data(self,*args,**kwargs):
        context=super(UserDetailView,self).get_context_data(*args,**kwargs)
        following=UserProfile.objects.is_following(self.request.user ,self.get_object())
        context['following']= following
        context['recommended']=UserProfile.objects.recommended(self.request.user)
        return context

#when any one do follow to me ,it add to my followers (followed_by)
class UserFollowView(View):
    def get(self,request , username,*args,**kwargs):
        toggle_user=get_object_or_404(User,username__iexact=username)
        if request.user.is_authenticated():
            is_following=UserProfile.objects.toggle_follow(request.user,toggle_user)
        return redirect("profiles:detail" , username=username)
        # the redirect fun shourtcuts those line __>
        #url=reverse("profiles:detail" , kwargs={"username":username})
        #return HttpResponseRedirect(url)