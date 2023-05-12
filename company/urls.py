from django.urls import path, re_path

from . import views


urlpatterns = [
    path(r'', views.APIViewSet.as_view({"get": "retrieve"}), name="company"),

]