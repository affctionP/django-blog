from django import forms
from django.forms.widgets import EmailInput
from .models import Comment

from django.forms import ModelForm, Textarea ,TextInput

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['name', 'email', 'text']
		
		widgets = {
			'text': Textarea(attrs={'cols': 50, 'rows':5,'class':'form-control'}),
			'name':	TextInput(attrs = {'class':'form-control'}),
			'email':EmailInput(attrs = {'class':'form-control'})
			
		}

class searchForm(forms.Form):
	query = forms.CharField(label='',max_length= 50)
	query.widget.attrs.update({'class':'searchform'})
	

	

