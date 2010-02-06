# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class AdminImportJob(models.Model):
    id = models.IntegerField(primary_key=True)
    module = models.CharField(max_length=1536)
    resource = models.CharField(max_length=1536)
    description = models.CharField(max_length=1536)
    source_file = models.CharField(max_length=1536)
    status = models.CharField(max_length=1536, blank=True)
    column_map = models.TextField(blank=True)
    failure_reason = models.CharField(max_length=1536, blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(AuthUser, null=True, db_column='created_by', blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, db_column='modified_by', blank=True)
    class Meta:
        db_table = u'admin_import_job'

class AdminImportLine(models.Model):
    id = models.IntegerField(primary_key=True)
    import_job = models.ForeignKey(AdminImportJob, null=True, db_column='import_job', blank=True)
    line_no = models.IntegerField(null=True, blank=True)
    valid = models.CharField(max_length=3, blank=True)
    errors = models.CharField(max_length=1536, blank=True)
    status = models.CharField(max_length=1536, blank=True)
    data = models.TextField(blank=True)
    class Meta:
        db_table = u'admin_import_line'

class AdminSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'admin_setting'

class AdminTheme(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=1536, blank=True)
    logo = models.CharField(max_length=1536, blank=True)
    footer = models.CharField(max_length=1536, blank=True)
    text_direction = models.CharField(max_length=1536, blank=True)
    col_background = models.CharField(max_length=1536, blank=True)
    col_txt = models.CharField(max_length=1536, blank=True)
    col_txt_background = models.CharField(max_length=1536, blank=True)
    col_txt_border = models.CharField(max_length=1536, blank=True)
    col_txt_underline = models.CharField(max_length=1536, blank=True)
    col_menu = models.CharField(max_length=1536, blank=True)
    col_highlight = models.CharField(max_length=1536, blank=True)
    col_input = models.CharField(max_length=1536, blank=True)
    col_border_btn_out = models.CharField(max_length=1536, blank=True)
    col_border_btn_in = models.CharField(max_length=1536, blank=True)
    col_btn_hover = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'admin_theme'

class AppadminSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'appadmin_setting'

class Atable(models.Model):
    id = models.IntegerField(primary_key=True)
    afield = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'atable'

class AuthEvent(models.Model):
    id = models.IntegerField(primary_key=True)
    time_stamp = models.DateTimeField(null=True, blank=True)
    client_ip = models.CharField(max_length=1536, blank=True)
    user = models.ForeignKey(AuthUser, null=True, blank=True)
    origin = models.CharField(max_length=1536, blank=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = u'auth_event'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=1536, blank=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = u'auth_group'

class AuthMembership(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, null=True, blank=True)
    group = models.ForeignKey(AuthGroup, null=True, blank=True)
    class Meta:
        db_table = u'auth_membership'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup, null=True, blank=True)
    name = models.CharField(max_length=1536, blank=True)
    table_name = models.CharField(max_length=1536, blank=True)
    record_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=384, blank=True)
    last_name = models.CharField(max_length=384, blank=True)
    person_uuid = models.CharField(max_length=192, blank=True)
    utc_offset = models.CharField(max_length=48, blank=True)
    email = models.CharField(max_length=1536, blank=True)
    password = models.CharField(max_length=1536, blank=True)
    registration_key = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'auth_user'

