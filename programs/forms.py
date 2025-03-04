from django import forms
from .models import Program
from django.utils.translation import activate, gettext_lazy as _

class ProgramForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # Activate the desired language when the form is initialized
        activate('ar')  # Replace 'ar' with the desired language code
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = Program
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Enter program name')}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Enter program description')}),
        }
        label = {
            'name' : _('Name'),
            'description' : _('Description'),
        }
