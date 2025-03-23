from django.urls import URLPattern, path

from . import views

urlpatterns =  [ path("", views.index, name="index"),
                path("new", views.new, name="new")
                 ]