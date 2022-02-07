""" Formu bizim oluşturduğumuz 1. kısım: """
# from django import forms

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     number = forms.IntegerField(required=False)




""" Formu bir modeli aracı olarak kullanarak djangonun oluşturduğu 2. kısım: """

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "number", "profile_pic"]
        # fields = "__all__"
        # exclude ... gelmesini istemediklerimiz
        labels = {"first_name": "Name"}

