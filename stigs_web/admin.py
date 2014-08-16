from django.contrib import admin
from stigs_web.models import Stig


class StigAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'users', 'location', 'pub_date']
    list_display = ('title', 'creator', 'location', 'pub_date')

# Register your models here.
admin.site.register(Stig, StigAdmin)