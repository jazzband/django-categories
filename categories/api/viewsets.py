from django.db.models import Count

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
            'children',
        ]


countable_fields = [
    f for f in Category._meta.get_fields()
    if f.is_relation and f.name not in ['parent', 'children', 'categoryrelation']
]


for field in countable_fields:
    CategorySerializer._declared_fields[field.name + '_count'] = serializers.SerializerMethodField()

    def field_count(self, obj, field=field):
        return getattr(obj, field.name + '_count', "-")
    setattr(CategorySerializer, 'get_' + field.name + '_count', field_count)
    CategorySerializer.Meta.fields += [field.name + '_count']

CategorySerializer._declared_fields['children'] = CategorySerializer(
    many=True,
    source='get_children',
)


class CategoryList(list):  # To overcome problem with filters that require model in queryset
    model = Category


class CategoryViewSet(
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    queryset = Category.tree.all()
    serializer_class = CategorySerializer

    def get_queryset(self, queryset=None):
        if not queryset:
            queryset = self.queryset

        for field in countable_fields:
            queryset = queryset.annotate(**{field.name + '_count': Count(field.name)})

        queryset = CategoryList(queryset.get_cached_trees())
        return queryset
