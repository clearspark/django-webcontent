#app WebContent
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^viewpage/(.*)', views.viewpage, name='viewpage'),#returns div with filecontent
    url(r'^editpage/(.*)', views.editpage, name='editpage'),#returns div with filecontent
    url(r'^viewfile/(.*)', views.viewfile, name='viewfile'),#returns filecontent
    url(r'^downloadPage/(.*)', views.downloadPage, name='filedownloadpage'),#returns filecontent
    url(r'^filedl/(.*)', views.filedl, name='filedl'),#returns filecontent
    url(r'^contentlist/', views.contentlist, name='contentlist'),#returns list of content
    url(r'^taglist/(?P<tag>[\w\d\-]*)$', views.taglist, name='taglist'),#returns list of content with tag

]
