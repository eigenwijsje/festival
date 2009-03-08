from django.contrib import admin

from models import Event, HardDisk, Memory, Processor, Registrant, Site, Software 

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'scheduled') 
    prepopulated_fields = {'slug': ('name',)}

class RegistrantAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'telephone', 'software')
    list_filter = ('site', 'event')

class SiteAdmin(admin.ModelAdmin):
    filter_horizontal = ('software',)
    list_display = ('name', 'event', 'max_capacity', 'scheduled', 'finished')
    list_filter = ('event',)
    prepopulated_fields = {'slug': ('name',)}

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('software', 'version')

admin.site.register(HardDisk)
admin.site.register(Memory)
admin.site.register(Processor)

admin.site.register(Event, EventAdmin)
admin.site.register(Registrant, RegistrantAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Software, SoftwareAdmin)
