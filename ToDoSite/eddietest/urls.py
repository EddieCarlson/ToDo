from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^eddietest/', include('eddietest.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    (r'^$', 'eddietest.messages.views.root'),
	(r'^user/(.{10})/$', 'eddietest.messages.views.index'),
    (r'^user/(.{10})/add/$', 'eddietest.messages.views.add'),   
    (r'^user/(.{10})/task/(\d+)/$', 'eddietest.messages.views.task'), 
    (r'^user/(.{10})/kind=(.+)/$', 'eddietest.messages.views.dispTasks', { 'dispAll' : False }),
	(r'^sneaky/set_defaults/$', 'eddietest.messages.views.defaults'),
	# Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
