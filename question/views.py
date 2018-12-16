from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view
from .serializers import QuestionSerializer, AnswerSerializer, CommentSerializer
from .models import Tag,Question,Answer,Comment

from question.forms import *

# POST = Add, PUT = Update, DELETE = Delete GET = Info Retrieve,

@api_view(['GET', 'POST'])
def Question_list(request):

    if request.method == 'GET':
        ques = Question.objects.all()
        serializer = QuestionSerializer(ques, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def Answer_List_Detail(request, id):

    if request.method == 'GET':
        ans = Answer.objects.filter(question = id)
        serializer = AnswerSerializer(ans, many = True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def Comment_List_Detail(request, id):

    if request.method == 'GET':
        com = Comment.objects.filter(answer = id)
        serializer = CommentSerializer(com, many = True)
        return Response(serializer.data)


class Question_Detail(APIView):
    print(123)
    def get_object(self, id):
        try:
            return Question.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        ques = self.get_object(id)
        ques = QuestionSerializer(ques)
        return Response(ques.data)

    def put(self, request, id, format=None):
        ques = self.get_object(id)
        serializer = QuestionSerializer(ques, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        ques = self.get_object(id)
        ques.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def home(request):
    return render(request, 'question/home.html')

def question(request, id):
    return render(request, 'question/ques.html', {'id' : id})

def answer(request, id):
    return render(request, 'question/ques.html', {'id' : id})

def comment(request, id):
    return render(request, 'question/ques.html', {'id' : id})

def question_add(request):
    return render(request, 'question/question_add.html',{'formqa': QuestionAddForm, 'id' : id})

def question_edit(request, id):
    return render(request, 'question/question_edit.html', {'formqe' : QuestionEditForm, 'id' : id})

def answer_add(request, id):
    return render(request, 'question/answer_add.html', {'formaa' : AnswerAddForm, 'id' : id})

def answer_edit(request, id):
    return render(request, 'question/answer_edit.html', {'formae' : AnswerEditForm, 'id' : id})

def comment_add(request, id):
    return render(request, 'question/comment_add.html', {'formca' : CommentAddForm, 'id' : id})

def comment_edit(request, id):
    return render(request, 'question/comment_edit.html', {'formce' : CommentEditForm, 'id' : id})


