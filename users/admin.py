from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    extra = 0

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_profile_picture')
    list_select_related = ('profile',)  

    def get_profile_picture(self, instance):
        if instance.profile.profile_picture:
            return f'<img src="{instance.profile.profile_picture.url}" style="height:50px;width:50px;border-radius:50%;" />'
        return "No Picture"
    get_profile_picture.short_description = "Profile Picture"
    get_profile_picture.allow_tags = True 


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')
    search_fields = ('user__username', 'user__email')
