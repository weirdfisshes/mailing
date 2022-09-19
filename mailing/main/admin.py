from django.contrib import admin

from .models import Client, Mailing, Message


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'mobile_code', 'tag', 'time_zone')
    search_fields = ('phone_number',)
    list_filter = ('id',)


class MailingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'start_date', 'stop_date',
        'text', 'mobile_code', 'tag'
    )
    search_fields = ('text',)
    list_filter = ('id',)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'status', 'mailing', 'client')
    search_fields = ('mailing',)
    list_filter = ('id',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Mailing, MailingAdmin)
admin.site.register(Message, MessageAdmin)
