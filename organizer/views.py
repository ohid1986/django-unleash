from django.http.response import HttpResponse
# from django.shortcuts import get_object_or_404
# from django.template import Context, loader
#
# from .models import Tag
#
#
# def homepage(request):
#     tag_list = Tag.objects.all()
#     template = loader.get_template(
#         'organizer/tag_list.html')
#     context = Context({'tag_list': tag_list})
#     output = template.render(context)
#     return HttpResponse(output)
#
#
# def tag_detail(request, slug):
#     # slug = ?
#     #tag = Tag.objects.get(slug__iexact=slug)
#     tag = get_object_or_404(
#         Tag, slug__iexact=slug)
#     template = loader.get_template(
#         'organizer/tag_detail.html')
#     context = Context({'tag': tag})
#     return HttpResponse(template.render(context))

# replaced with following codes

from django.shortcuts import (
    get_object_or_404, redirect, render)

from .forms import TagForm
from .models import Startup, Tag


def startup_detail(request, slug):
    startup = get_object_or_404(
        Startup, slug__iexact=slug)
    return render(
        request,
        'organizer/startup_detail.html',
        {'startup': startup})


def startup_list(request):
    return render(
        request,
        'organizer/startup_list.html',
        {'startup_list': Startup.objects.all()})

def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST) # bind data to form
        if form.is_valid(): # if the data is valid:
            new_tag = form.save() # create new object from data
            return redirect(new_tag) # show webpage for new object
    else: # request.method != 'POST'
        form = TagForm()
        return render(request,
        'organizer/tag_form.html',
        {'form': form}) # show bound HTML form (with errors)



def tag_detail(request, slug):
    tag = get_object_or_404(
        Tag, slug__iexact=slug)
    return render(
        request,
        'organizer/tag_detail.html',
        {'tag': tag})


def tag_list(request):
    return render(
        request,
        'organizer/tag_list.html',
        {'tag_list': Tag.objects.all()})