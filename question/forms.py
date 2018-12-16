from django.forms import ModelForm
from question.models import Question,Answer,Comment

class QuestionAddForm(ModelForm):
     class Meta:
         model = Question
         fields = ['title', 'body', 'tag','owner',]


class QuestionEditForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'tag', ]


class AnswerAddForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['body', 'owner',]


class AnswerEditForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['body',]


class CommentAddForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'owner', ]


class CommentEditForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body',]