
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from helloworld.serializers import PostSerializer
from helloworld.models import Post
from helloworld.permissions import IsPostPossessor
from helloworld.filters import PostFilter


class HelloWorldView(APIView):
    def get(self, request, format=None):
        return Response({'message': 'Hello world'})


class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    serializer_class = PostSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = PostFilter
    search_fields = ['title', 'content']
    ordering_fields = ['id']

    def get_queryset(self):
        return Post.objects.filter(
            created_by=self.request.user
        )