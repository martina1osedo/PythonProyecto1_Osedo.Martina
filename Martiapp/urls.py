from django.urls import path 

from . import views 

app_name = "Martiapp"

urlpatterns = [
    path("post/list", views.index2, name="index2"),
]
