from django.contrib import admin
from django.contrib.auth.models import User, Group

admin.site.unregister((User, Group))

admin.site.site_header = 'Страница администратора soAktau'
admin.site.site_title = 'Aktau'
admin.site.index_title = 'Страница администратора'
admin.site.disable_action('delete_selected')
