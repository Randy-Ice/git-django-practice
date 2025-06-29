from django.urls import path
from blog.views import PostViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('posts', PostViewSet)
urlpatterns  = router.urls
