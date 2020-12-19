from django.urls import path

from quiz_app.views.answer import CreateAnswer, UpdateAnswer
from quiz_app.views.question import question, QuestionDetail
from quiz_app.views.index import quiz_index, QuizDetail

app_name = 'quiz'

urlpatterns = [
    path('<int:quiz_id>', quiz_index, name='index'),
    path('<int:quiz_id>/question/<int:question_id>', question, name='question'),
    path('<int:quiz_id>/question/detail/<int:question_id>/', question, name='question'),
    path('<int:quiz_id>/question/<int:question_id>/edit', question, name='question'),
    path('detail/<int:pk>/', QuizDetail.as_view(), name='quiz detail'),
    path('question/<int:pk>/', QuestionDetail.as_view(), name='question update'),
    path('answer/create', CreateAnswer.as_view(), name='create answer'),
    path('answer/update/<int:pk>', UpdateAnswer.as_view(), name='update answer'),
]
