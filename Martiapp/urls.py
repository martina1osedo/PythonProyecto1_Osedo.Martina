from django.urls import path 

from . import views 

app_name = "Martiapp"

urlpatterns = [
   # path("index2", views.index2, name="index2"),
    path("index2", views.PostListView.as_view(), name="post_list"),
    path("post/create", views.post_create, name="post_create"),
    
]
