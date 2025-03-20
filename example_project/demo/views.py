from django.shortcuts import render
from WebContent.models import Content, Page, FileUpload, ContentTag

def home(request):
    # Get some example content
    pages = Page.objects.all()
    files = FileUpload.objects.all()
    tags = ContentTag.objects.all()
    
    return render(request, 'demo/home.html', {
        'pages': pages,
        'files': files,
        'tags': tags,
    })
