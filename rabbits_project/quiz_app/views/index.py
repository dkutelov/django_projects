from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from quiz_app.models import Quiz


def quiz_index(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    start_question = None

    if quiz.question_set.count() > 0:
        start_question = quiz.question_set.order_by('position')[0]

    context = {
        'quiz': quiz,
        'start_question': start_question
    }

    return render(request, 'quiz/index.html', context)


class QuizDetail(DetailView):
    model = Quiz
    template_name = 'quiz/quiz-detail.html'
    context_object_name = 'quiz'
    start_question = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quiz = self.get_object()

        if quiz.question_set.count() > 0:
            self.start_question = quiz.question_set.order_by('position')[0]
        context['start_question'] = self.start_question
        return context
