from django.urls import path

from . import views

urlpatterns = [
    path("", views.defaultView, name="default"),
   path("<path:encoded_database_connection_string>", views.metaView, name="metadata"),
]