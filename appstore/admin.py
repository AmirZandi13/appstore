from django.contrib import admin
from appstore.models import App

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'owner__username')

    actions = ['verify_apps', 'reject_apps']

    def verify_apps(self, request, queryset):
        queryset.update(status='verified')
        self.message_user(request, "Selected apps have been verified.")

    verify_apps.short_description = "Mark selected apps as verified"

    def reject_apps(self, request, queryset):
        queryset.update(status='rejected')
        self.message_user(request, "Selected apps have been rejected.")

    reject_apps.short_description = "Mark selected apps as rejected"
