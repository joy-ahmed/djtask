from django.contrib import admin

from taskList_app.models import ProfileImg

@admin.register(ProfileImg)
class AdminProfile(admin.ModelAdmin):
    pass
