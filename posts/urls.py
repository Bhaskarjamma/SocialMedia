from django.urls import path
from .views import PostListView, PostDetailView, post_create, like_toggle, add_comment, delete_comment, edit_comment, delete_post
app_name = 'posts'

urlpatterns = [
    path('',PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_details'),
    path('new/',post_create,name='new_post'),
    path('<int:pk>/like/',like_toggle,name='like_toggle'),
    path('<int:pk>/comment/',add_comment,name='add_comment'),
    path('comment/<int:pk>/delete/', delete_comment, name='delete_comment'),
    # path('comment/<int:pk>/edit/', edit_comment, name='edit_comment'),
    path('comment/<int:pk>/edit/', edit_comment, name='edit_comment'),
    path('posts/<int:pk>/delete/', delete_post, name='delete_post'),
]


