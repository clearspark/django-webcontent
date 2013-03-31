#Content app
from django.contrib import admin
from WebContent.models import Page, FileUpload, ContentTag
from tinymce.widgets import TinyMCE
from tinymce.widgets import AdminTinyMCE
from django.db import models



class PageAdmin(admin.ModelAdmin):

	
	formfield_overrides = {
		models.TextField: {'widget': TinyMCE(attrs={'cols': 200, 'rows': 50})},
		}
        #admin.site.register(PageAdmin)

admin.site.register(Page,PageAdmin)
admin.site.register(FileUpload)
admin.site.register(ContentTag)
