from django.contrib import admin
from django.urls import include, path
from api.views import login, logout, index, create

urlpatterns = [
#     path('login/', login, name='login'),
#     path('logout/', logout, name='logout'),
    path('create/', create, name='create'),
    
]
