from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.home, name="home"),
    url(r'^list/$', views.Question_list),
    url(r'^detail/(?P<id>\d+)/$', views.Question_Detail.as_view()),
    url(r'^(?P<id>\d+)/$', views.question),
    url(r'^answer/(?P<id>\d+)/$', views.answer),
    url(r'^answer/detail/(?P<id>\d+)/$', views.Answer_List_Detail),
    url(r'^answer/comment(?P<id>\d+)/$', views.comment),
    url(r'^answer/comment/detail/(?P<id>\d+)/$', views.Comment_List_Detail),

    # Redirect links to HTML
    url(r'^add/$', views.question_add),
    url(r'^edit/(?P<id>\d+)/$', views.question_edit),

   # url(r'^like/(?P<id>\d+)/$', views.Question_detail),
   # url(r'^dislike/(?P<id>\d+)/$', views.Question_detail),


    # Redirect links to HTML
    url(r'^answer/add/(?P<id>\d+)/$', views.answer_add),
    url(r'^answer/edit/(?P<id>\d+)/$', views.answer_edit),

   # url(r'^answer/like/(?P<id>\d+)/$', views.Question_detail),
   # url(r'^answer/dislike/(?P<id>\d+)/$', views.Question_detail),


    # Redirect links to HTML
    url(r'^answer/comment/add/(?P<id>\d+)/$', views.comment_add),
    url(r'^answer/comment/edit/(?P<id>\d+)/$', views.comment_edit),

   # url(r'^answer/comment/like/(?P<id>\d+)/$', views.Question_detail),
   # url(r'^answer/comment/dislike/(?Pid>\d+)/$', views.Question_detail),


    # Links functionality
    url(r'^add/detail$', views.Question_list),
    url(r'^delete/(?P<id>\d+)$', views.Question_Detail.as_view()),
    url(r'^edit/detail/(?P<id>\d+)$', views.Question_Detail.as_view()),

   # url(r'^answer/add/detail/(?P<id>\d+)/$', views.answer_add),
   # url(r'^answer/delete/detail/(?P<id>\d+)/$', views.answer_delete),
   # url(r'^answer/edit/detail/(?P<id>\d+)/$', views.answer_edit),

   # url(r'^answer/comment/add/detail/(?P<id>\d+)/$', views.comment_add),
   # url(r'^answer/comment/delete/detail/(?P<id>\d+)/$', views.comment_delete),
   # url(r'^answer/comment/edit/detail/(?P<id>\d+)/$', views.comment_edit),



]