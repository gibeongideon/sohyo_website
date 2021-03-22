
from django.urls import path  #,re_path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    # re_path(r'^.*\.html', views.pages, name='pages'),

    path('', views.index, name='index'),
    path('causes', views.causes, name='causes'),
    path('about', views.about, name='about'),
    path('events', views.events, name='events'),
    path('blogs', views.blogs, name='blogs'),
    path('contact', views.contact, name='contact'),
    path('join_us', views.join_us, name='join_us'),
    path('members', views.members, name='members'),


] 
