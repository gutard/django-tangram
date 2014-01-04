from django import forms

from .models import Unite


class PreinscriptionForm(forms.ModelForm):
    class Meta:
        model = Unite
        fields = ('nom', 'inscr_explogram', 'inscr_congram', 'inscr_tangram',
            'etat_explogram', 'effectif')
