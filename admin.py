#Content app
from django.contrib import admin
from csdjango.WebContent.models import Page, FileUpload, ContentTag, Hyperlink

class FileUploadAdmin(ContentAdmin):
    list_display = ["slug", "title", "get_static_url"]

admin.site.register(Page,PageAdmin)
admin.site.register(FileUpload, FileUploadAdmin)
admin.site.register(ContentTag)
admin.site.register(HyperLink)
