from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('', TemplateView.as_view(template_name='question/home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('user/', include('django.contrib.auth.urls')),
    path('question/', include('question.urls')),

]

urlpatterns = format_suffix_patterns(urlpatterns)