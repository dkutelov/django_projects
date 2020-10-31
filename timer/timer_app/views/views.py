from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from timer_app.forms.subtopic import SubTopicForm
from timer_app.forms.topic import TopicForm
from timer_app.models import Topic, SubTopic


def homepage(request):
    return render(request, 'timer/index.html')


def dashboard(request):
    return render(request, 'timer/dashboard.html')








def start_session(request):
    pass

