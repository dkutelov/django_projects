from django.shortcuts import render, get_object_or_404

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
