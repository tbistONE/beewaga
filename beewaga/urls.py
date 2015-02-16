from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'beewaga_app.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup$', 'beewaga_app.views.signup', name='home'),
    url(r'^logout$', 'beewaga_app.views.logout_view', name='logout'),
    url(r'^login$', 'beewaga_app.views.login_page', name='login'),
    url(r'^login-check$', 'beewaga_app.views.login_view', name='login_view'),
    url(r'^register$', 'beewaga_app.views.register_view', name='register'),

)
