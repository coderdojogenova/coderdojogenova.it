from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CoderDojo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^accounts/', include('allauth.urls')),

    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog')),
)
