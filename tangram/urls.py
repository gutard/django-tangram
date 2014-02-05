from django.conf.urls import patterns, url

urlpatterns = patterns("tangram.views",
    url("^respos/inscription/$", "inscription", name="inscription"),
    url("^respos/fiches-action/$", "fiches", name="fiches"),
    url("^respos/fiches-action/(?P<pk>\d+)/$", "fiche", name="fiche"),
    url("^respos/fiches-action/ajouter/$", "ajouter_fiche", name="ajouter_fiche"),
    url("^respos/fiches-action/(?P<pk>\d+)/modifier/$", "modifier_fiche", name="modifier_fiche"),
    url("^fichgrams/$", "fichgrams", name="fichgrams"),
    url("^fichgrams/(?P<numero>\d+)/$", "fichgram", name="fichgram"),
    url("^$", "grams", name="grams"),
)
