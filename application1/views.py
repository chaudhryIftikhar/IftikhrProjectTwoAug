# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Page, PageContent

# Create your views here.


def home(request, Slug):
    print(Slug)
    obj = Page.objects.get(slug=Slug)
    print(obj.title)
    template_name = 'application1/myPage.html'
    context = {'Object': obj}
    return render(request, template_name, context)


def content(request):
    template_name = 'application1/content.html'
    return render(request, template_name)


def view_404(request):
    context = {'Text': "There is no page you are looking for...",
               'errorNo':'404'}
    template_name = 'application1/errorPage.html'
    return render(request, template_name, context)


def view_403(request):
    context = {'Text': "Permission Denied",
               'errorNo':'403'}
    template_name = 'application1/errorPage.html'
    return render(request, template_name, context)


def view_400(request):
    context = {'Text': "Bad Request",
               'errorNo': '400'}
    template_name = 'application1/errorPage.html'
    return render(request, template_name, context)


def view_500(request):
    context = {'Text': "Server Error",
               'errorNo': '500'}
    template_name = 'application1/errorPage.html'
    return render(request, template_name, context)