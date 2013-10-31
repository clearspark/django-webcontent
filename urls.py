#app WebContent
from django.conf.urls import patterns, include, url

urlpatterns = patterns('csdjango.WebContent.views',

    url(r'^viewpage/(.*)', 'viewpage', name='viewpage'),#returns div with filecontent
    url(r'^editpage/(.*)', 'editpage', name='editpage'),#returns div with filecontent
    url(r'^viewfile/(.*)', 'viewfile', name='viewfile'),#returns filecontent
    url(r'^downloadPage/(.*)', 'downloadPage', name='filedownloadpage'),#returns filecontent
    url(r'^filedl/(.*)', 'filedl', name='filedl'),#returns filecontent
    url(r'^contentlist/', 'contentlist', name='contentlist'),#returns list of content
    url(r'^taglist/(?P<tag>[\w\d\-]*)$', 'taglist', name='taglist'),#returns list of content with tag

)
