# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db.models.signals import post_save
from django.db import models
from django.urls import reverse_lazy

# Create your models here.
#make this class to prevent the user to follow himself
class UserProfileManger(models.Manager):
    use_for_related_fields=True

    def all(self):
        qs=self.get_queryset().all()
        #print (dir(self)) #get all fun in this class
        #print(self.instance) # get the user who owen this profile
        try:
            if(self.instance):
                qs=qs.exclude(user=self.instance)
        except:
            pass        
        return qs

     
    def toggle_follow(self,user,to_toggle_user):
        user_profile,created=UserProfile.objects.get_or_create(user=user) # return (user_obj , true)
        if to_toggle_user in user_profile.following.all():
            user_profile.following.remove(to_toggle_user)
            added=False
        else:
            user_profile.following.add(to_toggle_user)
            added=True
        return added

    #get_or_create return false if the user already exist 
    def is_following(self , user , followed_by_user):
        user_profile,created=UserProfile.objects.get_or_create(user=user)
        if created:
            return False
        if followed_by_user in user_profile.following.all():
            return True
        return False



class UserProfile(models.Model):
    user =models.OneToOneField(settings.AUTH_USER_MODEL,related_name='profile') #user.profile
    following =models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='followed_by') 
    #user.profile.following --users i follow
    #user.followrd_by --users that follow me
    objects=UserProfileManger() # userprofile.objects.all
    #abc=UserProfileManger() # userprofile.abc.all 

    def __str__(self):
        return str(self.following.all().count())
    
    def get_following(self): #get who i follow them
        users=self.following.all() #user.objects.all.exclude(username=self.user.username)
        return users.exclude(username=self.user.username)

    def get_follow_url(self):
        return reverse_lazy("profiles:follow" ,kwargs={"username":self.user.username})

    def get_absolute_url(self):
        return reverse_lazy("profiles:detail" , kwargs={"username":self.user.username})


#to save the user data , like this code
#user(amany)=User.objects.frist()
#amany.save()

def post_save_user_reciver(sender,instance,created,*args,**kwargs):
    print(instance) 
    if created:
        new_profile=UserProfile.objects.get_or_create(user=instance)


post_save.connect(post_save_user_reciver,sender=settings.AUTH_USER_MODEL)