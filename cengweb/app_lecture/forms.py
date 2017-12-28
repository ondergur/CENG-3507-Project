from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    def clean_body(self):
        question = self.cleaned_data['body']
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return question

    class Meta:
        model = Question
        # exclude = []
        fields = '__all__'
        labels = {
            'name': 'İsim',
            'question': 'Sorunuz',
            'mail': 'E-mail',
        }
        # fields = ["body"]

