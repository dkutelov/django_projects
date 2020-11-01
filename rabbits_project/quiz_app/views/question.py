from django.shortcuts import render, get_object_or_404, redirect

from quiz_app.forms import QuestionAnswerForm
from quiz_app.models import Quiz, Answer


def get_progress(request, quiz):
    current_answers = len(Answer.objects.filter(user=request.user))
    all_answers = quiz.question_set.count()
    progress = current_answers / all_answers * 100
    return round(progress)


def get_next_question(current_question, ordered_questions):
    next_question_index = ordered_questions.index(current_question) + 1
    if next_question_index >= len(ordered_questions):
        return ordered_questions[0].id
    else:
        return ordered_questions[next_question_index].id


def question(request, quiz_id, question_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    current_question = quiz.question_set.get(pk=question_id)
    ordered_questions = quiz.question_set.order_by('position')
    start_question = None

    if quiz.question_set.count() > 0:
        start_question = ordered_questions[0]

    if request.method == 'GET':
        progress = get_progress(request, quiz)

        context = {
            'quiz': quiz,
            'question': current_question,
            'progress': progress,
            'start_question': start_question
        }

        try:
            answer = Answer.objects.get(user=request.user, question=current_question)
            context['form'] = QuestionAnswerForm(instance=answer)
        except Answer.DoesNotExist:
            context['form'] = QuestionAnswerForm()

        return render(request, 'quiz/question.html', context)

    elif request.method == 'POST':
        next_question = get_next_question(current_question, list(ordered_questions))
        try:
            answer = Answer.objects.get(user=request.user, question=current_question)
            form = QuestionAnswerForm(request.POST, instance=answer)

            if form.is_valid():
                form.save()
                return redirect('quiz:question', quiz_id, next_question)

        except Answer.DoesNotExist:
            form = QuestionAnswerForm(request.POST)

            if form.is_valid():
                answer = form.save(commit=False)
                answer.question = current_question
                answer.user = request.user
                answer.save()
                return redirect('quiz:question', quiz_id, next_question)
