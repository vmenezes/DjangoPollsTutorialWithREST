from .models import Question, Choice
from rest_framework import serializers


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date')

class ChoiceSerializer(serializer.HyperlinkedModelSerializer):
    class meta:
        model = Choice
        fields = ('question', 'choice_text', 'votes')