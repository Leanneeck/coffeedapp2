from django.conf.urls import patterns, include, url
import core.views as coreviews
from django.conf.urls import include

urlpatterns = patterns('',

    url(r'^$', coreviews.LandingView.as_view()),
 )


