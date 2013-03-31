#app WebContent
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^viewpage/(.*)', 'WebContent.views.viewpage', name='viewpage'),#returns div with filecontent
    url(r'^viewfile/(.*)', 'WebContent.views.viewfile', name='viewfile'),#returns filecontent
    url(r'^downloadPage/(.*)', 'WebContent.views.downloadPage', name='filedownloadpage'),#returns filecontent
    url(r'^filedl/(.*)', 'WebContent.views.filedl', name='filedl'),#returns filecontent
    url(r'^contentlist/', 'WebContent.views.contentlist', name='contentlist'),#returns list of content
    url(r'^taglist/(?P<tag>[\w\d\-]*)$', 'WebContent.views.taglist', name='taglist'),#returns list of content with tag

)
