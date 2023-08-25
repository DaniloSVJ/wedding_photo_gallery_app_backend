from django.contrib import admin
from .models import Photo, Comment, Like, UserProfile
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import User
class UserProfileAdmin(DefaultUserAdmin):
    list_display = ('email', 'is_staff', 'user_type')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        (None, {
            'fields': ('email', 'username')
        }),
        ('Permissions and Status', {
            'fields': ('user_type', 'is_active', 'is_staff', 'password', 'first_name', 'last_name')
        }),
    )

admin.site.register(UserProfile, UserProfileAdmin)

# class UserProfileInline(admin.StackedInline):
#     model = UserProfile
#     can_delete = False

# class UserAdmin(DefaultUserAdmin):
#     inlines = (UserProfileInline, )


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['userUpload', 'timestamp', 'approved']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo', 'content', 'timestamp']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo']
