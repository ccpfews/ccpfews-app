from django.urls import path

from .views import BlogDetails, BlogPost

urlpatterns = [
    path('', BlogPost.as_view(), name='blog_listings'),
    path('<slug:slug>/details/', BlogDetails.as_view(), name='blog_details'),
]
