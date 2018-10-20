from django.contrib import admin
from django.contrib.auth.models import User, Group
from django_summernote.admin import SummernoteModelAdmin

from main.models import Phone, Address, CompanyInfo, Coordinate, ChatRoom, ChatMessage, Bus, Mail, AddressInfo

admin.site.unregister((User, Group))

admin.site.site_header = 'Страница администратора soAktau'
admin.site.site_title = 'Aktau'
admin.site.index_title = 'Страница администратора'
admin.site.disable_action('delete_selected')


class InfoAdmin(SummernoteModelAdmin):
    summernote_fields = ('info_kaz', 'info_rus')


class PhoneInline(admin.StackedInline):
    model = Phone
    extra = 1


class CoordinateInline(admin.StackedInline):
    model = Coordinate
    extra = 1


class BusInline(admin.StackedInline):
    model = Bus
    extra = 1


class MailInline(admin.StackedInline):
    model = Mail
    extra = 1


class AddressInfoInline(admin.StackedInline):
    model = AddressInfo
    extra = 1


class ChatMessageInline(admin.StackedInline):
    model = ChatMessage
    extra = 1


class AddressAdmin(admin.ModelAdmin):
    inlines = [AddressInfoInline, MailInline, PhoneInline, CoordinateInline, BusInline]


class ChatRoomAdmin(admin.ModelAdmin):
    inlines = [ChatMessageInline, ]


admin.site.register(CompanyInfo, InfoAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(ChatRoom, ChatRoomAdmin)
