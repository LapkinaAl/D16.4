from django_filters import FilterSet, DateFilter
import django_filters
from django import forms
from .models import Post

class PostFilter(FilterSet):
    post_time_in = DateFilter(
        field_name='post_time_in',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Date',
        lookup_expr='date__gte',
    )
    post_name = django_filters.CharFilter(
        label='Title',
        field_name='post_name',
        lookup_expr='icontains'
    )
    post_author = django_filters.CharFilter(
        lookup_expr='exact',
        field_name='post_author',
        label='Authors name'
    )

    class Meta:
        model = Post
        fields = ['post_author', 'post_name', 'post_time_in']

