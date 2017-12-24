from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    def clean_body(self):
        comment = self.cleaned_data['body']
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return comment

    class Meta:
        model = Comment
        # exclude = []
        fields = '__all__'
        labels = {
            'subject': 'Konu',
            'comment': 'Yorumunuz',
            'mail': 'E-mail',
        }
        # fields = ["body"]

