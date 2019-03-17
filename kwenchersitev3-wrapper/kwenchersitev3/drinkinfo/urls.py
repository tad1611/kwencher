"""kwenchersitev2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from views import auth_view,location_auto_complete,beer_auto_complete
import views




urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^login/', views.login_page, name='login'),
    url(r'^beers/(?P<BEER_ID>\w+)/$', views.beer_list, name='beers'),
    url(r'^specials/(?P<LOCATION_KEY>\w+)/$', views.special_list, name='specials'), 
    url(r'^addspecials/', views.add_special_hdr, name='addspecials'),
    url(r'^add_posts/', views.add_posts, name='add_posts'),
    url(r'^addlnspecials/', views.add_special_ln, name='addlnspecials'),
    url(
        r'^location-autocomplete/$',
        location_auto_complete.as_view(),
        name='location-autocomplete',
    ),
    url(
        r'^beer-autocomplete/$',
        beer_auto_complete.as_view(),
        name='beer-autocomplete',
    ),
    url(r'^accounts/auth/$', views.auth_view),    #authorize login


]


