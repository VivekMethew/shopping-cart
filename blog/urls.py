from django.urls import path

from . import views

#create blogs urls 

urlpatterns = [
    path('',views.index, name='blogHome'),
    path('blogPost/<int:id>',views.blogPost, name='blogPost'),
] 