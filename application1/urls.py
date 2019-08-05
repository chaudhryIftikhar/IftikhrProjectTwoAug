from django.conf.urls import url
from .views import home, content



urlpatterns = [
    # url(r'^$', home),
    url(r'^contents/$', content),
    url(r'^(?P<Slug>[-\w]+)/$', home),
]