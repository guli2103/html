from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import mimetypes


def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'index.html', context )

def vazifa1(request, slug ):
    vazifa1 = Post.objects.get(slug=slug)
    context = {
        'vazifa1' : vazifa1
    }
    return render(request, 'vazifa1.html', context)

def vazifa2(request, slug ):
    vazifa2 = Post.objects.get(slug=slug)
    context = {
        'vazifa2': vazifa2
    }
    return render(request, 'vazifa2.html', context)

def vazifa3(request):
    return render(request, 'vazifa3.html')

def vazifa4(request):
    return render(request, 'vazifa4.html')

def vazifa5(request):
    return render(request, 'vazifa5.html')

def vazifa6(request):
    return render(request, 'vazifa6.html')

def vazifa7(request):
    return render(request, 'vazifa7.html')

def vazifa8(request):
    return render(request,'vazifa8.html')

def vazifa9(request):
    return render(request, 'vazifa9.html')

def vazifa10(request):
    return render(request, 'vazifa10.html')

def download_link(self):
    path = self.cert.path
    filename = 'download.extension'
    fl = open(path, 'r')
    mime_type, _ = mimetypes.guess_type(path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response



