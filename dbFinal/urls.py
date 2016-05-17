from django.conf.urls import include, url, patterns
from django.contrib import admin
from contactos import views
urlpatterns = patterns ('',
    # Examples:
    # url(r'^$', 'dbFinal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),

    #url(r'^login/$', contacto_views.login_view, name='login'),
    #url(r'^signup/$', contacto_views.register, name='signup'),
    #url(r'^logout/$', "django.contrib.auth.views.logout",{"next_page":"/"}, name='logout'),

    #url(r'^new/persons/$', contacto_views.PersonView.as_view(), name='person-new'),
    #url(r'^contactos/$', contacto_views.get_contactos, name='get_contactos'),

    #url(r'^contactos/edit/(?P<primaryKey>\d{1,})/$', contacto_views.edit_contactos, name='edit_contactos'),
    #url(r'^grupos/edit/(?P<primaryKey>\d{1,})/$', contacto_views.edit_grupos, name='edit_grupos'),

    #url(r'^contactos/borrar/(?P<primaryKey>\d{1,})/$', contacto_views.delete_contact, name='delete_contactos'),
    #url(r'^grupos/borrar/(?P<primaryKey>\d{1,})/$', contacto_views.delete_group, name='delete_group'),


    #url(r'^new/groups/$', contacto_views.GroupView.as_view(), name='group-new'),
    #url(r'^grupos/$', contacto_views.get_grupos, name='get_grupos'),

    #url(r'^contacts/$', api_views.PersonViewList.as_view(), name='list-contactos'),
    #url(r'^contacts/(?P<pk>[0-9]+)/$', api_views.PersonViewDetail.as_view(), name='detail-contactos'),
)
