from rest_framework import serializers
from api.models import Question


#create serializers here
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    question_id=serializers.ReadOnlyField()
    class Meta:
        model=Question
        fields="__all__"
