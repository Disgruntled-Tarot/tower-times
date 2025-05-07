from django.shortcuts import render
from .models import BlogPost
from django.shortcuts import get_object_or_404
from .models import NarrativePrediction

def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, 'core/post_detail.html', {'post': post})

def home(request):
    return render(request, 'core/index.html')

def veil(request):
    return render(request, 'core/veil.html')

def tools(request):
    return render(request, 'core/tools.html')

def messages(request):
    return render(request, 'core/messages.html')

def reading_table(request):
    posts = BlogPost.objects.filter(published=True).order_by('-created_at')
    return render(request, 'core/reading_table.html', {'exposes': exposes})

def displayed_view(request):
    predictions = NarrativePrediction.objects.filter(narrative_type='displayed').order_by('-added_on')
    return render(request, 'narratives/displayed.html', {'predictions': predictions})

def hidden_view(request):
    predictions = NarrativePrediction.objects.filter(narrative_type='hidden').order_by('-added_on')
    return render(request, 'narratives/hidden.html', {'predictions': predictions})

def exposes(request):
    exposes = BlogPost.objects.filter(published=True).order_by('-created_at')
    return render(request, 'core/exposes.html', {'exposes': exposes})

def expose_detail(request, slug):
    expose = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'core/expose_detail.html', {'expose': expose})

def about(request):
    return render(request, 'core/about.html')