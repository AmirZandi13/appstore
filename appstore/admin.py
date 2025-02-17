from django.contrib import admin
from appstore.models import App

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'owner__username')

    actions = ['verify_apps']

    def verify_apps(self, request, queryset):
        queryset.update(status='verified')
    verify_apps.short_description = "Mark selected apps as verified"
