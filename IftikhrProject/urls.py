"""IftikhrProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, handler404, handler400, handler403, handler500
from django.contrib import admin
from application1.views import view_404

handler404 = 'application1.views.view_404'
handler500 = 'application1.views.view_500'
handler400 = 'application1.views.view_400'
handler403 = 'application1.views.view_403'

urlpatterns = [
    url(r'^application1/', include('application1.urls')),
    url(r'^admin/', admin.site.urls),
]