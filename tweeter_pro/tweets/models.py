# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re #regular expretion
from django.db.models.signals import post_save
from django.urls import reverse , reverse_lazy
from django.conf import settings
from django.db import models
from .validators import validate_content
from django.utils import timezone
from hashtags.signals import parsed_hashtags
# Create your models here
#use this class to copy every thing of the original tweet , user is the new one
#for comments on my tweet
class TweetManger(models.Manager):
    def retweet(self , user , parent_obj):
        if parent_obj.parent:
            og_parent=parent_obj.parent #og=original
        else:
            og_parent=parent_obj

        #to prevent the retweet that created to create again
        qs=self.get_queryset().filter(
            user=user,parent=og_parent
            ).filter(
            timestamp__year=timezone.now().year,
            timestamp__month=timezone.now().month,
            timestamp__day=timezone.now().day,

            )
        if qs.exists():
            return None

        obj=self.model(
            parent=og_parent,
            user=user,
            content=parent_obj.content,
            )
        obj.save()
        return obj

class Tweet(models.Model):
    parent    =models.ForeignKey("self",blank=True ,null=True)
    user      =models.ForeignKey(settings.AUTH_USER_MODEL)#this argument means that user cannot be null or delete it from form (intgrity error)
    content   =models.CharField(max_length = 140,validators=[validate_content])
    updated   =models.DateTimeField(auto_now=True)
    timestamp =models.DateTimeField(auto_now_add=True)

    objects=TweetManger()
    

    def __str__(self):
        return str(self.content)
     


    def get_absolute_url(self):
        return reverse_lazy("tweet:detail", kwargs={"pk":self.pk}) #when press confirm in create class call detail page ,istade of successurl in createclass

    
    class Meta:
        ordering=['-timestamp']# if i want to rarrange the tweets by timestamp and i do here in model to can use it in another app  




    '''def clean(self,*args ,**kwargs):
        content=self.content
        if content=="abc":
            raise ValidationError("cannot be abc")
        return super(Tweet,self).clean(*args,**kwargs)'''


def tweet_save_reciver(sender,instance,created,*args,**kwargs):
    if created and not instance.parent:
        #notify user
        user_regex=r'@(?P<username>[\w.@+-]+)'
        usernames =re.findall(user_regex,instance.content) #m ,match
        
        #send anotification to user here
        #send hashtag signal to user here
        hash_regex=r'#(?P<hashtag>[\w\d-]+)'
        hashtags=re.findall(hash_regex,instance.content) #m ,match find all hashtags
        parsed_hashtags.send(sender=instance.__class__,hashtag_list=hashtags) #send them  to hashtag app and in hashtag model there are a reciver,,__class__ it refer to class of this instance (datamodel decumentaion)
        



post_save.connect(tweet_save_reciver,sender=Tweet)       


