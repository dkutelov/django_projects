from django.shortcuts import render, get_object_or_404, redirect

from quiz_app.forms import QuestionAnswerForm
from quiz_app.models import Quiz, Answer


def get_progress(request, quiz):
    current_answers = len(Answer.objects.filter(user=request.user))
    all_answers = quiz.question_set.count()
    progress = current_answers / all_answers * 100
    return round(progress)


def question(request, quiz_id, question_id):
    if request.method == 'GET':
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        current_question = quiz.question_set.get(pk=question_id)
        progress = get_progress(request, quiz)
        form = QuestionAnswerForm()

        context = {
            'quiz': quiz,
            'question': current_question,
            'progress': progress,
            'form': form
        }
        return render(request, 'quiz/question.html', context)

    elif request.method == 'POST':
        form = QuestionAnswerForm(request.POST)
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        current_question = quiz.question_set.get(pk=question_id)
        progress = get_progress(request, quiz)

        context = {
            'quiz': quiz,
            'question': current_question,
            'progress': progress,
            'form': form
        }
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = current_question
            answer.user = request.user
            answer.save()
            return redirect('quiz:question', quiz_id, question_id + 1)
        return render(request, 'quiz/question.html', context)

