from django.views.generic import ListView
from django.shortcuts import render, redirect
from .models import Post 
from .forms import PostForm


def index2(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        index2 = Post.objects.filter(titulo__icontains=busqueda)
    else:    
        index2 = Post.objects.all()
    return render(request, 'Martiapp/index2.html', context={"posts": index2})

class PostListView(ListView):
    model = Post
    template_name = "Martiapp/index2.html"
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda", None)
        if busqueda: 
            queryset = queryset.filter(titulo_icontains=busqueda)
            return QuerySet
                       
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.autor = request.user
                post.save()
                return redirect("Martiapp:index2")
            else: 
                form.add_error(None, "Debes estar logueado para crear una publicacion")
                    
    else:
        form = PostForm()    
    return render(request, "Martiapp/post_create.html", context={"form": form})