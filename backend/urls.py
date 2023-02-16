from django.urls import path
from .views import *
from backend.views import *

urlpatterns = [
    path('',index ),
    path('vazifa1/<slug:slug>/', vazifa1, name='vazifa1'),
    path('vazifa2/<slug:slug>/', vazifa2, name='vazifa2'),
    path('vazifa3/', vazifa3, name='vazifa3'), 
    path('vazifa4/', vazifa4, name='vazifa4'),
    path('vazifa5/', vazifa5, name='vazifa5'),
    path('vazifa6/', vazifa6, name='vazifa6'),
    path('vazifa7/', vazifa7, name='vazifa7'),
    path('vazifa8/', vazifa8, name='vazifa8'),
    path('vazifa9/', vazifa9, name='vazifa9'),
    path('vazifa10/', vazifa10, name='vazifa10'),
]