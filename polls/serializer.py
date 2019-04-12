from rest_framework import serializers
from .models import Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Choice
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, source='choice_set')

    class Meta(object):
        model = Question
        fields = '__all__'
