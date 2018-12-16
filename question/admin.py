from django.contrib import admin
from question.models import Question,Answer,Comment,Tag

admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
