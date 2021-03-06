"""monumenten URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from rest_framework import routers

from monumenten.api import views as api_views
from monumenten.api import searchviews as search_views


class MonumentenView(routers.APIRootView):
    """
    De monumenten in de stad worden hier als een lijst getoond.

    - monumenten
    - situeringen
    - complexen

    datamodel conform stelselpedia https://www.amsterdam.nl/stelselpedia/monumenten-index/catalogus-monumenten/
    """


class MonumentenRouter(routers.DefaultRouter):
    APIRootView = MonumentenView


monumenten = MonumentenRouter()

monumenten.register(r'situeringen', api_views.SitueringList,
                    basename='situeringen')
monumenten.register(r'monumenten', api_views.MonumentViewSet,
                    basename='monumenten')
monumenten.register(r'complexen', api_views.ComplexViewSet,
                    basename='complexen')

monumenten.register(r'typeahead', search_views.TypeaheadViewSet,
                    basename='typeahead')
monumenten.register(r'search', search_views.SearchComplexenMonumentenViewSet,
                    basename='search')


urls = monumenten.urls
