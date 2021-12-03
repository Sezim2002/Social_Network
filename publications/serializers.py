from rest_framework import serializers
from publications.models import Publication


class PublicationList_Detail_Create_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['likes_count'] = instance.likes.count()
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        return rep

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    publication = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Publication.objects.all())
    user = serializers.PrimaryKeyRelatedField(read_only=True)


