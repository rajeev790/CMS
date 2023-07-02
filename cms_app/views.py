# from django.shortcuts import render
# from django.contrib.admin.views.decorators import staff_member_required
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from django.contrib.admin.sites import AdminSite
# from rest_framework import viewsets
# from .models import User, Post, Like
# from .serializers import UserSerializer, PostSerializer, LikeSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     @method_decorator(login_required(login_url='admin:login'))
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     @method_decorator(login_required(login_url='admin:login'))
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

# class LikeViewSet(viewsets.ModelViewSet):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer

#     @method_decorator(login_required(login_url='admin:login'))
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

# admin_login_view = staff_member_required(login_url='admin:login')(AdminSite().login)

from django.shortcuts import redirect, reverse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.sites import AdminSite
from rest_framework import viewsets
from .models import User, Post, Like
from .serializers import UserSerializer, PostSerializer, LikeSerializer

def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_active or not request.user.is_staff or not request.user.is_superuser:
            return redirect(reverse('admin:login'))  # Redirect non-admin users to the admin login page
        return view_func(request, *args, **kwargs)
    return wrapper

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @method_decorator(custom_login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @method_decorator(custom_login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    @method_decorator(custom_login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

admin_login_view = staff_member_required(login_url='admin:login')(AdminSite().login)

