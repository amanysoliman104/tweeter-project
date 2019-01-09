
from django.conf.urls import url

from django.contrib.staticfiles import views
from django.views.generic.base import RedirectView 
from django.conf.urls.static import static
from .views import (
    RetweetAPIView,
	TweetCreateAPIView,
    TweetListAPIView,
    )

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListAPIView.as_view() , name ='list'), #/api/tweet/
    #url(r'^$', RedirectView.as_view(url="/")),
    url(r'^create/$', TweetCreateAPIView.as_view() , name ='create'),#api/tweet/create/
    url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view() , name ='retweet'), #api/tweet/1/retweet #id write by user 
    #url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view() , name ='update'),#tweet/1/update/
    #url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view() , name ='delete'),#tweet/1/delete/
]
