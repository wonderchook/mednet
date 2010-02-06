from mednet.sahana.models import * 
from django.contrib.gis import admin

class HmsHospitalAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'city', 'phone_business', 'phone_emergency', 'ems_status', 'facility_status', 'clinical_status', 'security_status')
    search_fields = ('name', 'comments', 'phone_business', 'phone_emergency', 'email')
    list_filter = ('facility_status', 'clinical_status', 'security_status')

class HmsActivityAdmin(admin.OSMGeoAdmin):
    list_display = ('pk', 'hospital', 'date', 'comment')
    search_fields = ('comment',)

class HmsBedCapacityAdmin(admin.OSMGeoAdmin):
    list_display = ('pk', 'hospital', 'bed_type', 'date','beds_baseline', 'beds_available', 'beds_add24')
    search_fields = ('comment',)

class HmsContactAdmin(admin.OSMGeoAdmin):
    list_display = ('pk', 'hospital', 'person', 'title','phone1', 'phone2', 'email')

class HmsImageAdmin(admin.OSMGeoAdmin):
    list_display = ('pk', 'hospital', 'type', 'image','description')
    search_fields = ('description',)

class HmsRequestAdmin(admin.OSMGeoAdmin):
    list_display = ('pk', 'hospital', 'subject', 'timestamp','type', 'priority', 'status')
    list_filter = ('priority', 'status', 'completed', 'actionable', 'verified')
    search_fields = ('description',)

class HmsResourceAdmin(admin.OSMGeoAdmin):
    list_display = ('pk', 'hospital', 'type','description', 'quantity')
    search_fields = ('description','comment')

class HmsServiceAdmin(admin.OSMGeoAdmin):
    list_display = ('pk', 'hospital', 'burn','card','dial','emsd')
    list_filter = ('burn', 'card', 'dial', 'emsd', 'infd', 'neon', 'neur','pedi','surg','labs','tran','tair','trac','psya','psyp','obgy')

admin.site.register(PrPerson)
admin.site.register(OrOrganisation)
admin.site.register(HmsHospital, HmsHospitalAdmin)
admin.site.register(HmsBedCapacity, HmsBedCapacityAdmin)
admin.site.register(HmsContact, HmsContactAdmin)
admin.site.register(HmsActivity, HmsActivityAdmin)
admin.site.register(HmsImage, HmsImageAdmin)
admin.site.register(HmsResource, HmsResourceAdmin)
admin.site.register(HmsService, HmsServiceAdmin)
admin.site.register(HmsRequest, HmsRequestAdmin)
admin.site.register(OrOffice)
admin.site.register(OrActivity)
admin.site.register(OrContact)
admin.site.register(OrProject)
admin.site.register(OrSector)
admin.site.register(OrService)
admin.site.register(RmsReq)
admin.site.register(RmsPledge)
admin.site.register(RmsSmsRequest)
admin.site.register(RmsTweetRequest)
