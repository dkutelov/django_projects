from django.urls import path

from quiz_app.views.question import question
from quiz_app.views.index import quiz_index

app_name = 'quiz'

urlpatterns = [
    path('<int:quiz_id>', quiz_index, name='index'),
    path('<int:quiz_id>/question/<int:question_id>', question, name='question'),
]
