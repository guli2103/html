from django.urls import path
from .views import *

urlpatterns = [
    path('',index ),
    path('vazifa1/', vazifa1, name='vazifa1'),
    path('vazifa2/', vazifa2, name='vazifa2'),
    path('vazifa3/', vazifa3, name='vazifa3'), 
    path('vazifa4/', vazifa4, name='vazifa4'),
    path('vazifa5/', vazifa5, name='vazifa5'),
]