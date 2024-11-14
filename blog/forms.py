from django import forms
from blog.models import Service

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Service 
        fields = ['blog_title','blog_name','blog_body'] 
