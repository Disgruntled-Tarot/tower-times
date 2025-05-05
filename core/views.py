from django.shortcuts import render
from .models import BlogPost
from django.shortcuts import get_object_or_404

def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, 'core/post_detail.html', {'post': post})

def home(request):
    return render(request, 'core/index.html')

def reading_table(request):
    return render(request, 'core/reading_table.html')

def veil(request):
    return render(request, 'core/veil.html')

def tools(request):
    return render(request, 'core/tools.html')

def messages(request):
    return render(request, 'core/messages.html')

def reading_table(request):
    posts = BlogPost.objects.filter(published=True).order_by('-created_at')
    return render(request, 'core/reading_table.html', {'posts': posts})

def veil(request):
    return render(request, 'core/veil.html')