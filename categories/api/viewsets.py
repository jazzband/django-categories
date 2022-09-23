from rest_framework import mixins, serializers, viewsets
from rest_framework import permissions
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

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
    CategorySerializer._declared_fields[f'{field.name}_count'] = serializers.SerializerMethodField()

    def field_count(self, obj, field=field):
        return getattr(obj, f'{field.name}_count', "-")
    setattr(CategorySerializer, f'get_{field.name}_count', field_count)
    CategorySerializer.Meta.fields += [f'{field.name}_count']

    CategorySerializer._declared_fields[f'{field.name}_count_cumulative'] = serializers.SerializerMethodField()

    def field_count_cumulative(self, obj, field=field):
        return getattr(obj, f'{field.name}_count_cumulative', "-")
    setattr(CategorySerializer, f'get_{field.name}_count_cumulative', field_count_cumulative)
    CategorySerializer.Meta.fields += [f'{field.name}_count_cumulative']


CategorySerializer._declared_fields['children'] = CategorySerializer(
    many=True,
    source='get_children',
)


class CategoryList(list):  # To overcome problem with filters that require model in queryset
    model = Category


def get_category_queryset(queryset, extra_filters=None, exclude_blank=False):
    if not extra_filters:
        extra_filters = {}

    for field in countable_fields:
        queryset = Category.tree.add_related_count(
            queryset, field.related_model, field.remote_field.name, f"{field.name}_count", extra_filters=extra_filters
        )
        queryset = Category.tree.add_related_count(
            queryset,
            field.related_model,
            field.remote_field.name,
            f"{field.name}_count_cumulative",
            extra_filters=extra_filters,
            cumulative=True,
        )

    if exclude_blank:
        queryset = queryset.filter(asset_count_cumulative__gt=0)
    return queryset


class CategoryViewSet(
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    queryset = Category.tree.all()
    serializer_class = CategorySerializer
    extra_count_filters = {}

    def get_queryset(self, queryset=None):
        if not queryset:
            queryset = self.queryset

        queryset = get_category_queryset(queryset, extra_filters=self.extra_count_filters)

        queryset = CategoryList(queryset.get_cached_trees())
        return queryset

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @method_decorator(cache_page(60 * 60))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)
