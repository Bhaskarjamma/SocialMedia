from django.urls import path
from groups import views
app_name = 'groups'

urlpatterns = [
    path('',views.UserGroupsListView.as_view(),name='user_groups'),
    path('<int:pk>/',views.GroupDetailView.as_view(),name='group_detail'),
    path('create_group/',views.GroupCreateView.as_view(),name='create_group'),
    path("<int:group_id>/join/",views.GroupJoinView.as_view(),name="join_group"),
    path('leave/<int:group_id>/', views.GroupLeaveView.as_view(), name='leave_group'),
]