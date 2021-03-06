
from django.conf.urls import url , include

from django.contrib.staticfiles import views
from django.views.generic.base import RedirectView 
from django.conf.urls.static import static
from .views import (
    UserDetailView,
    UserFollowView
    )

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^search/$', TweetListView.as_view() , name ='list'), #tweet/
    #url(r'^$', RedirectView.as_view(url="/"))
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view() , name ='detail'), #tweet/1/ #id write by user
    url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view() , name ='follow'), 
    #url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view() , name ='update'),#tweet/1/update/
    #url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view() , name ='delete'),#tweet/1/delete/
]
