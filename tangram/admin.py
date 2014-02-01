from django.contrib import admin

from .models import Unite


class UniteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'branche', 'theme_explogram', 'effectif')
    fieldsets = (
        (None, {
            #'classes': ('collapse',),
            'fields': ('branche', 'nom', 'inscr_explogram', 'inscr_congram', 'inscr_tangram', 'theme_explogram', 'etat_explogram', 'effectif', 'contact', 'tel', 'user')
        }),
        ('FichGRAM 1', {
            #'classes': ('collapse',),
            'fields': ('fg1_theme', 'fg1_projet', 'fg1_ok')
        }),
        ('FichGRAM 2', {
            #'classes': ('collapse',),
            'fields': ('fg2_votants', 'fg2_resultat', 'fg2_elus', 'fg2_adresses', 'fg2_propositions', 'fg2_ok')
        }),
        ('FichGRAM 3', {
            #'classes': ('collapse',),
            'fields': ('fg3_date', 'fg3_temps', 'fg3_forme', 'fg3_ok')
        }),
        ('FichGRAM 4', {
            #'classes': ('collapse',),
            'fields': ('fg4_theme', 'fg4_description', 'fg4_taches', 'fg4_roles', 'fg4_partenaire', 'fg4_materiel', 'fg4_reunions', 'fg4_ok')
        }),
        ('FichGRAM 5', {
            #'classes': ('collapse',),
            'fields': ('fg5_theme', 'fg5_texte', 'fg5_photo', 'fg5_ok')
        }),
        ('FichGRAM 6', {
            #'classes': ('collapse',),
            'fields': ('fg6_theme', 'fg6_date', 'fg6_descriptif', 'fg6_positifs', 'fg6_ok')
        }),
        ('FichGRAM 7', {
            #'classes': ('collapse',),
            'fields': ('fg7_theme', 'fg7_description', 'fg7_install', 'fg7_presentation', 'fg7_espace', 'fg7_micro', 'fg7_ecran', 'fg7_expo', 'fg7_autre', 'fg7_ok')
        }),
    )

admin.site.register(Unite, UniteAdmin)
