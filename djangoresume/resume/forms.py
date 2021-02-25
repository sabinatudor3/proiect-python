from django import forms
from .models import Data, Skill, Work, Education, Template, Language, Tech


class FormData(forms.ModelForm):
    class Meta:
        model    = Data
        fields   = ['firstname', 'lastname', 'email', 'phone']
   

class FormTech(forms.ModelForm):
    class Meta:
        model    = Tech
        fields = ['profile', 'tech1', 'tech2', 'tech3']


class FormSkill(forms.ModelForm):
    class Meta:
        model    = Skill
        fields   = ['skills1', 'skills2', 'skills3']


class FormWork(forms.ModelForm):
    class Meta:
        model    = Work
        fields   = ['position', 'company', 'description']


class FormEducation(forms.ModelForm):
    class Meta:
        model    = Education
        fields   = ['institution', 'studies', 'description']


class FormLanguage(forms.ModelForm):
    class Meta:
        model    = Language
        fields   = ['language1', 'language2', 'language3']


class FormTemplate(forms.ModelForm):
    class Meta:
        model    = Template
        fields   = ['type']
