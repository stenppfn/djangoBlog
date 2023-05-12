from django.urls import path, re_path,include
from . import views


urlpatterns = [
    path(r'', views.BlogViewSet.as_view({"get": "list","post": "create"}), name="blog"),
    # path(r'', views.UserViewSet.as_view({"get": "list"}), name="blog"),
    # path(r'', views.BlogViewSet.as_view(), name="blog"),
]
