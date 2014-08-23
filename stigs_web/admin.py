from django.contrib import admin
from django.utils import timezone
from stigs_web.models import Stig


class StigAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'users', 'location', 'pub_date']
    list_display = ('title', 'creator', 'location', 'pub_date')
    readonly_fields = ('pub_date',)

    #def get_readonly_fields(self, request, obj=None):
    #    if request.user.is_superuser:
    #        return 'pub_date'
    #    return 'location', 'pub_date'

    def save_model(self, request, obj, form, change):
        # Write pub_date on init.
        if obj.pub_date is None:
            obj.pub_date = timezone.now()
        obj.save()

    def has_change_permission(self, request, obj=None):
        return obj is None or self.queryset(request).filter(pk=obj.pk).count() > 0

    def queryset(self, request):
        query = super(StigAdmin, self).queryset(request)
        if request.user.is_superuser:
            return query
        else:
            if request.user.has_perm('stigs_web.change_own_stig'):
                return query.filter(users__username__exact=request.user)
            else:
                return query.filter(users__id__exact=0)

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            if request.user.is_superuser:
                return True
            else:
                if request.user.has_perm('stigs_web.delete_own_stig'):
                    return request.user == obj.creator()
                else:
                    return False
        else:
            return False


# Register your models here.
admin.site.register(Stig, StigAdmin)