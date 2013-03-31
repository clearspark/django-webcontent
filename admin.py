#Content app
from django.contrib import admin
from csdjango.WebContent.models import Page, FileUpload, ContentTag
try:
    from tinymce.widgets import TinyMCE
    from tinymce.widgets import AdminTinyMCE
    tinyMCE = True
except ImportError:
    tinyMCE = False
    print "Could not import TinyMCE"

from django.db import models

class PageAdmin(admin.ModelAdmin):

    if tinyMCE:
        formfield_overrides = {
            models.TextField: {'widget': TinyMCE(attrs={'cols': 200, 'rows': 50})},
            }

admin.site.register(Page,PageAdmin)
admin.site.register(FileUpload)
admin.site.register(ContentTag)
