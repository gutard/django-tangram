# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


BRANCHE_CHOICES = (
    (1, u"Lutins"),
    (2, u"Louveteaux"),
    (3, u"Éclés"),
    (4, u"Aînés"),
)

EXPLOGRAM_CHOICES = (
    (1, u"Le pont des cultures"),
    (2, u"On est cap !"),
    (3, u"Filles/garçons"),
    (4, u"Au fil du temps"),
)


class Unite(models.Model):
    branche = models.IntegerField(u"Branche", choices=BRANCHE_CHOICES)
    nom = models.CharField(u"Nom de l'unité/équipage", max_length=100)
    inscr_explogram = models.NullBooleanField(u"Nous souhaitons participer à l'ExploGRAM")
    inscr_congram = models.NullBooleanField(u"Nous souhaitons participer au ConGRAM")
    inscr_tangram = models.NullBooleanField(u"Nous souhaitons participer au rassemblement TanGRAM")
    theme_explogram = models.CharField(max_length=100, blank=True)
    etat_explogram = models.TextField(u"Descriptif de l'ExploGRAM tel qu'il en est aujourd'hui", blank=True)
    effectif = models.PositiveIntegerField(u"Effectif approximatif", blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True)
    tel = models.CharField(max_length=100, blank=True)
    user = models.OneToOneField(User)
    fg1_theme = models.IntegerField(u"Notre exploGRAM", null=True, blank=True, choices=EXPLOGRAM_CHOICES)
    fg1_projet = models.TextField(u"Le projet qu'on rêve de réaliser", blank=True)
    fg2_votants = models.CharField(u"Nombre de votants", max_length=100, blank=True)
    fg2_resultat = models.CharField(u"Résultats des votes", max_length=100, blank=True)
    fg2_elus = models.TextField(u"Sont élus", blank=True)
    fg2_adresses = models.TextField(u"Adresses", blank=True)
    fg2_propositions = models.TextField(u"Nombre de propositions à présenter", blank=True)
    fg3_date = models.CharField(u"Date", max_length=100, blank=True)
    fg3_temps = models.TextField(u"Temps consacré", blank=True)
    fg3_forme = models.TextField(u"Forme adoptée (conseil, jeux,...)", blank=True)
    fg4_theme = models.IntegerField(u"Notre exploGRAM", null=True, blank=True, choices=EXPLOGRAM_CHOICES)
    fg4_description = models.TextField(u"Le projet qu'on rêve de réaliser", blank=True)
    fg4_taches = models.BooleanField(u"Nous avons listé les tâches à faire")
    fg4_roles = models.BooleanField(u"Nous nous sommes répartis les rôles")
    fg4_partenaire = models.BooleanField(u"Nous allons chercher un partenaire")
    fg4_materiel = models.BooleanField(u"Nous avons fait la liste du matériel")
    fg4_reunions = models.IntegerField(u"Nombre de réunions de préparation", null=True, blank=True)
    fg5_theme = models.IntegerField(u"Notre exploGRAM", null=True, blank=True, choices=EXPLOGRAM_CHOICES)
    fg5_texte = models.TextField(u"La carte postale de l'exploGRAM", blank=True)
    fg5_photo = models.ImageField(u"Photo", blank=True, null=True, upload_to='carte_postale/')
    fg6_theme = models.IntegerField(u"Notre exploGRAM", null=True, blank=True, choices=EXPLOGRAM_CHOICES)
    fg6_date = models.CharField(u"Date", max_length=100, blank=True)
    fg6_descriptif = models.TextField(u"Descriptif de notre projet", blank=True)
    fg6_positifs = models.TextField(u"Les points positifs de notre projet", blank=True)
    fg7_theme = models.IntegerField(u"Notre exploGRAM", null=True, blank=True, choices=EXPLOGRAM_CHOICES)
    fg7_description = models.TextField(u"Description de notre retransmission", blank=True)
    fg7_install = models.CharField(u"Le temps qu'il nous faudra pour l'installer", max_length=100, blank=True)
    fg7_presentation = models.CharField(u"Le temps qu'il nous faudra pour le présenter pendant le rassemblement tanGRAM", max_length=100, blank=True)
    fg7_espace = models.CharField(u"L'espace qu'il nous faudra", max_length=100, blank=True)
    fg7_micro = models.BooleanField(u"Nous aurons besoin d'un micro")
    fg7_ecran = models.BooleanField(u"Nous aurons besoin d'un écran")
    fg7_expo = models.BooleanField(u"Nous aurons besoin de supports expo")
    fg7_autre = models.TextField(u"Nous aurons besoin d'autres choses", blank=True)
    fg1_ok = models.BooleanField(u"Gram attribué")
    fg2_ok = models.BooleanField(u"Gram attribué")
    fg3_ok = models.BooleanField(u"Gram attribué")
    fg4_ok = models.BooleanField(u"Gram attribué")
    fg5_ok = models.BooleanField(u"Gram attribué")
    fg6_ok = models.BooleanField(u"Gram attribué")
    fg7_ok = models.BooleanField(u"Gram attribué")
