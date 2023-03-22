from django.contrib import admin
from .views import Group, GroupMember
# Register your models here.


class GroupMemberInline(admin.TabularInline):
    model = GroupMember


admin.site.register(Group)
