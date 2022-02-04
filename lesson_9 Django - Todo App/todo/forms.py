from django import forms
from .models import Todo

class TodoAddForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title']
        # field = '__all__'
        
class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'completed']