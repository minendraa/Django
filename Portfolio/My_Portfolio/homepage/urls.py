from .views import index,contact,viewmore
from django.urls import path

urlpatterns=[
    path('',index,name='homepage'),
    path('/contact',contact,name='contact'),
    path('/viewmore',viewmore,name='viewmore')
]