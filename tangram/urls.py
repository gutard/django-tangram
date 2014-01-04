from django.conf.urls import patterns, url

urlpatterns = patterns("tangram.views",
    url("^$", "inscription", name="inscription"),
)
