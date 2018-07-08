from django.conf.urls import include, url
from django.urls import path
from django.contrib.auth import views
from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'crm.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^', include('common.urls', namespace='common')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^leads/', include('leads.urls', namespace='leads')),
    url(r'^contacts/', include('contacts.urls', namespace='contacts')),
    url(r'^opportunities/', include('opportunity.urls', namespace='opportunities')),
    url(r'^cases/', include('cases.urls', namespace='cases')),
    url(r'^emails/', include('emails.urls', namespace='emails')),
    # url(r'^planner/', include('planner.urls', namespace='planner')),
    url(r'^logout/$', views.logout, {'next_page': '/login/'}, name='logout'),
    path('admin/', admin.site.urls),

]
