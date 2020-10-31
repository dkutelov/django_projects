from django import forms
from timer_app.models import Topic
from django.core.validators import RegexValidator


class TopicForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        validators=[RegexValidator(r'^[A-Zaz][\w\d\s]+$', message='Topic name should start with letter.')],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Topic
        fields = ['name']

