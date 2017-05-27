# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from WebContent.models import Content, Page, FileUpload
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.conf import settings
from django.core.exceptions import PermissionDenied

def authenticate(request, obj):
    if not obj.authGroup.filter(name = "everyone").exists() and not request.user.groups.filter(pk__in = obj.authGroup.all()).exists():
        raise PermissionDenied

def viewpage(request, slug, template=None):

    page = get_object_or_404(Page, slug = slug)

    authenticate(request, page)

    if template is None:
        template = "WebContent/viewpage.html"
    return render(request, template,{"page":page})

def editpage(request, slug, template=None):
    page = get_object_or_404(Page, slug = slug)
    if page.owner != request.user:
        raise PermissionDenied()
    if request.method == "POST":
        page.html = request.POST['content']
        page.save()
        return redirect(page)
    if template is None:
        template = 'WebContent/edit_page.html'
    return render(request, template, {'page': page, 'template': template})

def viewfile(request, slug):

    fileupload = get_object_or_404(FileUpload, slug = slug)
    authenticate(request, fileupload)
    fileupload.fileContent.open()
    content = fileupload.fileContent.read()
    fileupload.fileContent.close()
    return HttpResponse(content)

def downloadPage(request, slug, template=False):
    fileupload = get_object_or_404(FileUpload, slug = slug)
    authenticate(request, fileupload)
    if auth != "all good":
        return auth
    if template:
        return render_to_response(template, context_instance = RequestContext(request, {"download":fileupload}))
    else:
        return render_to_response("WebContent/downloadpage.html", context_instance = RequestContext(request, {"download":fileupload}))
    
def filedl(request, slug):
    fileupload = get_object_or_404(FileUpload, slug = slug)
    auth = authenticate(request, fileupload)
    fileupload.fileContent.open()
    response    = HttpResponse(fileupload.fileContent.read())
    fileupload.fileContent.close()
    filename = fileupload.fileContent.url.split("/")[-1]
    print("filename:", filename)
    response['Content-Disposition'] = 'attachment; filename = %s' %(filename,)
    return response

def taglist(request, tag, template=None):
    print("tag", tag)
    content = Content.objects.filter(tags__name=tag).all()
    print("content:", content)
    if template is None:
        template = "WebContent/contentlist.html"
    return render_to_response(template, context_instance=RequestContext(request, {"content": content}))


def contentlist(request):
    auth = authenticate(request, page)
    return ""
    
