from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'joined_date')
    list_filter = ('joined_date',)
    search_fields = ('first_name', 'last_name', 'phone')
    ordering = ('last_name', 'first_name')

# Register your models here.
admin.site.register(Member, MemberAdmin)