class BudgetBudget(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(unique=True, max_length=384)
    description = models.CharField(max_length=1536, blank=True)
    total_onetime_costs = models.FloatField(null=True, blank=True)
    total_recurring_costs = models.FloatField(null=True, blank=True)
    comments = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'budget_budget'

class BudgetBudgetBundle(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    budget = models.ForeignKey(BudgetBudget, null=True, blank=True)
    project = models.ForeignKey(BudgetProject, null=True, blank=True)
    location = models.ForeignKey(BudgetLocation, null=True, blank=True)
    bundle = models.ForeignKey(BudgetBundle, null=True, blank=True)
    quantity = models.IntegerField()
    months = models.IntegerField()
    class Meta:
        db_table = u'budget_budget_bundle'

class BudgetBudgetStaff(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    budget = models.ForeignKey(BudgetBudget, null=True, blank=True)
    project = models.ForeignKey(BudgetProject, null=True, blank=True)
    location = models.ForeignKey(BudgetLocation, null=True, blank=True)
    staff = models.ForeignKey(BudgetStaff, null=True, blank=True)
    quantity = models.IntegerField()
    months = models.IntegerField()
    class Meta:
        db_table = u'budget_budget_staff'

class BudgetBundle(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(unique=True, max_length=384)
    description = models.CharField(max_length=1536, blank=True)
    total_unit_cost = models.FloatField(null=True, blank=True)
    total_monthly_cost = models.FloatField(null=True, blank=True)
    comments = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'budget_bundle'

class BudgetBundleItem(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    bundle = models.ForeignKey(BudgetBundle, null=True, blank=True)
    item = models.ForeignKey(BudgetItem, null=True, blank=True)
    quantity = models.IntegerField()
    minutes = models.IntegerField()
    megabytes = models.IntegerField()
    class Meta:
        db_table = u'budget_bundle_item'

class BudgetBundleKit(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    bundle = models.ForeignKey(BudgetBundle, null=True, blank=True)
    kit = models.ForeignKey(BudgetKit, null=True, blank=True)
    quantity = models.IntegerField()
    minutes = models.IntegerField()
    megabytes = models.IntegerField()
    class Meta:
        db_table = u'budget_bundle_kit'

class BudgetItem(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    category_type = models.IntegerField()
    code = models.CharField(unique=True, max_length=384)
    description = models.CharField(max_length=1536)
    cost_type = models.IntegerField()
    unit_cost = models.FloatField(null=True, blank=True)
    monthly_cost = models.FloatField(null=True, blank=True)
    minute_cost = models.FloatField(null=True, blank=True)
    megabyte_cost = models.FloatField(null=True, blank=True)
    comments = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'budget_item'

class BudgetKit(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    code = models.CharField(unique=True, max_length=384)
    description = models.CharField(max_length=1536, blank=True)
    total_unit_cost = models.FloatField(null=True, blank=True)
    total_monthly_cost = models.FloatField(null=True, blank=True)
    total_minute_cost = models.FloatField(null=True, blank=True)
    total_megabyte_cost = models.FloatField(null=True, blank=True)
    comments = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'budget_kit'

class BudgetKitItem(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    kit = models.ForeignKey(BudgetKit, null=True, blank=True)
    item = models.ForeignKey(BudgetItem, null=True, blank=True)
    quantity = models.IntegerField()
    class Meta:
        db_table = u'budget_kit_item'

class BudgetLocation(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    code = models.CharField(unique=True, max_length=9)
    description = models.CharField(max_length=1536, blank=True)
    subsistence = models.FloatField(null=True, blank=True)
    hazard_pay = models.FloatField(null=True, blank=True)
    comments = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'budget_location'

class BudgetParameter(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    shipping = models.FloatField()
    logistics = models.FloatField()
    admin = models.FloatField()
    indirect = models.FloatField()
    class Meta:
        db_table = u'budget_parameter'

class BudgetProject(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    code = models.CharField(unique=True, max_length=384)
    title = models.CharField(max_length=1536, blank=True)
    comments = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'budget_project'

class BudgetSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'budget_setting'

class BudgetStaff(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(unique=True, max_length=384)
    grade = models.CharField(max_length=1536)
    salary = models.IntegerField()
    currency_type = models.IntegerField()
    travel = models.IntegerField(null=True, blank=True)
    comments = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'budget_staff'

class CrSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'cr_setting'

class CrShelter(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(max_length=1536)
    description = models.CharField(max_length=1536, blank=True)
    admin = models.ForeignKey(AuthGroup, null=True, db_column='admin', blank=True)
    location = models.ForeignKey(GisLocation, null=True, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    address = models.TextField(blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    dwellings = models.IntegerField(null=True, blank=True)
    persons_per_dwelling = models.IntegerField(null=True, blank=True)
    area = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'cr_shelter'

class DelphiForumPost(models.Model):
    id = models.IntegerField(primary_key=True)
    solution_item = models.ForeignKey(DelphiSolutionItem, null=True, db_column='solution_item', blank=True)
    title = models.CharField(max_length=1536, blank=True)
    post = models.TextField()
    post_html = models.TextField(blank=True)
    user = models.ForeignKey(AuthUser, null=True, db_column='user', blank=True)
    last_modification = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'delphi_forum_post'

class DelphiGrp(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1536)
    description = models.TextField(blank=True)
    moderator = models.ForeignKey(AuthUser, null=True, db_column='moderator', blank=True)
    last_modification = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'delphi_grp'

class DelphiProblem(models.Model):
    id = models.IntegerField(primary_key=True)
    grp = models.ForeignKey(DelphiGrp, null=True, db_column='grp', blank=True)
    title = models.CharField(max_length=1536)
    description = models.TextField(blank=True)
    criteria = models.TextField()
    active = models.CharField(max_length=3, blank=True)
    created_by = models.ForeignKey(AuthUser, null=True, db_column='created_by', blank=True)
    last_modification = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'delphi_problem'

class DelphiSolutionItem(models.Model):
    id = models.IntegerField(primary_key=True)
    problem = models.ForeignKey(DelphiProblem, null=True, db_column='problem', blank=True)
    title = models.CharField(max_length=1536, blank=True)
    description = models.TextField(blank=True)
    suggested_by = models.ForeignKey(AuthUser, null=True, db_column='suggested_by', blank=True)
    last_modification = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'delphi_solution_item'

class DelphiVote(models.Model):
    id = models.IntegerField(primary_key=True)
    problem = models.ForeignKey(DelphiProblem, null=True, db_column='problem', blank=True)
    solution_item = models.ForeignKey(DelphiSolutionItem, null=True, db_column='solution_item', blank=True)
    rank = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(AuthUser, null=True, db_column='user', blank=True)
    last_modification = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'delphi_vote'

class DviBody(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    pr_pe = models.ForeignKey(PrPentity, null=True, blank=True)
    pr_pe_label = models.CharField(max_length=384, blank=True)
    dvi_find = models.ForeignKey(DviFind, null=True, blank=True)
    date_of_recovery = models.DateTimeField(null=True, blank=True)
    location = models.ForeignKey(GisLocation, null=True, blank=True)
    recovery_details = models.TextField(blank=True)
    has_major_outward_damage = models.CharField(max_length=3, blank=True)
    is_burned_or_charred = models.CharField(max_length=3, blank=True)
    is_decayed = models.CharField(max_length=3, blank=True)
    is_incomplete = models.CharField(max_length=3, blank=True)
    opt_pr_gender = models.IntegerField(null=True, blank=True)
    opt_pr_age_group = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'dvi_body'

class DviChecklist(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    pr_pe = models.ForeignKey(PrPentity, null=True, blank=True)
    personal_effects = models.IntegerField(null=True, blank=True)
    body_radiology = models.IntegerField(null=True, blank=True)
    fingerprints = models.IntegerField(null=True, blank=True)
    anthropology = models.IntegerField(null=True, blank=True)
    pathology = models.IntegerField(null=True, blank=True)
    embalming = models.IntegerField(null=True, blank=True)
    dna = models.IntegerField(null=True, blank=True)
    dental = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'dvi_checklist'

class DviEffects(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    pr_pe = models.ForeignKey(PrPentity, null=True, blank=True)
    clothing = models.TextField(blank=True)
    jewellery = models.TextField(blank=True)
    footwear = models.TextField(blank=True)
    watch = models.TextField(blank=True)
    other = models.TextField(blank=True)
    class Meta:
        db_table = u'dvi_effects'

class DviFind(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    find_date = models.DateTimeField(null=True, blank=True)
    location = models.ForeignKey(GisLocation, null=True, blank=True)
    location_details = models.CharField(max_length=1536, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    description = models.CharField(max_length=1536, blank=True)
    bodies_est = models.IntegerField(null=True, blank=True)
    opt_dvi_task_status = models.IntegerField(null=True, blank=True)
    bodies_rcv = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'dvi_find'

class DviIdentification(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    pr_pe = models.ForeignKey(PrPentity, null=True, blank=True)
    identified_by = models.ForeignKey(PrPerson, null=True, db_column='identified_by', blank=True)
    reported_by = models.ForeignKey(PrPerson, null=True, db_column='reported_by', blank=True)
    opt_dvi_id_status = models.IntegerField(null=True, blank=True)
    opt_dvi_id_method = models.IntegerField(null=True, blank=True)
    identity = models.ForeignKey(PrPerson, null=True, db_column='identity', blank=True)
    comment = models.TextField(blank=True)
    class Meta:
        db_table = u'dvi_identification'

class DviSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'dvi_setting'

class DvrSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'dvr_setting'

class GisApikey(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=1536)
    apikey = models.CharField(max_length=384)
    description = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'gis_apikey'

class GisCache(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    name = models.CharField(unique=True, max_length=384)
    file = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'gis_cache'

class GisConfig(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    zoom = models.IntegerField(null=True, blank=True)
    projection = models.ForeignKey(GisProjection, null=True, blank=True)
    symbology = models.ForeignKey(GisSymbology, null=True, blank=True)
    marker = models.ForeignKey(GisMarker, null=True, blank=True)
    map_height = models.IntegerField()
    map_width = models.IntegerField()
    zoom_levels = models.IntegerField()
    cluster_distance = models.IntegerField()
    cluster_threshold = models.IntegerField()
    class Meta:
        db_table = u'gis_config'

class GisFeatureClass(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(unique=True, max_length=384)
    description = models.CharField(max_length=1536, blank=True)
    marker = models.ForeignKey(GisMarker, null=True, blank=True)
    module = models.CharField(max_length=1536, blank=True)
    resource = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'gis_feature_class'

class GisFeatureClassToFeatureGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    feature_group = models.ForeignKey(GisFeatureGroup, null=True, blank=True)
    feature_class = models.ForeignKey(GisFeatureClass, null=True, blank=True)
    class Meta:
        db_table = u'gis_feature_class_to_feature_group'

class GisFeatureGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    created_by = models.ForeignKey(AuthUser, null=True, db_column='created_by', blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, db_column='modified_by', blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(unique=True, max_length=384)
    description = models.CharField(max_length=1536, blank=True)
    enabled = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'gis_feature_group'

class GisLayerGeorss(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=1536)
    description = models.CharField(max_length=1536, blank=True)
    enabled = models.CharField(max_length=3, blank=True)
    url = models.CharField(max_length=1536, blank=True)
    projection = models.ForeignKey(GisProjection, null=True, blank=True)
    marker = models.ForeignKey(GisMarker, null=True, blank=True)
    class Meta:
        db_table = u'gis_layer_georss'

class GisLayerGoogle(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=1536)
    description = models.CharField(max_length=1536, blank=True)
    enabled = models.CharField(max_length=3, blank=True)
    subtype = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'gis_layer_google'

class GisLayerGpx(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=1536)
    description = models.CharField(max_length=1536, blank=True)
    enabled = models.CharField(max_length=3, blank=True)
    track = models.ForeignKey(GisTrack, null=True, blank=True)
    marker = models.ForeignKey(GisMarker, null=True, blank=True)
    class Meta:
        db_table = u'gis_layer_gpx'

class GisLayerJs(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=1536)
    description = models.CharField(max_length=1536, blank=True)
    enabled = models.CharField(max_length=3, blank=True)
    code = models.TextField(blank=True)
    class Meta:
        db_table = u'gis_layer_js'

class GisLayerKml(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=1536)
    description = models.CharField(max_length=1536, blank=True)
    enabled = models.CharField(max_length=3, blank=True)
    url = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'gis_layer_kml'

class GisLayerMgrs(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=1536)
    description = models.CharField(max_length=1536, blank=True)
    enabled = models.CharField(max_length=3, blank=True)
    url = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'gis_layer_mgrs'

class GisLayerOpenstreetmap(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=1536)
    description = models.CharField(max_length=1536, blank=True)
    enabled = models.CharField(max_length=3, blank=True)
    subtype = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'gis_layer_openstreetmap'

class GisLayerTms(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=1536)
    description = models.CharField(max_length=1536, blank=True)
    enabled = models.CharField(max_length=3, blank=True)
    url = models.CharField(max_length=1536, blank=True)
    layers = models.CharField(max_length=1536, blank=True)
    format = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'gis_layer_tms'

class GisLayerWms(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=1536)
    description = models.CharField(max_length=1536, blank=True)
    enabled = models.CharField(max_length=3, blank=True)
    url = models.CharField(max_length=1536, blank=True)
    base = models.CharField(max_length=3, blank=True)
    map = models.CharField(max_length=1536, blank=True)
    layers = models.CharField(max_length=1536, blank=True)
    format = models.CharField(max_length=1536, blank=True)
    transparent = models.CharField(max_length=3, blank=True)
    projection = models.ForeignKey(GisProjection, null=True, blank=True)
    class Meta:
        db_table = u'gis_layer_wms'

class GisLayerXyz(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=1536)
    description = models.CharField(max_length=1536, blank=True)
    enabled = models.CharField(max_length=3, blank=True)
    url = models.CharField(max_length=1536, blank=True)
    base = models.CharField(max_length=3, blank=True)
    sphericalmercator = models.CharField(max_length=3, db_column='sphericalMercator', blank=True) # Field name made lowercase.
    transitioneffect = models.CharField(max_length=1536, db_column='transitionEffect', blank=True) # Field name made lowercase.
    numzoomlevels = models.IntegerField(null=True, db_column='numZoomLevels', blank=True) # Field name made lowercase.
    transparent = models.CharField(max_length=3, blank=True)
    visible = models.CharField(max_length=3, blank=True)
    opacity = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'gis_layer_xyz'

class GisLayerYahoo(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=1536)
    description = models.CharField(max_length=1536, blank=True)
    enabled = models.CharField(max_length=3, blank=True)
    subtype = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'gis_layer_yahoo'

class GisLocation(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(max_length=1536)
    feature_class = models.ForeignKey(GisFeatureClass, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, db_column='parent', blank=True)
    marker = models.ForeignKey(GisMarker, null=True, blank=True)
    gis_feature_type = models.IntegerField()
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    wkt = models.TextField(blank=True)
    osm_id = models.CharField(max_length=1536, blank=True)
    lon_min = models.FloatField(null=True, blank=True)
    lat_min = models.FloatField(null=True, blank=True)
    lon_max = models.FloatField(null=True, blank=True)
    lat_max = models.FloatField(null=True, blank=True)
    admin = models.ForeignKey(AuthGroup, null=True, db_column='admin', blank=True)
    class Meta:
        db_table = u'gis_location'

class GisLocationToFeatureGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    feature_group = models.ForeignKey(GisFeatureGroup, null=True, blank=True)
    location = models.ForeignKey(GisLocation, null=True, blank=True)
    class Meta:
        db_table = u'gis_location_to_feature_group'

class GisMarker(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    name = models.CharField(unique=True, max_length=384)
    image = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'gis_marker'

class GisProjection(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    name = models.CharField(unique=True, max_length=384)
    epsg = models.IntegerField()
    maxextent = models.CharField(max_length=192, db_column='maxExtent') # Field name made lowercase.
    maxresolution = models.FloatField(db_column='maxResolution') # Field name made lowercase.
    units = models.CharField(max_length=1536)
    class Meta:
        db_table = u'gis_projection'

class GisSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'gis_setting'

class GisSymbology(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    name = models.CharField(unique=True, max_length=384)
    class Meta:
        db_table = u'gis_symbology'

class GisSymbologyToFeatureClass(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(unique=True, max_length=384)
    symbology = models.ForeignKey(GisSymbology, null=True, blank=True)
    feature_class = models.ForeignKey(GisFeatureClass, null=True, blank=True)
    marker = models.ForeignKey(GisMarker, null=True, blank=True)
    class Meta:
        db_table = u'gis_symbology_to_feature_class'

class GisTrack(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    name = models.CharField(unique=True, max_length=384)
    description = models.CharField(max_length=384, blank=True)
    track = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'gis_track'

class HmsBedCapacity(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    created_by = models.ForeignKey(AuthUser, null=True, db_column='created_by', blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, db_column='modified_by', blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    hospital = models.ForeignKey(HmsHospital, null=True, blank=True)
    unit_name = models.CharField(max_length=192, blank=True)
    bed_type = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    admissions24 = models.IntegerField(null=True, blank=True)
    discharges24 = models.IntegerField(null=True, blank=True)
    deaths24 = models.IntegerField(null=True, blank=True)
    beds_baseline = models.IntegerField(null=True, blank=True)
    beds_available = models.IntegerField(null=True, blank=True)
    beds_add24 = models.IntegerField(null=True, blank=True)
    comment = models.CharField(max_length=384, blank=True)
    class Meta:
        db_table = u'hms_bed_capacity'

class HmsContact(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    hospital = models.ForeignKey(HmsHospital, null=True, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    title = models.CharField(max_length=1536, blank=True)
    email = models.CharField(max_length=1536, blank=True)
    fax = models.CharField(max_length=1536, blank=True)
    skype = models.CharField(max_length=1536, blank=True)
    phone = models.CharField(max_length=1536, blank=True)
    mobile = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'hms_contact'

class HmsHospital(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(max_length=1536)
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    location = models.ForeignKey(GisLocation, null=True, blank=True)
    address = models.CharField(max_length=1536, blank=True)
    postcode = models.CharField(max_length=1536, blank=True)
    city = models.CharField(max_length=1536, blank=True)
    phone_business = models.CharField(max_length=1536, blank=True)
    phone_emergency = models.CharField(max_length=1536, blank=True)
    email = models.CharField(max_length=1536, blank=True)
    fax = models.CharField(max_length=1536, blank=True)
    total_beds = models.IntegerField(null=True, blank=True)
    available_beds = models.IntegerField(null=True, blank=True)
    ems_status = models.IntegerField(null=True, blank=True)
    ems_reason = models.CharField(max_length=384, blank=True)
    facility_status = models.IntegerField(null=True, blank=True)
    clinical_status = models.IntegerField(null=True, blank=True)
    morgue_status = models.IntegerField(null=True, blank=True)
    morgue_units = models.IntegerField(null=True, blank=True)
    security_status = models.IntegerField(null=True, blank=True)
    doctors = models.IntegerField(null=True, blank=True)
    nurses = models.IntegerField(null=True, blank=True)
    non_medical_staff = models.IntegerField(null=True, blank=True)
    patients = models.IntegerField(null=True, blank=True)
    staffing = models.IntegerField(null=True, blank=True)
    facility_operations = models.IntegerField(null=True, blank=True)
    clinical_operations = models.IntegerField(null=True, blank=True)
    comments = models.TextField(blank=True)
    aka2 = models.CharField(max_length=1536, blank=True)
    aka1 = models.CharField(max_length=1536, blank=True)
    facility_id = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'hms_hospital'

class HmsResources(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    created_by = models.ForeignKey(AuthUser, null=True, db_column='created_by', blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, db_column='modified_by', blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    hospital = models.ForeignKey(HmsHospital, null=True, blank=True)
    type = models.CharField(max_length=1536, blank=True)
    description = models.CharField(max_length=1536, blank=True)
    quantity = models.CharField(max_length=1536, blank=True)
    comment = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'hms_resources'

class HmsServices(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    created_by = models.ForeignKey(AuthUser, null=True, db_column='created_by', blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, db_column='modified_by', blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    hospital = models.ForeignKey(HmsHospital, null=True, blank=True)
    burn = models.CharField(max_length=3, blank=True)
    card = models.CharField(max_length=3, blank=True)
    dial = models.CharField(max_length=3, blank=True)
    emsd = models.CharField(max_length=3, blank=True)
    infd = models.CharField(max_length=3, blank=True)
    neon = models.CharField(max_length=3, blank=True)
    neur = models.CharField(max_length=3, blank=True)
    pedi = models.CharField(max_length=3, blank=True)
    surg = models.CharField(max_length=3, blank=True)
    labs = models.CharField(max_length=3, blank=True)
    tran = models.CharField(max_length=3, blank=True)
    tair = models.CharField(max_length=3, blank=True)
    trac = models.CharField(max_length=3, blank=True)
    psya = models.CharField(max_length=3, blank=True)
    psyp = models.CharField(max_length=3, blank=True)
    obgy = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'hms_services'

class HmsSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'hms_setting'

class HmsShortage(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    created_by = models.ForeignKey(AuthUser, null=True, db_column='created_by', blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, db_column='modified_by', blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    hospital = models.ForeignKey(HmsHospital, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    impact = models.IntegerField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    subject = models.CharField(max_length=1536, blank=True)
    description = models.TextField(blank=True)
    status = models.IntegerField(null=True, blank=True)
    feedback = models.TextField(blank=True)
    class Meta:
        db_table = u'hms_shortage'

class HrmSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'hrm_setting'

class LmsCatalog(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    name = models.CharField(max_length=1536, blank=True)
    description = models.CharField(max_length=1536, blank=True)
    comments = models.TextField(blank=True)
    class Meta:
        db_table = u'lms_catalog'

class LmsCatalogCat(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(max_length=1536, blank=True)
    description = models.CharField(max_length=1536, blank=True)
    comments = models.TextField(blank=True)
    class Meta:
        db_table = u'lms_catalog_cat'

class LmsCatalogSubcat(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    parent_category = models.ForeignKey(LmsCatalogCat, null=True, db_column='parent_category', blank=True)
    name = models.CharField(max_length=1536, blank=True)
    description = models.CharField(max_length=1536, blank=True)
    comments = models.TextField(blank=True)
    class Meta:
        db_table = u'lms_catalog_subcat'

class LmsCategoryMaster(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    category = models.ForeignKey(LmsCatalogCat, null=True, blank=True)
    subcategory = models.ForeignKey(LmsCatalogSubcat, null=True, blank=True)
    catalog = models.ForeignKey(LmsCatalog, null=True, blank=True)
    class Meta:
        db_table = u'lms_category_master'

class LmsItem(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    site = models.ForeignKey(LmsSite, null=True, blank=True)
    storage = models.ForeignKey(LmsStorageLoc, null=True, blank=True)
    bin = models.ForeignKey(LmsStorageBin, null=True, blank=True)
    catalog = models.ForeignKey(LmsCatalog, null=True, db_column='catalog', blank=True)
    way_bill = models.CharField(max_length=1536, blank=True)
    sender_site = models.ForeignKey(LmsSite, null=True, db_column='sender_site', blank=True)
    sender_person = models.CharField(max_length=1536, blank=True)
    recipient_site = models.ForeignKey(LmsSite, null=True, db_column='recipient_site', blank=True)
    recieving_person = models.CharField(max_length=1536, blank=True)
    name = models.CharField(max_length=1536, blank=True)
    description = models.CharField(max_length=1536, blank=True)
    category = models.ForeignKey(LmsCatalogCat, null=True, db_column='category', blank=True)
    sub_category = models.ForeignKey(LmsCatalogSubcat, null=True, db_column='sub_category', blank=True)
    designated = models.CharField(max_length=1536, blank=True)
    quantity_sent = models.FloatField(null=True, blank=True)
    quantity_received = models.FloatField(null=True, blank=True)
    quantity_shortage = models.CharField(max_length=1536, blank=True)
    quantity_unit = models.CharField(max_length=1536, blank=True)
    specifications = models.CharField(max_length=1536, blank=True)
    specifications_unit = models.CharField(max_length=1536, blank=True)
    weight = models.FloatField(null=True, blank=True)
    weight_unit = models.CharField(max_length=1536, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)
    comments = models.TextField(blank=True)
    attachment = models.CharField(max_length=1536, blank=True)
    unit_cost = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'lms_item'

class LmsKit(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    code = models.CharField(unique=True, max_length=384)
    description = models.CharField(max_length=1536, blank=True)
    total_unit_cost = models.FloatField(null=True, blank=True)
    total_monthly_cost = models.FloatField(null=True, blank=True)
    total_minute_cost = models.FloatField(null=True, blank=True)
    total_megabyte_cost = models.FloatField(null=True, blank=True)
    comments = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'lms_kit'

class LmsKitItem(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    kit = models.ForeignKey(LmsKit, null=True, blank=True)
    item = models.ForeignKey(LmsItem, null=True, blank=True)
    quantity = models.IntegerField()
    class Meta:
        db_table = u'lms_kit_item'

class LmsSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'lms_setting'

class LmsShipment(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    way_bill = models.CharField(max_length=1536)
    sender_site = models.ForeignKey(LmsSite, null=True, db_column='sender_site', blank=True)
    sender_person = models.CharField(max_length=1536, blank=True)
    sent_date = models.DateTimeField(null=True, blank=True)
    recipient_site = models.ForeignKey(LmsSite, null=True, db_column='recipient_site', blank=True)
    recieving_person = models.CharField(max_length=1536, blank=True)
    recieved_date = models.DateTimeField(null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)
    currency = models.CharField(max_length=1536, blank=True)
    track_status = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'lms_shipment'

class LmsShipmentItem(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    shipment = models.ForeignKey(LmsShipment, null=True, blank=True)
    item = models.ForeignKey(LmsItem, null=True, blank=True)
    class Meta:
        db_table = u'lms_shipment_item'

class LmsShipmentTransitLogs(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    shipment = models.ForeignKey(LmsShipment, null=True, blank=True)
    item = models.ForeignKey(LmsItem, null=True, blank=True)
    class Meta:
        db_table = u'lms_shipment_transit_logs'

class LmsSite(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(max_length=1536)
    description = models.CharField(max_length=1536, blank=True)
    category = models.IntegerField()
    admin = models.ForeignKey(AuthGroup, null=True, db_column='admin', blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    address = models.TextField(blank=True)
    site_phone = models.CharField(max_length=1536, blank=True)
    site_fax = models.CharField(max_length=1536, blank=True)
    location = models.ForeignKey(GisLocation, null=True, blank=True)
    attachment = models.CharField(max_length=1536, blank=True)
    comments = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'lms_site'

class LmsStorageBin(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    site = models.ForeignKey(LmsSite, null=True, blank=True)
    storage = models.ForeignKey(LmsStorageLoc, null=True, blank=True)
    number = models.CharField(max_length=1536)
    bin_type = models.ForeignKey(LmsStorageBinType, null=True, db_column='bin_type', blank=True)
    capacity = models.CharField(max_length=1536, blank=True)
    capacity_unit = models.CharField(max_length=1536, blank=True)
    max_weight = models.CharField(max_length=1536, blank=True)
    weight_unit = models.CharField(max_length=1536, blank=True)
    attachment = models.CharField(max_length=1536, blank=True)
    comments = models.TextField(blank=True)
    class Meta:
        db_table = u'lms_storage_bin'

class LmsStorageBinType(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(max_length=1536)
    description = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'lms_storage_bin_type'

class LmsStorageLoc(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    site = models.ForeignKey(LmsSite, null=True, blank=True)
    name = models.CharField(max_length=1536)
    description = models.CharField(max_length=1536, blank=True)
    location = models.ForeignKey(GisLocation, null=True, blank=True)
    capacity = models.CharField(max_length=1536, blank=True)
    capacity_unit = models.CharField(max_length=1536, blank=True)
    max_weight = models.CharField(max_length=1536, blank=True)
    weight_unit = models.CharField(max_length=1536, blank=True)
    attachment = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'lms_storage_loc'

class LmsUnit(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    opt_lms_unit_type = models.IntegerField(null=True, blank=True)
    label = models.CharField(max_length=1536, blank=True)
    name = models.CharField(max_length=1536, blank=True)
    base_unit = models.CharField(max_length=1536, blank=True)
    multiplicator = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'lms_unit'

class MediaImage(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    created_by = models.ForeignKey(AuthUser, null=True, db_column='created_by', blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, db_column='modified_by', blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(unique=True, max_length=384)
    location = models.ForeignKey(GisLocation, null=True, blank=True)
    metadata = models.ForeignKey(MediaMetadata, null=True, blank=True)
    image = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'media_image'

class MediaMetadata(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    created_by = models.ForeignKey(AuthUser, null=True, db_column='created_by', blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, db_column='modified_by', blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    location = models.ForeignKey(GisLocation, null=True, blank=True)
    description = models.CharField(max_length=1536, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    source = models.CharField(max_length=1536, blank=True)
    accuracy = models.CharField(max_length=1536, blank=True)
    sensitivity = models.CharField(max_length=1536, blank=True)
    event_time = models.DateTimeField(null=True, blank=True)
    expiry_time = models.DateTimeField(null=True, blank=True)
    url = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'media_metadata'

class MediaSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'media_setting'

class MobileSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    port = models.CharField(max_length=1536, blank=True)
    baud = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'mobile_setting'

class MprMissingPerson(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    pr_pe = models.ForeignKey(PrPentity, null=True, blank=True)
    pr_pe_label = models.CharField(max_length=384, blank=True)
    class Meta:
        db_table = u'mpr_missing_person'

class MprMissingReport(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'mpr_missing_report'

class MprSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'mpr_setting'

class MsgEmailInboundStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'msg_email_inbound_status'

class MsgEmailInbox(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    sender = models.CharField(max_length=1536)
    subject = models.CharField(max_length=234, blank=True)
    body = models.TextField(blank=True)
    class Meta:
        db_table = u'msg_email_inbox'

class MsgEmailOutbox(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(AuthUser, null=True, db_column='created_by', blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, db_column='modified_by', blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    msg_group = models.ForeignKey(MsgGroup, null=True, blank=True)
    subject = models.CharField(max_length=234, blank=True)
    body = models.TextField(blank=True)
    class Meta:
        db_table = u'msg_email_outbox'

class MsgEmailSent(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(AuthUser, null=True, db_column='created_by', blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, db_column='modified_by', blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    msg_group = models.ForeignKey(MsgGroup, null=True, blank=True)
    subject = models.CharField(max_length=234, blank=True)
    body = models.TextField(blank=True)
    class Meta:
        db_table = u'msg_email_sent'

class MsgGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(max_length=1536)
    group_type = models.IntegerField()
    comments = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'msg_group'

class MsgGroupUser(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    msg_group = models.ForeignKey(MsgGroup, null=True, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    class Meta:
        db_table = u'msg_group_user'

class MsgSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    inbound_mail_server = models.CharField(max_length=1536, blank=True)
    inbound_mail_type = models.CharField(max_length=1536, blank=True)
    inbound_mail_ssl = models.CharField(max_length=3, blank=True)
    inbound_mail_port = models.IntegerField(null=True, blank=True)
    inbound_mail_username = models.CharField(max_length=1536, blank=True)
    inbound_mail_password = models.CharField(max_length=1536, blank=True)
    inbound_mail_delete = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'msg_setting'

class MsgSmsInbox(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    phone_number = models.IntegerField()
    contents = models.CharField(max_length=2100, blank=True)
    class Meta:
        db_table = u'msg_sms_inbox'

class MsgSmsOutbox(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(AuthUser, null=True, db_column='created_by', blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, db_column='modified_by', blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    msg_group = models.ForeignKey(MsgGroup, null=True, blank=True)
    contents = models.CharField(max_length=2100, blank=True)
    class Meta:
        db_table = u'msg_sms_outbox'

class MsgSmsSent(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(AuthUser, null=True, db_column='created_by', blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, db_column='modified_by', blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    msg_group = models.ForeignKey(MsgGroup, null=True, blank=True)
    contents = models.CharField(max_length=2100, blank=True)
    class Meta:
        db_table = u'msg_sms_sent'

class NimAnamnesis(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    user = models.ForeignKey(AuthUser, null=True, blank=True)
    shelter = models.ForeignKey(PrPentity, null=True, blank=True)
    opt_nim_care_strategy = models.IntegerField(null=True, blank=True)
    lang_spoken = models.CharField(max_length=1536, blank=True)
    lang_understood = models.CharField(max_length=1536, blank=True)
    lang_comment = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'nim_anamnesis'

class NimCareReportMeasures(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    measures = models.CharField(max_length=768, blank=True)
    report = models.TextField(blank=True)
    class Meta:
        db_table = u'nim_care_report_measures'

class NimCareReportPlanning(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    planning = models.TextField(blank=True)
    class Meta:
        db_table = u'nim_care_report_planning'

class NimCareReportProblems(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    problems = models.TextField(blank=True)
    class Meta:
        db_table = u'nim_care_report_problems'

class NimCareStatusMental(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    status = models.TextField(blank=True)
    class Meta:
        db_table = u'nim_care_status_mental'

class NimCareStatusPhysical(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    user = models.ForeignKey(AuthUser, null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    status = models.TextField(blank=True)
    class Meta:
        db_table = u'nim_care_status_physical'

class NimCareStatusSocial(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    status = models.TextField(blank=True)
    class Meta:
        db_table = u'nim_care_status_social'

class NimDisabilities(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    disabilities = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'nim_disabilities'

class NimDiseases(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    diseases = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'nim_diseases'

class NimInjuries(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    injuries = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'nim_injuries'

class NimSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'nim_setting'

class NimTreatments(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    treatments = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'nim_treatments'

class OrActivity(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    location = models.ForeignKey(GisLocation, null=True, blank=True)
    sector_id = models.CharField(max_length=1536, blank=True)
    description = models.CharField(max_length=1536, blank=True)
    beneficiaries = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    funded = models.CharField(max_length=3, blank=True)
    budgeted_cost = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'or_activity'

class OrOffice(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(max_length=1536)
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    admin = models.ForeignKey(AuthGroup, null=True, db_column='admin', blank=True)
    location = models.ForeignKey(GisLocation, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, db_column='parent', blank=True)
    address = models.TextField(blank=True)
    postcode = models.CharField(max_length=1536, blank=True)
    phone1 = models.CharField(max_length=1536, blank=True)
    phone2 = models.CharField(max_length=1536, blank=True)
    email = models.CharField(max_length=1536, blank=True)
    fax = models.CharField(max_length=1536, blank=True)
    national_staff = models.IntegerField(null=True, blank=True)
    international_staff = models.IntegerField(null=True, blank=True)
    number_of_vehicles = models.IntegerField(null=True, blank=True)
    vehicle_types = models.CharField(max_length=1536, blank=True)
    equipment = models.CharField(max_length=1536, blank=True)
    source = models.ForeignKey(S3Source, null=True, blank=True)
    comments = models.TextField(blank=True)
    class Meta:
        db_table = u'or_office'

class OrContact(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    office = models.ForeignKey(OrOffice, null=True, blank=True)
    title = models.CharField(max_length=1536, blank=True)
    manager = models.ForeignKey(PrPerson, null=True, blank=True)
    focal_point = models.CharField(max_length=3, blank=True)
    source = models.ForeignKey(S3Source, null=True, blank=True)
    comments = models.TextField(blank=True)
    class Meta:
        db_table = u'or_contact'

class OrOrganisation(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(unique=True, max_length=384)
    acronym = models.CharField(max_length=24, blank=True)
    type = models.IntegerField(null=True, blank=True)
    sector_id = models.CharField(max_length=1536, blank=True)
    admin = models.ForeignKey(AuthGroup, null=True, db_column='admin', blank=True)
    country = models.IntegerField(null=True, blank=True)
    website = models.CharField(max_length=1536, blank=True)
    twitter = models.CharField(max_length=1536, blank=True)
    donation_phone = models.CharField(max_length=1536, blank=True)
    comments = models.TextField(blank=True)
    source = models.ForeignKey(S3Source, null=True, blank=True)
    class Meta:
        db_table = u'or_organisation'

class OrProject(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    location = models.ForeignKey(GisLocation, null=True, blank=True)
    sector_id = models.CharField(max_length=1536, blank=True)
    title = models.CharField(max_length=1536, blank=True)
    description = models.CharField(max_length=1536, blank=True)
    beneficiaries = models.IntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    funded = models.CharField(max_length=3, blank=True)
    budgeted_cost = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'or_project'

class OrSector(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(unique=True, max_length=384)
    service_id = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'or_sector'

class OrService(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(unique=True, max_length=384)
    class Meta:
        db_table = u'or_service'

class OrSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'or_setting'

class PrAddress(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    pr_pe = models.ForeignKey(PrPentity, null=True, blank=True)
    opt_pr_address_type = models.IntegerField(null=True, blank=True)
    co_name = models.CharField(max_length=1536, blank=True)
    street1 = models.CharField(max_length=1536, blank=True)
    street2 = models.CharField(max_length=1536, blank=True)
    postcode = models.CharField(max_length=1536, blank=True)
    city = models.CharField(max_length=1536, blank=True)
    state = models.CharField(max_length=1536, blank=True)
    opt_pr_country = models.IntegerField(null=True, blank=True)
    location = models.ForeignKey(GisLocation, null=True, blank=True)
    lat = models.CharField(max_length=1536, blank=True)
    lon = models.CharField(max_length=1536, blank=True)
    comment = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'pr_address'

class PrContact(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    pr_pe = models.ForeignKey(PrPentity, null=True, blank=True)
    name = models.CharField(max_length=1536, blank=True)
    opt_pr_contact_method = models.IntegerField(null=True, blank=True)
    person_name = models.CharField(max_length=1536, blank=True)
    priority = models.CharField(max_length=1536, blank=True)
    value = models.CharField(max_length=1536)
    comment = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'pr_contact'

class PrGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    created_by = models.ForeignKey(AuthUser, null=True, db_column='created_by', blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, db_column='modified_by', blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    pr_pe = models.ForeignKey(PrPentity, null=True, blank=True)
    pr_pe_label = models.CharField(max_length=384, blank=True)
    opt_pr_group_type = models.IntegerField(null=True, blank=True)
    system = models.CharField(max_length=3, blank=True)
    group_name = models.CharField(max_length=1536, blank=True)
    group_description = models.CharField(max_length=1536, blank=True)
    comment = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'pr_group'

class PrGroupMembership(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    group = models.ForeignKey(PrGroup, null=True, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    group_head = models.CharField(max_length=3, blank=True)
    description = models.CharField(max_length=1536, blank=True)
    comment = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'pr_group_membership'

class PrIdentity(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    opt_pr_id_type = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=1536, blank=True)
    value = models.CharField(max_length=1536, blank=True)
    country_code = models.CharField(max_length=12, blank=True)
    ia_name = models.CharField(max_length=1536, blank=True)
    comment = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'pr_identity'

class PrImage(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    pr_pe = models.ForeignKey(PrPentity, null=True, blank=True)
    opt_pr_image_type = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=1536, blank=True)
    image = models.CharField(max_length=1536, blank=True)
    url = models.CharField(max_length=1536, blank=True)
    description = models.CharField(max_length=1536, blank=True)
    comment = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'pr_image'

class PrPdBody(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    pr_pe = models.ForeignKey(PrPentity, null=True, blank=True)
    opt_pr_pd_neck_length = models.IntegerField(null=True, blank=True)
    opt_pr_pd_neck_shape = models.IntegerField(null=True, blank=True)
    opt_pr_pd_neck_peculiarities = models.IntegerField(null=True, blank=True)
    neck_collar_size = models.CharField(max_length=30, blank=True)
    neck_circumference = models.CharField(max_length=30, blank=True)
    opt_pr_pd_hands_shape = models.IntegerField(null=True, blank=True)
    opt_pr_pd_hands_size = models.IntegerField(null=True, blank=True)
    opt_pr_pd_hands_nails_length = models.IntegerField(null=True, blank=True)
    opt_pr_pd_hands_nails_peculiarities = models.IntegerField(null=True, blank=True)
    opt_pr_pd_hands_nicotine = models.IntegerField(null=True, blank=True)
    opt_pr_pd_feet_shape = models.IntegerField(null=True, blank=True)
    pd_feet_size = models.CharField(max_length=1536, blank=True)
    opt_pr_pd_feet_condition = models.IntegerField(null=True, blank=True)
    opt_pr_pd_feet_nails = models.IntegerField(null=True, blank=True)
    feet_peculiarities = models.CharField(max_length=1536, blank=True)
    opt_pr_pd_hair_body_extent = models.IntegerField(null=True, blank=True)
    opt_pr_pd_hair_body_colour = models.IntegerField(null=True, blank=True)
    opt_pr_pd_hair_pubic_extent = models.IntegerField(null=True, blank=True)
    opt_pr_pd_hair_pubic_colour = models.IntegerField(null=True, blank=True)
    circumcision = models.CharField(max_length=3, blank=True)
    opt_pr_pd_smoking_habits = models.IntegerField(null=True, blank=True)
    smoking_stains_teeth = models.CharField(max_length=3, blank=True)
    smoking_stains_lips = models.CharField(max_length=3, blank=True)
    smoking_stains_moustache = models.CharField(max_length=3, blank=True)
    smoking_stains_hand_left = models.CharField(max_length=3, blank=True)
    smoking_stains_hand_right = models.CharField(max_length=3, blank=True)
    specific_details_head = models.CharField(max_length=1536, blank=True)
    specific_details_throat = models.CharField(max_length=1536, blank=True)
    specific_details_arm_left = models.CharField(max_length=1536, blank=True)
    specific_details_arm_right = models.CharField(max_length=1536, blank=True)
    specific_details_hand_left = models.CharField(max_length=1536, blank=True)
    specific_details_hand_right = models.CharField(max_length=1536, blank=True)
    specific_details_body_front = models.CharField(max_length=1536, blank=True)
    specific_details_body_back = models.CharField(max_length=1536, blank=True)
    specific_details_leg_left = models.CharField(max_length=1536, blank=True)
    specific_details_leg_right = models.CharField(max_length=1536, blank=True)
    specific_details_foot_left = models.CharField(max_length=1536, blank=True)
    specific_details_foot_right = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'pr_pd_body'

class PrPdFace(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    pr_pe = models.ForeignKey(PrPentity, null=True, blank=True)
    opt_pr_pd_forehead_height = models.IntegerField(null=True, blank=True)
    opt_pr_pd_forehead_width = models.IntegerField(null=True, blank=True)
    opt_pr_pd_forehead_inclination = models.IntegerField(null=True, blank=True)
    opt_pr_pd_eyebrows_shape = models.IntegerField(null=True, blank=True)
    opt_pr_pd_eyebrows_thickness = models.IntegerField(null=True, blank=True)
    opt_pr_pd_eyebrows_peculiarities = models.IntegerField(null=True, blank=True)
    opt_pr_pd_eyes_colour = models.IntegerField(null=True, blank=True)
    opt_pr_pd_eyes_shade = models.IntegerField(null=True, blank=True)
    opt_pr_pd_eyes_distance = models.IntegerField(null=True, blank=True)
    opt_pr_pd_eyes_peculiarities = models.IntegerField(null=True, blank=True)
    opt_pr_pd_nose_size = models.IntegerField(null=True, blank=True)
    opt_pr_pd_nose_shape = models.IntegerField(null=True, blank=True)
    nose_spectacle_marks = models.CharField(max_length=3, blank=True)
    nose_peculiarities = models.CharField(max_length=1536, blank=True)
    opt_pr_pd_nose_curve = models.IntegerField(null=True, blank=True)
    opt_pr_pd_nose_angle = models.IntegerField(null=True, blank=True)
    opt_pr_pd_hair_facial_type = models.IntegerField(null=True, blank=True)
    opt_pr_pd_hair_facial_colour = models.IntegerField(null=True, blank=True)
    opt_pr_pd_ears_size = models.IntegerField(null=True, blank=True)
    opt_pr_pd_ears_angle = models.IntegerField(null=True, blank=True)
    ears_lobes_attached = models.CharField(max_length=3, blank=True)
    ears_piercings_left = models.IntegerField(null=True, blank=True)
    ears_piercings_right = models.IntegerField(null=True, blank=True)
    opt_pr_pd_mouth_size = models.IntegerField(null=True, blank=True)
    mouth_other = models.CharField(max_length=1536, blank=True)
    opt_pr_pd_lips_shape = models.IntegerField(null=True, blank=True)
    lips_madeup = models.CharField(max_length=3, blank=True)
    lips_other = models.CharField(max_length=1536, blank=True)
    opt_pr_pd_chin_size = models.IntegerField(null=True, blank=True)
    opt_pr_pd_chin_inclination = models.IntegerField(null=True, blank=True)
    opt_pr_pd_chin_shape = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'pr_pd_face'

class PrPdGeneral(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    pr_pe = models.ForeignKey(PrPentity, null=True, blank=True)
    est_age = models.CharField(max_length=1536, blank=True)
    height = models.CharField(max_length=1536, blank=True)
    weight = models.CharField(max_length=1536, blank=True)
    opt_pr_pd_bodily_constitution = models.IntegerField(null=True, blank=True)
    opt_pr_pd_race_group = models.IntegerField(null=True, blank=True)
    race_type = models.CharField(max_length=1536, blank=True)
    opt_pr_pd_race_complexion = models.IntegerField(null=True, blank=True)
    other_peculiarities = models.TextField(blank=True)
    class Meta:
        db_table = u'pr_pd_general'

class PrPdHead(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    pr_pe = models.ForeignKey(PrPentity, null=True, blank=True)
    opt_pr_pd_head_form_front = models.IntegerField(null=True, blank=True)
    opt_pr_pd_head_form_profile = models.IntegerField(null=True, blank=True)
    opt_pr_pd_hair_head_type = models.IntegerField(null=True, blank=True)
    opt_pr_pd_hair_head_length = models.IntegerField(null=True, blank=True)
    opt_pr_pd_hair_head_colour = models.IntegerField(null=True, blank=True)
    opt_pr_pd_hair_head_shade = models.IntegerField(null=True, blank=True)
    opt_pr_pd_hair_head_thickness = models.IntegerField(null=True, blank=True)
    opt_pr_pd_hair_head_style = models.IntegerField(null=True, blank=True)
    opt_pr_pd_hair_head_parting = models.IntegerField(null=True, blank=True)
    opt_pr_pd_hair_head_baldness_ext = models.IntegerField(null=True, blank=True)
    opt_pr_pd_hair_head_baldness_loc = models.IntegerField(null=True, blank=True)
    hair_head_other = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'pr_pd_head'

class PrPdTeeth(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    pr_pe = models.ForeignKey(PrPentity, null=True, blank=True)
    teeth_natural = models.CharField(max_length=3, blank=True)
    teeth_treated = models.CharField(max_length=3, blank=True)
    teeth_crowns = models.CharField(max_length=3, blank=True)
    teeth_bridges = models.CharField(max_length=3, blank=True)
    teeth_implants = models.CharField(max_length=3, blank=True)
    opt_pr_pd_teeth_gaps = models.IntegerField(null=True, blank=True)
    opt_pr_pd_teeth_missing = models.IntegerField(null=True, blank=True)
    opt_pr_pd_teeth_toothless = models.IntegerField(null=True, blank=True)
    opt_pr_pd_teeth_dentures_lower = models.IntegerField(null=True, blank=True)
    opt_pr_pd_teeth_dentures_upper = models.IntegerField(null=True, blank=True)
    teeth_dentures_id = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'pr_pd_teeth'

class PrPentity(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    created_by = models.ForeignKey(AuthUser, null=True, db_column='created_by', blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, db_column='modified_by', blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    opt_pr_entity_type = models.IntegerField(null=True, blank=True)
    label = models.CharField(max_length=384, blank=True)
    class Meta:
        db_table = u'pr_pentity'

class PrPerson(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    created_by = models.ForeignKey(AuthUser, null=True, db_column='created_by', blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, db_column='modified_by', blank=True)
    deleted = models.CharField(max_length=3, blank=True)
    pr_pe = models.ForeignKey(PrPentity, null=True, blank=True)
    pr_pe_label = models.CharField(max_length=384, blank=True)
    missing = models.CharField(max_length=3, blank=True)
    first_name = models.CharField(max_length=1536)
    middle_name = models.CharField(max_length=1536, blank=True)
    last_name = models.CharField(max_length=1536, blank=True)
    preferred_name = models.CharField(max_length=1536, blank=True)
    local_name = models.CharField(max_length=1536, blank=True)
    opt_pr_gender = models.IntegerField(null=True, blank=True)
    opt_pr_age_group = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=384, blank=True)
    mobile_phone = models.CharField(max_length=1536, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    opt_pr_nationality = models.IntegerField(null=True, blank=True)
    opt_pr_country = models.IntegerField(null=True, blank=True)
    opt_pr_religion = models.IntegerField(null=True, blank=True)
    opt_pr_marital_status = models.IntegerField(null=True, blank=True)
    occupation = models.CharField(max_length=1536, blank=True)
    comment = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'pr_person'

class PrPresence(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    pr_pe = models.ForeignKey(PrPentity, null=True, blank=True)
    observer = models.ForeignKey(PrPerson, null=True, db_column='observer', blank=True)
    reporter = models.ForeignKey(PrPerson, null=True, db_column='reporter', blank=True)
    location = models.ForeignKey(GisLocation, null=True, blank=True)
    location_details = models.CharField(max_length=1536, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    opt_pr_presence_condition = models.IntegerField(null=True, blank=True)
    proc_desc = models.CharField(max_length=1536, blank=True)
    orig = models.ForeignKey(GisLocation, null=True, blank=True)
    dest = models.ForeignKey(GisLocation, null=True, blank=True)
    comment = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'pr_presence'

class PrRole(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    pr_pe = models.ForeignKey(PrPentity, null=True, blank=True)
    role = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'pr_role'

class PrSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'pr_setting'

class RmsPledge(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(AuthUser, null=True, db_column='created_by', blank=True)
    modified_by = models.ForeignKey(AuthUser, null=True, db_column='modified_by', blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    submitted_on = models.DateTimeField(null=True, blank=True)
    req = models.ForeignKey(RmsReq, null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    class Meta:
        db_table = u'rms_pledge'

class RmsReq(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    message = models.TextField(blank=True)
    hospital = models.ForeignKey(HmsHospital, null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    verified = models.CharField(max_length=3, blank=True)
    city = models.CharField(max_length=1536, blank=True)
    completion_status = models.CharField(max_length=3, blank=True)
    source_type = models.IntegerField(null=True, blank=True)
    source_id = models.IntegerField(null=True, blank=True)
    actionable = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'rms_req'

class RmsSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'rms_setting'

class RmsSmsRequest(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    pledge = models.IntegerField(null=True, blank=True)
    sms = models.CharField(max_length=1536, blank=True)
    notes = models.CharField(max_length=1536, blank=True)
    phone = models.CharField(max_length=1536, blank=True)
    ush_id = models.CharField(max_length=1536, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=1536, blank=True)
    categorization = models.CharField(max_length=1536, blank=True)
    location = models.ForeignKey(GisLocation, null=True, blank=True)
    status = models.CharField(max_length=1536, blank=True)
    smsrec = models.IntegerField(null=True, blank=True)
    author = models.CharField(max_length=1536, blank=True)
    category_term = models.CharField(max_length=1536, blank=True)
    firstname = models.CharField(max_length=1536, blank=True)
    lastname = models.CharField(max_length=1536, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=1536, blank=True)
    department = models.CharField(max_length=1536, blank=True)
    summary = models.CharField(max_length=1536, blank=True)
    link = models.CharField(max_length=1536, blank=True)
    actionable = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'rms_sms_request'

class RmsTweetRequest(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    pledge = models.IntegerField(null=True, blank=True)
    details = models.CharField(max_length=1536, blank=True)
    tweet = models.CharField(max_length=1536, blank=True)
    author = models.CharField(max_length=1536, blank=True)
    updated = models.CharField(max_length=1536, blank=True)
    link = models.CharField(max_length=1536, blank=True)
    ttt_id = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'rms_tweet_request'

class S3Audit(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    person = models.ForeignKey(AuthUser, null=True, db_column='person', blank=True)
    operation = models.CharField(max_length=1536, blank=True)
    representation = models.CharField(max_length=1536, blank=True)
    module = models.CharField(max_length=1536, blank=True)
    resource = models.CharField(max_length=1536, blank=True)
    record = models.IntegerField(null=True, blank=True)
    old_value = models.CharField(max_length=1536, blank=True)
    new_value = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u's3_audit'

class S3Module(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=96)
    name_nice = models.CharField(unique=True, max_length=384)
    module_type = models.IntegerField()
    access = models.CharField(max_length=1536, blank=True)
    priority = models.IntegerField(unique=True)
    description = models.CharField(max_length=1536, blank=True)
    enabled = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u's3_module'

class S3Setting(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    admin_name = models.CharField(max_length=1536, blank=True)
    admin_email = models.CharField(max_length=1536, blank=True)
    admin_tel = models.CharField(max_length=1536, blank=True)
    utc_offset = models.CharField(max_length=48, blank=True)
    theme = models.ForeignKey(AdminTheme, null=True, db_column='theme', blank=True)
    debug = models.CharField(max_length=3, blank=True)
    self_registration = models.CharField(max_length=3, blank=True)
    security_policy = models.IntegerField(null=True, blank=True)
    archive_not_delete = models.CharField(max_length=3, blank=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u's3_setting'

class S3Source(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    name = models.CharField(max_length=1536, blank=True)
    description = models.CharField(max_length=1536, blank=True)
    url = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u's3_source'

class SyncLog(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(max_length=108, blank=True)
    function = models.CharField(max_length=1536, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    format = models.CharField(max_length=1536, blank=True)
    class Meta:
        db_table = u'sync_log'

class SyncPartner(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(max_length=108, blank=True)
    policy = models.IntegerField()
    username = models.CharField(max_length=1536, blank=True)
    password = models.CharField(max_length=1536, blank=True)
    webservice_port = models.IntegerField(null=True, blank=True)
    rpc_service_url = models.CharField(max_length=1536, blank=True)
    description = models.CharField(max_length=192, blank=True)
    class Meta:
        db_table = u'sync_partner'

class SyncSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(max_length=108, blank=True)
    policy = models.IntegerField()
    username = models.CharField(max_length=1536, blank=True)
    password = models.CharField(max_length=1536, blank=True)
    ip = models.CharField(max_length=1536, blank=True)
    webservice_port = models.IntegerField(null=True, blank=True)
    rpc_service_url = models.CharField(max_length=1536, blank=True)
    zeroconf_description = models.CharField(max_length=192, blank=True)
    class Meta:
        db_table = u'sync_setting'

class VolPosition(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    vol_project = models.ForeignKey(VolProject, null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=90, blank=True)
    description = models.TextField(blank=True)
    slots = models.IntegerField(null=True, blank=True)
    payrate = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'vol_position'

class VolProject(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    name = models.CharField(max_length=150, blank=True)
    location = models.ForeignKey(GisLocation, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    status = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'vol_project'

class VolResource(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    subject = models.IntegerField(null=True, blank=True)
    deployment = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'vol_resource'

class VolSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    audit_read = models.CharField(max_length=3, blank=True)
    audit_write = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'vol_setting'

class VolTask(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    deleted = models.CharField(max_length=3, blank=True)
    vol_project = models.ForeignKey(VolProject, null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    subject = models.CharField(max_length=240, blank=True)
    description = models.TextField(blank=True)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    status = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'vol_task'

class VolVolunteer(models.Model):
    id = models.IntegerField(primary_key=True)
    created_on = models.DateTimeField(null=True, blank=True)
    modified_on = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(unique=True, max_length=192)
    person = models.ForeignKey(PrPerson, null=True, blank=True)
    organisation = models.ForeignKey(OrOrganisation, null=True, blank=True)
    date_avail_start = models.DateField(null=True, blank=True)
    date_avail_end = models.DateField(null=True, blank=True)
    hrs_avail_start = models.TextField(blank=True) # This field type is a guess.
    hrs_avail_end = models.TextField(blank=True) # This field type is a guess.
    status = models.IntegerField(null=True, blank=True)
    special_needs = models.TextField(blank=True)
    class Meta:
        db_table = u'vol_volunteer'

