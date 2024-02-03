from django.contrib import admin
from django.urls import path,include
from api.views import QuestionViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'question', QuestionViewSet)

urlpatterns = [    
    path('',include(router.urls))
]