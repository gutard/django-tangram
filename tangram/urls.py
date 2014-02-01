from django.conf.urls import patterns, url

urlpatterns = patterns("tangram.views",
    url("^respos/inscription/$", "inscription", name="inscription"),
    url("^fichgrams/$", "fichgrams", name="fichgrams"),
    url("^fichgrams/(?P<numero>\d+)/$", "fichgram", name="fichgram"),
    url("^$", "grams", name="grams"),
)
