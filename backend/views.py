from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'index.html', context )

def vazifa1(request):
    return render(request, 'vazifa1.html')

def vazifa2(request):
    return render(request, 'vazifa2.html')

def vazifa3(request):
    return render(request, 'vazifa3.html')

def vazifa4(request):
    return render(request, 'vazifa4.html')

def vazifa5(request):
    return render(request, 'vazifa5.html')