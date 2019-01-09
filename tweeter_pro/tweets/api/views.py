from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from .serializers import TweetModelSerializer
from .pagination import StandardResultsPagination 
from rest_framework.views import APIView
from rest_framework.response import Response
from tweets.models import Tweet


class RetweetAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,pk,format=None):
        tweet_qs =Tweet.objects.filter(pk=pk)
        message="Not allowed"
        if tweet_qs.exists() and tweet_qs.count()==1:
            #if request.user.is_authenticated():
            new_tweet=Tweet.objects.retweet(request.user ,tweet_qs.first())
            if new_tweet is not None:
                data =TweetModelSerializer(new_tweet).data
                return Response(data)
            message="cannot retweet the same in 1 day"
        return Response({"message":message},status=400)

        


class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class=TweetModelSerializer
    permission_classes=[permissions.IsAuthenticated] #to make sure that the user log in 


    def perform_create(self,serializer): #to handle id for create post
        serializer.save(user=self.request.user) 


class TweetListAPIView(generics.ListAPIView):
    serializer_class=TweetModelSerializer 
    pagination_class=StandardResultsPagination
    
    def get_queryset(self,*args,**kwargs):
        #.profile here come from jason formate
         
        requested_user=self.kwargs.get("username")
        #tweets of the user himself if i write his name in url
        if requested_user:
            qs=Tweet.objects.filter(user__username=requested_user).order_by("-timestamp")   #combine two queryset
        else:
            #all tweets of user that log in now and his followers posts
            im_following=self.request.user.profile.get_following()# give me i follow them to see thier posts
            qs1=Tweet.objects.filter(user__in=im_following)    #tweets of who i follow
            qs2=Tweet.objects.filter(user=self.request.user)   #my tweets
            qs=(qs1 | qs2).distinct().order_by("-timestamp")   #combine two queryset
            print (self.request.GET)

        query = self.request.GET.get("q",None)
        if query is not None:
            qs=qs.filter(Q(content__icontains=query)|Q(user__username__icontains=query)) # Q here to i can search with the username and the content ,but if i delete it i will search with content only
        return qs

        