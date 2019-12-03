from django.urls import path, include
from . import views


urlpatterns = [
    path('messages/', views.MessageListView.as_view()),
    path('add/message/', views.CreateMessageView.as_view()),
    path('comments/', views.CommentListView.as_view()),
    path('add/comment/', views.CreateCommentView.as_view()),

]
