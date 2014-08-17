from django.contrib import admin
from stigs_web.models import Stig


class StigAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'users', 'location', 'pub_date']
    list_display = ('title', 'creator', 'location', 'pub_date')

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        #print ('creator')

        #if request.user == Stig.creator:
        if request.user.is_superuser:
            return True
        else:
            return False


# Register your models here.
admin.site.register(Stig, StigAdmin)