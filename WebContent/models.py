#WebContent app
from django.db import models
from django.core.urlresolvers import reverse

#Each page stored in a database so that users can add more pages easily

def href(url, text, newtab=False):
    tab = ' target="_blank"' if newtab else ''
    return '<a href="%s"%s>%s</a>' %(url, newtab, text)

class ContentTag(models.Model):
    name = models.CharField(max_length = 20)
    context = models.CharField(max_length = 20, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('taglist', kwargs={"tag": self.name})
    
class Content(models.Model):
    slug = models.SlugField(max_length=200)
    pub_date = models.DateField('Date published', null=True, blank=True)
    tags = models.ManyToManyField(ContentTag, blank=True)
    authGroup = models.ManyToManyField("auth.Group", help_text = "Groups who are allowed to view content")
    owner = models.ForeignKey('auth.User')
    created = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)

    def get_subclass(self):
        if hasattr(self, "page"):
            return self.page
        elif hasattr(self, "fileupload"):
            return self.fileupload
        elif hasattr(self, "hyperlink"):
            return self.hyperlink
        else:
            return None

    def __str__(self):
        return self.slug
        
    def get_absolute_url(self):
        sub = self.get_subclass()
        if sub:
            return sub.get_absolute_url()
        else:
            return ""

    def href(self):
        return href(self.get_absolute_url(), str(self))

class Page(Content):

    html = models.TextField()

    def as_div(self):
        return '<div id="%s">%s</div>' %(self.slug, self.html)

    def get_absolute_url(self):
        return reverse("viewpage", args = [self.slug])
    #Optional fields that should only be filled in when entering an update. Text and image.

class FileUpload(Content):
    fileContent = models.FileField(upload_to= "uploads/webcontent/%Y/%m/%d/", null=False,blank=False)

    def image_tag(self):
        return '<img src="%s"/>' %(self.fileContent.url)

    def get_absolute_url(self):
        return reverse("filedownloadpage", args=[self.slug])

    def get_static_url(self):
        return self.fileContent.url


class HyperLink(Content):
    target = models.URLField()

    def get_absolute_url(self):
        return self.target
