from mednet.ushahidi.models import * 
from django.contrib.gis import admin

class CategoryAdmin(admin.OSMGeoAdmin):
    list_display = ('ushahidi_id', 'title', 'description', 'color', 'icon')
    

class CountryAdmin(admin.OSMGeoAdmin):
    list_display = ('ushahidi_id', 'iso', 'name', 'capital')


class LocationAdmin(admin.OSMGeoAdmin):
    list_display = ('ushahidi_id', 'name', 'description', 'country', 'point')
    

class IncidentAdmin(admin.OSMGeoAdmin):
    list_display = ('ushahidi_id', 'title', 'description', 'date_time', 'mode', 'active', 'verified', 'location')
    list_filter = ('categories','verified','active')
    search_fields = ('title', 'description')




admin.site.register(Category, CategoryAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Incident, IncidentAdmin)
