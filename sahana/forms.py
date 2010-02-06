from sahana.models import *
from django.forms import ModelForm

class HospitalBedCapacityForm(ModelForm):
    class Meta:
        model = HmsBedCapacity
	exclude = ('hospital', 'created_by', 'modified_by', 'created_on','modified_on', 'uuid', 'deleted',)

class HospitalRequestForm(ModelForm):
    class Meta:
        model = HmsRequest
	exclude = ('hospital', 'created_by', 'timestamp', 'modified_by', 'created_on','modified_on', 'uuid', 'deleted','actionable', 'verified', 'verified_by', 'verified_date', 'completed', 'source_type')

class HospitalContactForm(ModelForm):
    class Meta:
        model = HmsContact
	exclude = ('hospital', 'created_by', 'modified_by', 'created_on','modified_on', 'uuid', 'deleted',)

class HospitalResourceForm(ModelForm):
    class Meta:
        model = HmsResource
	exclude = ('hospital', 'created_by', 'modified_by', 'created_on','modified_on', 'uuid', 'deleted',)

class HospitalServiceForm(ModelForm):
    class Meta:
        model = HmsService
	exclude = ('hospital', 'created_by', 'modified_by', 'created_on','modified_on', 'uuid', 'deleted',)

class HospitalActivityForm(ModelForm):
    class Meta:
        model = HmsActivity
	exclude = ('hospital', 'created_by', 'modified_by', 'created_on','modified_on', 'uuid', 'deleted',)

class PersonForm(ModelForm):
    class Meta:
        model = PrPerson 
	exclude = ('created_on','created_by', 'modified_by', 'modified_on', 'uuid', 'deleted',)

