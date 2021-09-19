from django.forms import ModelForm, fields
from django.forms.widgets import EmailInput
from .models import Subscriber

class SubForm(ModelForm):
    class Meta:
        model=Subscriber
        fields = ['email']
        labels = {
             'email': '',
            }
        widgets = {
			'email': EmailInput(attrs={'class': 'sub-email'}),
		}
