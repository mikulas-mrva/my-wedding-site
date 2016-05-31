from django.forms import ModelForm
from .models import Visitor


class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        fields = [
            'email',
            'name',
            'attending',
            'baker',
            'vegan',
            'vegetarian',
            'gluten_free',
        ]
        label_suffix = ''
        # success_url='/tesime-se'
