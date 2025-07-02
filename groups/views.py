from django.shortcuts import render,get_object_or_404
from .models import Group
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from posts.models import Post
from .forms import GroupForm
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages as message

# Create your views here.
class UserGroupsListView(LoginRequiredMixin, ListView):
   model = Group
   template_name = 'groups/user_groups.html'
   context_object_name = 'groups'
   
   def get_queryset(self):
       return self.request.user.social_groups.all()

class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'groups/group_detail.html'
    context_object_name = 'group'
    
    def dispatch(self, request, *args, **kwargs):
        group = self.get_object()
        if not group.members.filter(id=request.user.pk).exists():
            return redirect('groups:user_groups')
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_member'] = (self.object.members.filter(pk=self.request.user.pk).exists())
        context['posts'] = (
            Post.objects.filter(group=self.object).order_by('-created_at') 
        )
        return context

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/group_create.html'
    success_url  = reverse_lazy('groups:user_groups')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.members.add(self.request.user)
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available'] = Group.objects.filter(members=self.request.user)
        return context
class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'groups/group_list.html'
    context_object_name = 'groups'
    
    def get_queryset(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(group = self.object).order_by('-created_at')
        # Exclude groups that the user is already a member of
        return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available'] = self.get_queryset()
        return context
class GroupJoinView(LoginRequiredMixin, View):
    def post(self, request, group_id,*args, **kwargs):
        group = get_object_or_404(Group, id=group_id)
        group.members.add(request.user)
        message.success(request, f"You have joined the group {group.name}.")
        return redirect('groups:group_detail', pk=group.pk)

class GroupLeaveView(LoginRequiredMixin, View):
    def post(self, request, group_id, *args, **kwargs):
        group = get_object_or_404(Group, id=group_id)
        if request.user in group.members.all():
            group.members.remove(request.user)
            message.success(request, f"You have left the group {group.name}.")
        else:
            message.error(request, "You are not a member of this group.")
        return redirect('groups:user_groups')