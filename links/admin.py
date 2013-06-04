from django.contrib import admin
from .models import Link, Vote, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

class LinkAdmin(admin.ModelAdmin):
    pass
admin.site.register(Link, LinkAdmin)

class VoteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Vote, VoteAdmin)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserProfileAdmin(UserAdmin):
    inlines=(UserProfileInline, )

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserProfileAdmin)
