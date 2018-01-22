from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls import url


urlpatterns = [
    url(r'^', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
