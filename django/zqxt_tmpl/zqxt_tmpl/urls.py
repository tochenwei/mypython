from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zqxt_tmpl.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'learn.views.home', name='home'),
	url(r'^add/(\d+)/(\d+)/$', 'learn.views.add', name='add'),
	url(r'^login/$', 'learn.views.login', name='login'),
    url(r'^admin/', include(admin.site.urls)),
)
