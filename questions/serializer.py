from rest_framework import serializers
from .models import Questions, Answers


class QuizQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = '__all__'


class QuizAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answers
        fields = ('answer', )
