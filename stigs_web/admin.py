from django.contrib import admin
from django.utils import timezone
from stigs_web.models import Stig


class StigAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'users', 'location', 'pub_date']
    list_display = ('title', 'creator', 'location', 'pub_date')
    readonly_fields = ('pub_date',)
    show_save_as_new = False

    def get_readonly_fields(self, request, obj=None):
        # Make fields editable if it is an add.
        if not obj:
            return super(StigAdmin, self).get_readonly_fields(request, obj)

        # Make fields readonly if the user is not the owner.
        if request.user.is_superuser or \
                (request.user.has_perm('stigs_web.change_own_stig') and
                 obj.is_owner(obj, request.user)):
            return super(StigAdmin, self).get_readonly_fields(request, obj)
        else:
            return 'title', 'content', 'users', 'location', 'pub_date'

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['save_on_bottom'] = True
        return super(StigAdmin, self).add_view(request, form_url, extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        stig = Stig.objects.get(pk=object_id)
        extra_context['save_on_bottom'] = \
            request.user.is_superuser or \
            request.user.has_perm('stigs_web.change_own_stig') and \
            stig.users.filter(username__exact=request.user).exists()
        return super(StigAdmin, self).change_view(request, object_id,
                                                  form_url, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        # Write pub_date on save.
        if obj.pub_date is None:
            obj.pub_date = timezone.now()
        obj.save()

    # def has_change_permission(self, request, obj=None):
    # return obj is None or self.queryset(request).filter(pk=obj.pk).count() > 0

    # def queryset(self, request):
    # query = super(StigAdmin, self).queryset(request)
    #    if request.user.is_superuser:
    #        return query
    #    else:
    #        if request.user.has_perm('stigs_web.change_own_stig'):
    #            return query.filter(users__username__exact=request.user)
    #        else:
    #            return query.filter(users__id__exact=0)

    def has_delete_permission(self, request, obj=None):
        # Don't allow users to delete a stig if they are not the owners.
        if obj is not None:
            if request.user.is_superuser:
                return True
            else:
                if request.user.has_perm('stigs_web.delete_own_stig'):
                    return obj.is_owner(obj, request.user)
                else:
                    return False
        else:
            return False


# Register your models here.
admin.site.register(Stig, StigAdmin)