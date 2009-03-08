from django import forms
from django.utils.translation import ugettext_lazy as _

from models import Registrant

class RegistrationForm(forms.ModelForm):
    def clean_terms_accepted(self):
        if self.cleaned_data['terms_accepted'] != True:
            raise forms.ValidationError(_(u'You need to accept the terms to register.'))
        else:
            return self.cleaned_data['terms_accepted']

    class Meta:
        model = Registrant
        exclude = ('registered', 'scheduled',)
