from django.contrib.gis.db import models
from django.contrib.auth.models import User, Group
from datetime import datetime

class PrPerson(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=64, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='person_created_by')
    modified_by = models.ForeignKey(User, null=True, blank=True, related_name='person_modified_by')
    deleted = models.CharField(max_length=3, blank=True)
    #pr_pe = models.ForeignKey(PrPentity, null=True, blank=True)
    pr_pe_label = models.CharField(max_length=384, blank=True)
    missing = models.CharField(max_length=3, blank=True)
    first_name = models.CharField(max_length=512)
    middle_name = models.CharField(max_length=512, blank=True)
    last_name = models.CharField(max_length=512, blank=True)
    preferred_name = models.CharField(max_length=512, blank=True)
    local_name = models.CharField(max_length=512, blank=True)
    opt_pr_gender = models.IntegerField(null=True, blank=True)
    opt_pr_age_group = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=384, blank=True)
    mobile_phone = models.CharField(max_length=512, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    opt_pr_nationality = models.IntegerField(null=True, blank=True)
    opt_pr_country = models.IntegerField(null=True, blank=True)
    opt_pr_religion = models.IntegerField(null=True, blank=True)
    opt_pr_marital_status = models.IntegerField(null=True, blank=True)
    occupation = models.CharField(max_length=512, blank=True)
    comment = models.CharField(max_length=512, blank=True)
    objects = models.GeoManager()
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
    class Meta:
	verbose_name = "Person"
	verbose_name_plural = "People"


class OrOrganisation(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=64, null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(unique=True, max_length=384)
    acronym = models.CharField(max_length=24, blank=True)
    type = models.IntegerField(null=True, blank=True)
    sector_id = models.CharField(max_length=512, blank=True)
    admin = models.ForeignKey(Group, null=True, blank=True)
    country = models.IntegerField(null=True, blank=True)
    website = models.CharField(max_length=512, blank=True)
    twitter = models.CharField(max_length=512, blank=True)
    donation_phone = models.CharField(max_length=512, blank=True)
    comments = models.TextField(blank=True)
    #source = models.ForeignKey(S3Source, null=True, blank=True)
    objects = models.GeoManager()
    class Meta:
	verbose_name = "Organization"

EMS_TRAFFIC_STATUS_CHOICES = (
	(1, 'Normal'),
	(2, 'Advisory'),
	(3, 'Closed'),
	(4, 'Not Applicable'),
)

FACILITY_STATUS_CHOICES = (	
	(1, "Normal"),
	(2, "Compromised"),
	(3, "Evacuating"),
	(4, "Closed"),
)

CLINICAL_STATUS_CHOICES = (	
	(1, "Normal"),
	(2, "Full"),
	(3, "Closed"),
)

MORGUE_STATUS_CHOICES = (
	(1, "Open"),
	(2, "Full"),
	(3, "Exceeded"),
	(4, "Closed"),
)

SECURITY_STATUS_CHOICES = (
	(1, "Normal"),
	(2, "Elevated"),
	(3, "Restricted Access"),
	(4, "Lockdown"),
	(5, "Quarantine"),
	(6, "Closed"),
)

STAFFING_STATUS_CHOICES = (	
	(1, "Adequate"),
	(2, "Insufficient"),
)

OR_STATUS_CHOICES = (	
	(1, "Adequate"),
	(2, "Insufficient"),
)

FACILITY_OPERATIONS_CHOICES = (	
	(1, "Adequate"),
	(2, "Insufficient"),
)

CLINICAL_OPERATIONS_CHOICES = (	
	(1, "Adequate"),
	(2, "Insufficient"),
)

class HmsHospital(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=64, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='hospital_created_by')
    modified_by = models.ForeignKey(User, null=True, blank=True, related_name='hospital_modified_by')
    deleted = models.CharField(max_length=1, blank=True)
    name = models.CharField(max_length=512)
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    location = models.PointField(srid=4326,null=True,blank=True)
    address = models.CharField(max_length=512, blank=True)
    postcode = models.CharField(max_length=512, blank=True)
    city = models.CharField(max_length=512, blank=True)
    phone_business = models.CharField(max_length=512, blank=True)
    phone_emergency = models.CharField(max_length=512, blank=True)
    email = models.CharField(max_length=512, blank=True)
    fax = models.CharField(max_length=512, blank=True)
    total_beds = models.IntegerField(null=True, blank=True)
    available_beds = models.IntegerField(null=True, blank=True)
    ems_status = models.IntegerField(null=True, blank=True, choices=EMS_TRAFFIC_STATUS_CHOICES)
    ems_reason = models.CharField(max_length=128, null=True, blank=True)
    facility_status = models.IntegerField(null=True, blank=True, choices=FACILITY_STATUS_CHOICES)
    clinical_status = models.IntegerField(null=True, blank=True, choices=CLINICAL_STATUS_CHOICES)
    morgue_status = models.IntegerField(null=True, blank=True, choices=MORGUE_STATUS_CHOICES)
    morgue_units = models.IntegerField(null=True, blank=True)
    security_status = models.IntegerField(null=True, blank=True, choices=SECURITY_STATUS_CHOICES)
    doctors = models.IntegerField(null=True, blank=True)
    nurses = models.IntegerField(null=True, blank=True)
    non_medical_staff = models.IntegerField(null=True, blank=True)
    staffing = models.IntegerField(null=True, blank=True, choices=STAFFING_STATUS_CHOICES)
    facility_operations = models.IntegerField(null=True, blank=True, choices=FACILITY_OPERATIONS_CHOICES)
    clinical_operations = models.IntegerField(null=True, blank=True, choices=CLINICAL_OPERATIONS_CHOICES)
    comments = models.TextField(blank=True)
    or_status = models.IntegerField(null=True, blank=True, choices=OR_STATUS_CHOICES)
    phone_exchange = models.CharField(max_length=512, blank=True)
    aka2 = models.CharField(max_length=512, blank=True)
    aka1 = models.CharField(max_length=512, blank=True)
    facility_type = models.IntegerField(null=True, blank=True)
    access_status = models.CharField(max_length=512, null=True, blank=True)
    or_reason = models.CharField(max_length=128, null=True, blank=True)
    gov_uuid = models.CharField(max_length=128, null=True, blank=True)
    website = models.CharField(max_length=512, null=True, blank=True)
    info_source = models.CharField(max_length=512, null=True, blank=True)
    objects = models.GeoManager()
    def __unicode__(self):
        return self.name
    class Meta:
	verbose_name = "Hospital"
	

BED_TYPE_CHOICES = (
	(1, "Adult ICU"),
	(2, "Pediatric ICU"),
	(3, "Neonatal ICU"),
	(4, "Emergency Department"),
	(5, "Nursery Beds"),
	(6, "General Medical/Surgical"),
	(7, "Rehabilitation/Long Term Care"),
	(8, "Burn ICU"),
	(9, "Pediatrics"),
	(10, "Adult Psychiatric"),
	(11, "Pediatric Psychiatric"),
	(12, "Negative Flow Isolation"),
	(13, "Other Isolation"),
	(14, "Operating Rooms"),
	(99, "Other"),
)

class HmsBedCapacity(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=64, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='hbc_created_by')
    modified_by = models.ForeignKey(User, null=True, blank=True, related_name='hbc_modified_by')
    deleted = models.CharField(max_length=3, blank=True)
    hospital = models.ForeignKey(HmsHospital, null=True, blank=True)
    unit_name = models.CharField(max_length=64, blank=True)
    bed_type = models.IntegerField(null=True, blank=True, choices=BED_TYPE_CHOICES)
    date = models.DateTimeField(null=True, blank=True)
    beds_baseline = models.IntegerField(null=True, blank=True, verbose_name="Baseline number of beds")
    beds_available = models.IntegerField(null=True, blank=True, verbose_name="Available Beds")
    beds_add24 = models.IntegerField(null=True, blank=True, verbose_name="Additional Beds in the past 24 Hours")
    comment = models.CharField(max_length=128, blank=True)
    objects = models.GeoManager()
    class Meta:
	verbose_name = "Hospital Bed Capacity"
	verbose_name_plural = "Hospital Bed Capacities"

class HmsContact(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    deleted = models.CharField(max_length=1, blank=True)
    hospital = models.ForeignKey(HmsHospital, null=True, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    title = models.CharField(max_length=512, blank=True)
    phone1 = models.CharField(max_length=512, blank=True)
    phone2 = models.CharField(max_length=512, blank=True)
    email = models.CharField(max_length=512, blank=True)
    fax = models.CharField(max_length=512, blank=True)
    skype = models.CharField(max_length=512, blank=True)
    objects = models.GeoManager()
    class Meta:
	verbose_name = "Hospital Contact"

class HmsActivity(models.Model):
    created_on = models.DateTimeField(null=True, blank=True,default=datetime.now())
    modified_on = models.DateTimeField(null=True, blank=True,default=datetime.now())
    uuid = models.CharField(unique=True, max_length=64, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='hmsactivity_created_by')
    modified_by = models.ForeignKey(User, null=True, blank=True, related_name='hmsactivity_modified_by')
    deleted = models.CharField(max_length=1, blank=True)
    hospital = models.ForeignKey(HmsHospital, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    patients = models.IntegerField(null=True, blank=True)
    admissions24 = models.IntegerField(null=True, blank=True, verbose_name="Admissions in the past 24 hours")
    discharges24 = models.IntegerField(null=True, blank=True, verbose_name="Discharges in the past 24 hours")
    deaths24 = models.IntegerField(null=True, blank=True, verbose_name="Deaths in the past 24 hours")
    comment = models.CharField(max_length=128, blank=True)
    objects = models.GeoManager()
    class Meta:
	verbose_name = "Hospital Activity"
	verbose_name_plural = "Hospital Activities"

class HmsResource(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=64, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='hmsresource_created_by')
    modified_by = models.ForeignKey(User, null=True, blank=True, related_name='hmsresource_modified_by')
    deleted = models.CharField(max_length=1, blank=True)
    hospital = models.ForeignKey(HmsHospital, null=True, blank=True)
    type = models.CharField(max_length=512, blank=True)
    description = models.CharField(max_length=512, blank=True)
    quantity = models.CharField(max_length=512, blank=True)
    comment = models.CharField(max_length=512, blank=True)
    objects = models.GeoManager()
    class Meta:
	verbose_name = "Hospital Resource"

class HmsService(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=64, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='hmss_created_by')
    modified_by = models.ForeignKey(User, null=True, blank=True, related_name='hmss_modified_by')
    deleted = models.CharField(max_length=1, blank=True)
    hospital = models.ForeignKey(HmsHospital, null=True, blank=True)
    burn = models.BooleanField(verbose_name="Burn Unit")
    card = models.BooleanField(verbose_name="Cardiology")
    dial = models.BooleanField(verbose_name="Dialysis")
    emsd = models.BooleanField(verbose_name="Emergency Department")
    infd = models.BooleanField(verbose_name="Infectious Diseases")
    neon = models.BooleanField(verbose_name="Neonatology")
    neur = models.BooleanField(verbose_name="Neurology")
    pedi = models.BooleanField(verbose_name="Pediatrics")
    surg = models.BooleanField(verbose_name="Surgery")
    labs = models.BooleanField(verbose_name="Clinical Laboratory")
    tran = models.BooleanField(verbose_name="Ambulance Services")
    tair = models.BooleanField(verbose_name="Air Transport Service")
    trac = models.BooleanField(verbose_name="Trauma Center")
    psya = models.BooleanField(verbose_name="Psychiatrics/Adult")
    psyp = models.BooleanField(verbose_name="Psychiatrics/Pediatric")
    obgy = models.BooleanField(verbose_name="Obstetrics/Gynecology")
    objects = models.GeoManager()
    class Meta:
	verbose_name = "Hospital Service"

REQUEST_TYPE_CHOICES = (
	(1, "Water"),
	(2, "Power"),
	(3, "Food"),
	(4, "Medical Supplies"),
	(5, "Medical Staff"),
	(6, "Non-medical Staff"),
	(7, "Security"),
	(8, "Transport"),
	(9, "Fuel"),
	(99, "Other"),
)

REQUEST_IMPACT_CHOICES = (
	(1, "Highly Critical"),
	(2, "critical"),
	(3, "not critical"),
)

PRIORITY_STATUS_CHOICES = (
	(1, "immediately"),
	(2, "urgent"),
	(3, "high"),
	(4, "normal"),
	(5, "low"),
)

REQUEST_STATUS_CHOICES = (
	(1, "open"),
	(2, "compensated"),
	(3, "feedback"),
	(4, "remedied"),
)

REQUEST_STATUS_CHOICES = (
	(1, "new"),
	(2, "reviewed"),
	(3, "deffered"),
	(4, "accepted"),
	(5, "invalid"),
)

class HmsRequest(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=64, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='hmsrequest_created_by')
    modified_by = models.ForeignKey(User, null=True, blank=True, related_name='hmsrequest_modified_by')
    deleted = models.CharField(max_length=1, blank=True)
    hospital = models.ForeignKey(HmsHospital, null=True, blank=True)
    subject = models.CharField(max_length=512, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    type = models.IntegerField(null=True, blank=True, choices=REQUEST_TYPE_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_STATUS_CHOICES, default=4)
    city = models.CharField(max_length=512, blank=True, null=True)
    status = models.IntegerField(choices=REQUEST_STATUS_CHOICES, default=1)
    completed = models.BooleanField()
    source_type = models.IntegerField(null=True, blank=True)
    actionable = models.BooleanField()
    verified = models.BooleanField()
    verified_by = models.ForeignKey(User, null=True, blank=True, related_name='verified_by')
    verified_date = models.DateTimeField(null=True, blank=True)
    objects = models.GeoManager()
    class Meta:
	verbose_name = "Hospital Request"

IMAGE_TYPE_CHOICES = (
	(1, 'Photograph'),
	(2, 'Map'),
	(3, 'Document Scan'),
	(99, 'Other'),
)

SUPPLY_TYPE_CHOICES = (
  (1, 'AMPULE'),
  (2, 'VIAL'),
  (3, 'TAB'),
  (4, 'BOT'),
  (5, 'TUBE'),
  (6, 'BOT'),
  (7, 'MILLE'),
  (8, 'EA'),
  (9, 'LITRE'),
)


class HmsRequestItem(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=64, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='hmsrequest_created_by')
    modified_by = models.ForeignKey(User, null=True, blank=True, related_name='hmsrequest_modified_by')
    deleted = models.CharField(max_length=1, blank=True)
    request = models.ForeignKey(HmsRequest, null=True, blank=True)
    item = models.CharField(max_length=512, blank=True, null=True)
    unit = models.CharField(max_length=128, blank=true, null=True)
    quanity = models.IntegerField(null=True, blank=True)
    item_id = models.CharField(max_length=512, blank=True, blank=True)
    item_category = models.CharField(max_length=512, blank=True, blank=True)
  verbose_name = "Medical Supply"
  verbose_name_plural = "Medical Supplies"
    
  
  
class HmsImage(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=64, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='hmsimage_created_by')
    modified_by = models.ForeignKey(User, null=True, blank=True, related_name='hmsimage_modified_by')
    deleted = models.CharField(max_length=1, blank=True)
    hospital = models.ForeignKey(HmsHospital)
    type = models.IntegerField(null=True, blank=True, choices=IMAGE_TYPE_CHOICES)
    image = models.ImageField(null=True, blank=True, max_length=255, upload_to='images')
    url = models.CharField(max_length=512, null=True, blank=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    tags = models.CharField(max_length=512, null=True, blank=True)
    objects = models.GeoManager()
    class Meta:
	verbose_name = "Hospital Image"
	verbose_name_plural = "Hospital Images"

class OrOffice(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=64, null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(max_length=512)
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    admin = models.ForeignKey(Group, null=True, blank=True)
    location = models.PointField(srid=4326,null=True,blank=True)
    parent = models.ForeignKey('self', null=True, blank=True)
    address = models.TextField(blank=True)
    postcode = models.CharField(max_length=512, blank=True)
    phone1 = models.CharField(max_length=512, blank=True)
    phone2 = models.CharField(max_length=512, blank=True)
    email = models.CharField(max_length=512, blank=True)
    fax = models.CharField(max_length=512, blank=True)
    national_staff = models.IntegerField(null=True, blank=True)
    international_staff = models.IntegerField(null=True, blank=True)
    number_of_vehicles = models.IntegerField(null=True, blank=True)
    vehicle_types = models.CharField(max_length=512, blank=True)
    equipment = models.CharField(max_length=512, blank=True)
    #source = models.ForeignKey(S3Source, null=True, blank=True)
    comments = models.TextField(blank=True)
    objects = models.GeoManager()
    class Meta:
	verbose_name = "Organization Office"

class OrActivity(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    location = models.PointField(srid=4326,null=True,blank=True)
    sector_id = models.CharField(max_length=512, blank=True)
    description = models.CharField(max_length=512, blank=True)
    beneficiaries = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    funded = models.CharField(max_length=3, blank=True)
    budgeted_cost = models.FloatField(null=True, blank=True)
    objects = models.GeoManager()
    class Meta:
	verbose_name = "Organization Activity"
	verbose_name = "Organization Activities"

class OrContact(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True, related_name='person')
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    office = models.ForeignKey(OrOffice, null=True, blank=True)
    title = models.CharField(max_length=512, blank=True)
    manager = models.ForeignKey(PrPerson, null=True, blank=True, related_name='manager')
    focal_point = models.CharField(max_length=3, blank=True)
    #source = models.ForeignKey(S3Source, null=True, blank=True)
    comments = models.TextField(blank=True)
    objects = models.GeoManager()
    class Meta:
	verbose_name = "Organization Contact"

class OrProject(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    location = models.PointField(srid=4326,null=True,blank=True)
    sector_id = models.CharField(max_length=512, blank=True)
    title = models.CharField(max_length=512, blank=True)
    description = models.CharField(max_length=512, blank=True)
    beneficiaries = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    funded = models.CharField(max_length=3, blank=True)
    budgeted_cost = models.FloatField(null=True, blank=True)
    objects = models.GeoManager()
    class Meta:
	verbose_name = "Organization Project"

class OrSector(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=64, null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(unique=True, max_length=384)
    service_id = models.CharField(max_length=512, blank=True)
    objects = models.GeoManager()
    class Meta:
	verbose_name = "Organization Sector"

class OrService(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=64, null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(unique=True, max_length=384)
    objects = models.GeoManager()
    class Meta:
	verbose_name = "Organization Service"

class RmsReq(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=64, null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    message = models.TextField(blank=True)
    hospital = models.ForeignKey(HmsHospital, null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    verified = models.CharField(max_length=3, blank=True)
    city = models.CharField(max_length=512, blank=True)
    completion_status = models.CharField(max_length=3, blank=True)
    source_type = models.IntegerField(null=True, blank=True)
    source_id = models.IntegerField(null=True, blank=True)
    actionable = models.CharField(max_length=3, blank=True)
    objects = models.GeoManager()
    class Meta:
	verbose_name = "Requirements"

class RmsPledge(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='created_by')
    modified_by = models.ForeignKey(User, null=True, blank=True, related_name='modified_by')
    uuid = models.CharField(unique=True, max_length=64, null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    submitted_on = models.DateTimeField(null=True, blank=True)
    req = models.ForeignKey(RmsReq, null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    objects = models.GeoManager()
    class Meta:
	verbose_name = "Requirement Pledge"

class RmsSmsRequest(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=64, null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    pledge = models.IntegerField(null=True, blank=True)
    sms = models.CharField(max_length=512, blank=True)
    notes = models.CharField(max_length=512, blank=True)
    phone = models.CharField(max_length=512, blank=True)
    ush_id = models.CharField(max_length=512, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=512, blank=True)
    categorization = models.CharField(max_length=512, blank=True)
    location = models.PointField(srid=4326,null=True,blank=True)
    status = models.CharField(max_length=512, blank=True)
    smsrec = models.IntegerField(null=True, blank=True)
    author = models.CharField(max_length=512, blank=True)
    category_term = models.CharField(max_length=512, blank=True)
    firstname = models.CharField(max_length=512, blank=True)
    lastname = models.CharField(max_length=512, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=512, blank=True)
    department = models.CharField(max_length=512, blank=True)
    summary = models.CharField(max_length=512, blank=True)
    link = models.CharField(max_length=512, blank=True)
    actionable = models.CharField(max_length=3, blank=True)
    objects = models.GeoManager()
    class Meta:
	verbose_name = "SMS Request"

class RmsTweetRequest(models.Model):
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=64, null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    pledge = models.IntegerField(null=True, blank=True)
    details = models.CharField(max_length=512, blank=True)
    tweet = models.CharField(max_length=512, blank=True)
    author = models.CharField(max_length=512, blank=True)
    updated = models.CharField(max_length=512, blank=True)
    link = models.CharField(max_length=512, blank=True)
    ttt_id = models.CharField(max_length=512, blank=True)
    objects = models.GeoManager()
    class Meta:
	verbose_name = "Tweet Request"
