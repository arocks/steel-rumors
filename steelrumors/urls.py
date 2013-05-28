from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from links.views import LinkListView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LinkListView.as_view(), name='home')
)
