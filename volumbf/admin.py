from django.contrib import admin

from .models import Mentions, Stones, Typ, Authors 

class StonesAdmin(admin.ModelAdmin):
    list_display = ('title', 'legend', 'place', 'typ')
    list_display_links = ('title', 'legend', 'place')
    search_fields = ('title', 'legend', 'place'
                     , 'mentions__work'
                     )

admin.site.register(Stones, StonesAdmin)
admin.site.register(Typ)
admin.site.register(Mentions)
admin.site.register(Authors)
