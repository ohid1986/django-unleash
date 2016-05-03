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
from django.views.generic import View

from .forms import (NewsLinkForm, StartupForm, TagForm)
from .models import Startup, Tag

class NewsLinkCreate(View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_newslink = bound_form.save()
            return redirect(new_newslink)
        else:
            return render(
                request,
                self.template_name,
                {'form': bound_form})

class StartupCreate(View):
    form_class = StartupForm
    template_name = 'organizer/startup_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_startup = bound_form.save()
            return redirect(new_startup)
        else:
            return render(
                request,
                self.template_name,
                {'form': bound_form})

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

# def tag_create(request):
#     if request.method == 'POST':
#         form = TagForm(request.POST) # bind data to form
#         if form.is_valid(): # if the data is valid:
#             new_tag = form.save() # create new object from data
#             return redirect(new_tag) # show webpage for new object
#     else: # request.method != 'POST'
#         form = TagForm()
#         return render(request,
#         'organizer/tag_form.html',
#         {'form': form}) # show bound HTML form (with errors)

class TagCreate(View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        else:
            return render(
                request,
                self.template_name,
                {'form': bound_form})

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