from rest_framework import mixins, serializers, viewsets

from ..models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'slug',
            'active',

            'thumbnail',
            'thumbnail_width',
            'thumbnail_height',
            'order',
            'alternate_title',
            'alternate_url',
            'description',
            'meta_keywords',
            'meta_extra',
            'children'
        ]


CategorySerializer._declared_fields['children'] = CategorySerializer(many=True)


class CategoryViewSet(
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    queryset = Category.tree.filter(active=True, parent=None)
    serializer_class = CategorySerializer
