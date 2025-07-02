from django import forms
from .models import Group

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description', 'members']
        widgets = {
            'members': forms.CheckboxSelectMultiple,
            'description': forms.Textarea(attrs={'rows': 2}),
        }