from django.contrib import admin
from .models import Quiz, Question, Answer
from django.contrib import admin


class QuestionInlineAdmin(admin.TabularInline):
    model = Question


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInlineAdmin, ]


class AnswerInlineAdmin(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInlineAdmin, ]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

