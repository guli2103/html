from django.urls import path 
from .views import *
from backend.views import *
from django.views.generic import DetailView,  ListView

urlpatterns = [
    path('',index ),
    path('vazifa1/', vazifa1, ),
    path('vazifa2/', vazifa2, ),
    path('vazifa3/', vazifa3, ), 
    path('vazifa4/', vazifa4, ),
    path('vazifa5/', vazifa5, ),
    path('vazifa6/', vazifa6, ),
    path('vazifa7/', vazifa7, ),
    path('vazifa8/', vazifa8, ),
    path('vazifa9/', vazifa9, ),
    path('vazifa10/', vazifa10,),
    path('vazifa11/', vazifa11,),
    path('vazifa12/', vazifa12,),
    path('vazifa13/', vazifa13,),
    path('vazifa14/', vazifa14,),
    path('vazifa15/', vazifa15,),
    path('vazifa16/', vazifa16,),
    path('vazifa17/', vazifa17,),
    path('vazifa18/', vazifa18,),
    path('vazifa19/', vazifa19,),
    path('vazifa20/', vazifa20,),
    


    # url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
    #                                       template_name="project/project.html")),
    # url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name="project/post.html")),
    # url(r'^upload/$', upload),
    # url(r'^download/(?P<path>.*)$', serve, {'document root': settings.MEDIA_ROOT}),
] 

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

