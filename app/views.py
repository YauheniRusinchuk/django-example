from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView
from django.views.decorators.http import require_http_methods
from .models import Post, Comment
from django.contrib.auth.models import User
from .forms import FormComments
# Create your views here.


class Index(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'app/home.html'


@require_http_methods(['GET', 'POST'])
def detail_post_view(request,pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    form = FormComments()
    context = {'post': post, 'form' : form, 'comments': comments}
    if request.method == "POST":
        com = request.POST.get('comment')
        new_comment = Comment(text=com, post=post)
        new_comment.save()
        return HttpResponseRedirect('/posts/{}'.format(pk))
    return render(request, 'app/detail.html', context)



def search(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
    post = Post.objects.filter(title__istartswith=search_text)[:]
    return render(request, 'app/search.html', {'result' : post})


class AboutView(TemplateView):
    template_name = 'app/about.html'
