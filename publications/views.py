from publications.models import Publication, Like, Comment
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins
from publications.permissions import IsAuthorOrIsAdmin, IsAuthor
from publications.serializers import PublicationList_Detail_Create_Serializer, CommentSerializer
from rest_framework.viewsets import GenericViewSet


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationList_Detail_Create_Serializer
    permission_classes = [IsAuthorOrIsAdmin,]

    def get_serializer_class(self):
        if self.action == 'list':
            return PublicationList_Detail_Create_Serializer
        elif self.action == 'retrieve':
            return PublicationList_Detail_Create_Serializer
        return PublicationList_Detail_Create_Serializer

    @action(['POST','DELETE'], detail=True)
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        try:
            like = Like.objects.get(room=post, user=user)
            like.is_liked = not like.is_liked
            if like.is_liked:
                like.save()
            else:
                like.delete()
            message = 'Нрпвится' if like.is_liked else 'Вам больше не нравится эта запись'
        except Like.DoesNotExist:
            Like.objects.create(room=post, user=user, is_liked=True)
            message = 'Нравится'
        return Response(message, status=200)

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return []
        elif self.action in ['like', 'favorite', 'reservation']:
            return [IsAuthenticated()]
        else:
            return []


class CommentViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [IsAuthor]



