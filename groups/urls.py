from django.urls import path
from groups import views
app_name = 'groups'

urlpatterns = [
    path('',views.UserGroupsListView.as_view(),name='user_groups'),
    path('/<int:pk>/',views.GroupDetailView.as_view(),name='group_detail'),
    path('create_group/',views.GroupCreateView.as_view(),name='create_group'),
    path('join_group/<int:group_id>/',views.GroupJoinView.as_view(),name='join_group'),
]