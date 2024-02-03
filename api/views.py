from django.shortcuts import render
from rest_framework import viewsets
from api.models import Question
from api.serializers import QuestionSerializer

# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset= Question.objects.all()
    serializer_class=QuestionSerializer