from django.conf import settings
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name


class Question(models.Model):

    title = models.TextField(max_length=1000)
    body = models.TextField(max_length = 10000)
    like_count = models.PositiveIntegerField(default = 0)
    dislike_count = models.PositiveIntegerField(default = 0)
    date = models.DateTimeField(auto_now_add = True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "ques_owner")

    tag = models.ManyToManyField(Tag, blank=True)

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "upvote_ques", blank = True)
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "downvote_ques", blank = True)

    def __str__(self):
        return self.title


class Answer(models.Model):

    body = models.TextField(max_length = 10000)
    like_count = models.PositiveIntegerField(default = 0)
    dislike_count = models.PositiveIntegerField(default = 0)
    date = models.DateTimeField(auto_now_add = True)

    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name = "root_ques")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "ans_owner")

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "upvote_ans", blank = True)
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "downvote_ans", blank = True)


class Comment(models.Model):

    body = models.TextField(max_length = 10000)
    like_count = models.PositiveIntegerField(default = 0)
    dislike_count = models.PositiveIntegerField(default = 0)
    date = models.DateTimeField(auto_now_add = True)

    answer = models.ForeignKey(Answer, on_delete = models.CASCADE, related_name = "root_ans")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "com_owner")

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "upvote_com", blank = True)
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "downvote_com", blank = True)