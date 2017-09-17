from django.contrib import admin
from . import models

# to edit objects of the model
# class GroupMemberInLine(admin.TabularInLine):
#     model = models.GroupMember

admin.site.register(models.GroupMember)
admin.site.register(models.Group)
