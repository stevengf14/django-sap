from django.forms import TextInput, ModelForm
from personas.models import Domicilio


class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            'no_calle': TextInput(attrs={'type': 'number'})
        }