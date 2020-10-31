from django import forms
from timer_app.models import SubTopic
from django.core.validators import RegexValidator


class SubTopicForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        validators=[RegexValidator(r'^[A-Zaz][\w\d\s]+$', message='Topic name should start with letter.')],
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    topic = forms.ChoiceField(
        choices=[],
        required=True,
        label='Select from existing topics',
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = SubTopic
        fields = ['name']

