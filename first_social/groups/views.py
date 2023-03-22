from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from django.contrib import messages
from .models import Group, GroupMember
from django.urls import reverse
from django.views.generic import (DetailView, DeleteView, CreateView,
                                  ListView, UpdateView, RedirectView)
# Create your views here.


class CreateGroup(LoginRequiredMixin, CreateView):
    model = Group
    fields = ('name', 'description')
    template_name = 'groups/groups_form.html'


class SingleGroup(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'groups/groups_detail.html'



class ListGroup(ListView):
    model = Group
    template_name = 'groups/groups_list.html'


class JoinGroup(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request, message="Already a member")
        else:
            messages.success(self.request, message="You are now a member")

        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):

        try:
            membership = GroupMember.objects.get(
                user=self.request.user,
                group__slug=self.kwargs.get('slug')
            )
        except GroupMember.DoesNotExist:
            messages.warning(self.request, message="You are not in this group")
        else:
            membership.delete()
            messages.success(self.request, message="You have left the group")

        return super().get(request, *args, **kwargs)



