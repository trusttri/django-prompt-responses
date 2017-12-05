from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'prompt_responses'

urlpatterns = [
    url(r'^prompt/(?P<pk>[0-9]+)/$', views.CreateResponseView.as_view(), name='create_response'),
]
