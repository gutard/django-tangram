from django.conf.urls import patterns, url

urlpatterns = patterns("tangram.views",
    url("^$", "fichgrams", name="fichgrams"),
    url("^(?P<numero>\d+)/$", "fichgram", name="fichgram"),
)
