from django import forms

from quiz_app.models import Answer


class QuestionAnswerForm(forms.ModelForm):
    score = forms.ChoiceField(
        choices=[
            (1, 'max_agree'),
            (2, 'med_agree'),
            (3, 'min_agree'),
            (4, 'neutral'),
            (5, 'min_disagree'),
            (6, 'med_disagree'),
            (7, 'max_disagree'),
        ],
        # required=True,
        widget=forms.RadioSelect(
            # attrs={
            #     'class': 'form-check-input position-static'
            # }
        )
    )

    class Meta:
        model = Answer
        fields = ('score',)
