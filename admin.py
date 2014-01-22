#Content app
from django.contrib import admin
from WebContent.models import Page, FileUpload, ContentTag, HyperLink

class FileUploadAdmin(admin.ModelAdmin):
    list_display = ["slug", "get_static_url"]

admin.site.register(Page)
admin.site.register(FileUpload, FileUploadAdmin)
admin.site.register(ContentTag)
admin.site.register(HyperLink)
