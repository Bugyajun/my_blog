from django import forms
from comments import models

class commentForm(forms.ModelForm):
    class Meta:
        model = models.comment
        fields = ['name','phone_num','email','comment']



