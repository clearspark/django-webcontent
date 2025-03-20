#app WebContent
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^viewpage/(.*)', views.viewpage, name='viewpage'),#returns div with filecontent
    re_path(r'^editpage/(.*)', views.editpage, name='editpage'),#returns div with filecontent
    re_path(r'^viewfile/(.*)', views.viewfile, name='viewfile'),#returns filecontent
    re_path(r'^downloadPage/(.*)', views.downloadPage, name='filedownloadpage'),#returns filecontent
    re_path(r'^filedl/(.*)', views.filedl, name='filedl'),#returns filecontent
    path('contentlist/', views.contentlist, name='contentlist'),#returns list of content
    re_path(r'^taglist/(?P<tag>[\w\d\-]*)$', views.taglist, name='taglist'),#returns list of content with tag
]
