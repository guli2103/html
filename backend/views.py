from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Post
import mimetypes


def index(request):
    if 'q' in request.GET:
        q=request.GET['q']
        post = Q(Q(name__nomi__icontains=q))
        posts = Post.objects.filter(post)
    else: 
        posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'index.html', context )


def vazifa1(request ):
    return render(request, 'vazifa1.html')

def vazifa2(request):
    return render(request, 'vazifa2.html')

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

def vazifa11(request):
    return render(request, 'vazifa11.html')

def vazifa12(request):
    return render(request, 'vazifa12.html')

def vazifa13(request):
    return render(request, 'vazifa13.html')

def vazifa14(request):
    return render(request, 'vazifa14.html')

def vazifa15(request):
    return render(request, 'vazifa15.html')

def vazifa16(request):
    return render(request, 'vazifa16.html')

def vazifa17(request):
    return render(request, 'vazifa17.html')

def vazifa18(request):
    return render(request, 'vazifa18.html')

def vazifa19(request):
    return render(request, 'vazifa19.html')

def vazifa20(request):
    return render(request, 'vazifa20.html')

def download_link(self):
    path = self.cert.path
    filename = 'download.extension'
    fl = open(path, 'r')
    mime_type, _ = mimetypes.guess_type(path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response



