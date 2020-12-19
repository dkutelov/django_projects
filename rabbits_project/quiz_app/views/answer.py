from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from quiz_app.forms import QuestionAnswerForm
from quiz_app.models import Answer, Question


class CreateAnswer(CreateView):
    http_method_names = ['post']
    model = Answer
    form_class = QuestionAnswerForm
    success_url = reverse_lazy('quiz:question', 2)

    def form_valid(self, form):
        form.instance.user = self.request.user
        question_id = self.request.POST['question']
        question = Question.objects.get(pk=question_id)
        form.instance.question = question
        return super().form_valid(form)


class UpdateAnswer(UpdateView):
    http_method_names = ['post']
    model = Answer
    form_class = QuestionAnswerForm
    success_url = reverse_lazy('quiz:question', 2)

    def form_valid(self, form):
        form.instance.user = self.request.user
        question_id = self.request.POST['question']
        question = Question.objects.get(pk=question_id)
        form.instance.question = question
        return super().form_valid(form)

