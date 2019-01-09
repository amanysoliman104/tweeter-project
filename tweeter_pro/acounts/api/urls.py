
from django.conf.urls import url
from django.contrib.staticfiles import views
from django.views.generic.base import RedirectView 
from django.conf.urls.static import static
from tweets.api.views import (
    TweetListAPIView,
    )

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^(?P<username>[\w.@+-]+)/tweet/$', TweetListAPIView.as_view() , name ='list'), #/api/username/tweet/
    
]
