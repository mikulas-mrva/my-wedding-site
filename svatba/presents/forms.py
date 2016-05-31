from django.forms import ModelForm, HiddenInput
from .models import Person


# Create the form class.
class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['email', 'present']
        widgets = {'present': HiddenInput()}