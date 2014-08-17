from django.contrib import admin
from django.utils import timezone
from stigs_web.models import Stig


class StigAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'users', 'location', 'pub_date']
    list_display = ('title', 'creator', 'location', 'pub_date')
    readonly_fields = ('pub_date',)

    def save_model(self, request, obj, form, change):
        # Write pub_date on init.
        if obj.pub_date is None:
            obj.pub_date = timezone.now()
        obj.save()

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            print obj.creator()
            print request.user

            if request.user == obj.creator() or request.user.is_superuser:
                return True
            else:
                return False
        else:
            return False


# Register your models here.
admin.site.register(Stig, StigAdmin)