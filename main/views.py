from django.shortcuts import get_object_or_404
from rest_framework import generics, exceptions, status , permissions
from rest_framework.response import Response

from .serializers import MessageSerializer, CommentSerializer, Message, Comment


class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CreateMessageView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = MessageSerializer
    queryset = ''

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CreateCommentView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CommentSerializer
    queryset = ''

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
