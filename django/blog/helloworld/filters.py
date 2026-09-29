
import django_filters
from django import forms
from helloworld.models import Post


class PostFilter(django_filters.FilterSet):
    created_on = django_filters.DateFilter(
        field_name='created_on',
        lookup_expr='date',
        widget=forms.DateInput(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = Post
        fields = ['created_on']