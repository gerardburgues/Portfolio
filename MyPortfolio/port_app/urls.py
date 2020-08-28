from django.conf.urls import urls
from django.urls import path
from . import views

app_name = 'port_app'

urlpatterns = [

path('',views.ListProjects.as_view(),name='list_projects'),


]
