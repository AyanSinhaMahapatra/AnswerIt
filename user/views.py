from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view
from question.serializers import QuestionSerializer, AnswerSerializer, CommentSerializer, CustomuserSerializer
from user.models import CustomUser

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@api_view(['GET', 'PUT', 'DELETE'])
def User_detail(request, id):
    try:
        user = CustomUser.objects.get(id = id)
    except user.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomuserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomuserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


def user(request, id):
    return render(request, 'user/user.html', {'id' : id})