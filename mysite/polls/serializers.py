from .models import Question, Choice
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    choice_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Choice.objects.all())
    class Meta:
        model = Question
        fields = (
            'id',
            'question_text',
            'pub_date',
            'choice_set'
        )

class ChoiceSerializer(serializers.ModelSerializer):
    question_id = serializers.ReadOnlyField(source='question.pk')
    class Meta:
        model = Choice
        fields = (
            'id',
            'choice_text',
            'votes',
            'question_id',
        )