from rest_framework import serializers
from .models import *
from user.models import CustomUser

class QuestionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Question
		fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Answer
		fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Comment
		fields = '__all__'

class CustomuserSerializer(serializers.ModelSerializer):

	class Meta:
		model = CustomUser
		fields = '__all__'