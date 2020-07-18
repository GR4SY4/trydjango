"""trydjango URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from pages.views import home_view, login_view, register_view, contact_view
from list.views import product_view, checkout_view, cart_view, categories_view

urlpatterns = [
    url(r'^$', home_view),
    url(r'^home/', home_view),
    url(r'^login/', login_view),
    url(r'^register/', register_view),
    url(r'^contact/', contact_view),
    url(r'^product/', product_view),
    url(r'^checkout/', checkout_view),
    url(r'^cart/', cart_view),
    url(r'^categories/', categories_view),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()