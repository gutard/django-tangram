from django import forms

from .models import Unite, FicheAction


class PreinscriptionForm(forms.ModelForm):
    class Meta:
        model = Unite
        fields = ('branche', 'nom', 'inscr_explogram', 'inscr_congram',
            'inscr_tangram', 'etat_explogram', 'effectif')


class Fichgram1Form(forms.ModelForm):
    class Meta:
        model = Unite
        fields = ('fg1_theme', 'fg1_projet')


class Fichgram2Form(forms.ModelForm):
    class Meta:
        model = Unite
        fields = ('fg2_votants', 'fg2_votants', 'fg2_elus', 'fg2_adresses',
            'fg2_propositions')


class Fichgram3Form(forms.ModelForm):
    class Meta:
        model = Unite
        fields = ('fg3_date', 'fg3_temps', 'fg3_forme')


class Fichgram4Form(forms.ModelForm):
    class Meta:
        model = Unite
        fields = ('fg4_theme', 'fg4_description', 'fg4_taches', 'fg4_roles',
            'fg4_partenaire', 'fg4_materiel', 'fg4_reunions')


class Fichgram5Form(forms.ModelForm):
    class Meta:
        model = Unite
        fields = ('fg5_theme', 'fg5_texte', 'fg5_photo')


class Fichgram6Form(forms.ModelForm):
    class Meta:
        model = Unite
        fields = ('fg6_theme', 'fg6_date', 'fg6_descriptif', 'fg6_positifs')


class Fichgram7Form(forms.ModelForm):
    class Meta:
        model = Unite
        fields = ('fg7_theme', 'fg7_description', 'fg7_install',
            'fg7_presentation', 'fg7_espace', 'fg7_micro', 'fg7_ecran',
            'fg7_expo', 'fg7_autre')


FichgramForms = [
    Fichgram1Form,
    Fichgram2Form,
    Fichgram3Form,
    Fichgram4Form,
    Fichgram5Form,
    Fichgram6Form,
    Fichgram7Form,
]


class FicheActionForm(forms.ModelForm):
    class Meta:
        model = FicheAction
        exclude = ('user', )
