from .models import Question, Choice
from rest_framework import serializers


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    id = Question.pk
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date')

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    question = QuestionSerializer()
    id = Choice.pk
    class Meta:
        model = Choice
        fields = ('id', 'choice_text', 'votes', 'question')