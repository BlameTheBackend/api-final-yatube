from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .views import (
    PostViewSet, GroupViewSet, FollowViewSet, CommentViewSet
)


app_name = 'api'

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet, basename='user-follows')

posts_router = routers.NestedDefaultRouter(
    router, r'posts', lookup='post'
)
posts_router.register(r'comments', CommentViewSet, basename='post-comments')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(posts_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt'))
]
