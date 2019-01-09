# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin   #if i want to force the user to log in 
from django.urls import reverse_lazy ,reverse
from django.shortcuts import render ,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.db.models import Q
from django.views.generic import( 
    CreateView,
    UpdateView,
    DetailView, 
    ListView  , 
    DeleteView
    )
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin ,UserOwnerMixin
from django.shortcuts import render ,get_object_or_404
from .models import Tweet

class RetweetView(View):
    def get(self ,request,pk,*args,**kwargs):
        tweet =get_object_or_404(Tweet,pk=pk)
        if request.user.is_authenticated():
            new_tweet=Tweet.objects.retweet(request.user ,tweet)
            return HttpResponseRedirect("/")
        return HttpResponseRedirect(tweet.get_absolute_url())

class TweetCreateView(FormUserNeededMixin,CreateView):# but ***** but LoginRequiredMixin  here and no comment login url 
    form_class   =TweetModelForm
    template_name="tweets/create_view.html"
   # success_url  =r to make url after create tweetcontent and press tweet submit

    #login_url="/admin/"
    #to make sure that the user logged in 
    

class TweetUpdateView(LoginRequiredMixin,UserOwnerMixin,UpdateView):
    queryset     =Tweet.objects.all()
    form_class   =TweetModelForm
    template_name="tweets/update_view.html"
    success_url  ="/tweet/"



class TweetDetailView(DetailView):
    queryset=Tweet.objects.all()

    '''def get_object(self):
        print (self.kwargs)
        pk = self.kwargs.get("pk")
        return Tweet.objects.get(id=pk)'''


class TweetListView(ListView):

    def get_queryset(self,*args,**kwargs):
        qs=queryset=Tweet.objects.all()
        query = self.request.GET.get("q",None)
        if query is not None:
            qs=qs.filter(Q(content__icontains=query)|Q(user__username__icontains=query)) # Q here to i can search with the username and the content ,but if i delete it i will search with content only
        return qs



        
    def get_context_data(self,*args,**kwargs):
        context=super(TweetListView,self).get_context_data(*args,**kwargs)
        context['create_form']=TweetModelForm()
        context['create_url'] =reverse_lazy("tweet:create")
        return context


class TweetDeleteView(LoginRequiredMixin,DeleteView):
    model=Tweet
    template_name="tweets/delete_confirm.html"
    context_object_name='name' #if i want to change the objectname that created by default in class to use it in the template
    success_url=reverse_lazy("tweet:list")







'''def tweet_detail_views(request , id=1):
    obj_of_detail=Tweet.objects.get(id=id) #we use objects to get data from database
    print(obj_of_detail)
    context ={
        "object_detail" : obj_of_detail
    }
    return render(request,"tweets/detail_view.html",context)

def tweet_list_views(request):
    obj_of_list  =Tweet.objects.all()
    for obj in obj_of_list:
        print(obj.content)
    context ={
        "object_list" : obj_of_list
    }
    return render(request,"tweets/list_view.html",context)'''
    
    