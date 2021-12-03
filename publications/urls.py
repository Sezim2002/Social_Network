from django.urls import path, include
from publications.views import PublicationViewSet, CommentViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('publications', PublicationViewSet, 'publications')
router.register('comments', CommentViewSet, 'comments')

urlpatterns = [
    path('', include(router.urls)),
]