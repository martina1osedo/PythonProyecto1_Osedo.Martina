from django.shortcuts import render
from .models import Post 


def index2(request):
    index2 = Post.objects.all()
    return render(request, 'Martiapp/index2.html', context={"posts": index2})
