# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Page, PageContent

# Register your models here.

admin.site.register(Page)
admin.site.register(PageContent)