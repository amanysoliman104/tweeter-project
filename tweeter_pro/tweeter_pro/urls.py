"""tweeter_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url , include
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles import views
from django.conf.urls.static import static
from tweets.views import TweetListView
from hashtags.views import HashTagView
from .views import home
# if i have alot of apps in my pro , i can make for every app ,
# its view file and its templates folder to organize the pro 
##tweets here is the name of the app
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListView.as_view() , name ='home'), # when press home title apear list 
    url(r'^tags/(?P<hashtag>.*)/$', HashTagView.as_view() , name ='hashtag'),
    url(r'^tweet/', include('tweets.urls' , namespace='tweet')), 
    url(r'^', include('acounts.urls' , namespace='profiles')),
    url(r'^api/', include('acounts.api.urls' , namespace='profiles-api')),
    url(r'^api/tweet/', include('tweets.api.urls' , namespace='tweet-api')), 


]
if settings.DEBUG:
	urlpatterns += (static(settings.STATIC_URL,document_root=settings.STATIC_ROOT))