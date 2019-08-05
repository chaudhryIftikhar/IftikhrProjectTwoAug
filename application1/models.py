# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Page(models.Model):
    PUBLISHED = 'PB'
    DRAFT = 'DF'
    content_status = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
    )

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    slug = models.SlugField(max_length=15)
    content = models.TextField(max_length=1000)
    status = models.CharField(max_length=15, choices=content_status)

    def __str__(self):
        return self.title


class PageContent(models.Model):
    title=models.CharField(max_length=20)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title
