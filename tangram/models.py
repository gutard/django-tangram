# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Unite(models.Model):
    nom = models.CharField(u"Nom de l'unité", max_length=100)
    inscr_explogram = models.NullBooleanField(u"Nous souhaitons participer à l'ExploGRAM")
    inscr_congram = models.NullBooleanField(u"Nous souhaitons participer au ConGRAM")
    inscr_tangram = models.NullBooleanField(u"Nous souhaitons participer au rassemblement TanGRAM")
    theme_explogram = models.CharField(max_length=100, blank=True)
    etat_explogram = models.TextField(u"Descriptif de l'ExploGRAM tel qu'il en est aujourd'hui", blank=True)
    effectif = models.PositiveIntegerField(u"Effectif approximatif", blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True)
    tel = models.CharField(max_length=100)
    user = models.OneToOneField(User)
