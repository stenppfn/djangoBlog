from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework import viewsets
from .models import Blog, User
from .serializers import BlogSerializer,UserSerializer
from utils.page import MyPageNumberPagination


class BlogViewSet(viewsets.ModelViewSet):

    pagination_class = MyPageNumberPagination
    # 指定查询集
    queryset = Blog.objects.all()
    # 指定序列化器
    serializer_class = BlogSerializer


class UserViewSet(viewsets.ModelViewSet):

    pagination_class = MyPageNumberPagination
    # 指定查询集
    queryset = User.objects.all()
    # 指定序列化器
    serializer_class = UserSerializer
