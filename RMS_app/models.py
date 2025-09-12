from django.db import models
from django.db import connections
from django.db import connections
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class TpmsClientTypeMaster(models.Model):
    ctmid = models.AutoField(primary_key=True)
    client_type_name = models.CharField(max_length=50)
    client_logo = models.CharField(max_length=300)
    id_definition = models.CharField(max_length=20, blank=True, null=True)
    h1name_display = models.CharField(max_length=20, blank=True, null=True)
    h2name_display = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=15)
    client_version = models.CharField(max_length=10)
    created_date = models.DateField()
    updated_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tpms_client_type_master'
class LoginTableForRms(models.Model):
    name = models.CharField(max_length=60)
    user_name = models.CharField(max_length=60)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'login_table_for_rms'

        
# class CommonEnergyData(models.Model):
#     productid = models.CharField(db_column='productId', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     softwarever = models.CharField(db_column='softwareVer', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     hardwarever = models.CharField(db_column='hardwareVer', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     systemmodepiu = models.CharField(db_column='systemModePIU', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     datedd = models.DateField(db_column='dateDD', blank=True, null=True)  # Field name made lowercase.
#     datemm = models.IntegerField(db_column='dateMM', blank=True, null=True)  # Field name made lowercase.
#     dateyy = models.IntegerField(db_column='dateYY', blank=True, null=True)  # Field name made lowercase.
#     datetime = models.TimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
#     reserverd = models.CharField(max_length=100, blank=True, null=True)
#     customerid = models.CharField(db_column='customerId', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     timehh = models.IntegerField(db_column='timeHH', blank=True, null=True)  # Field name made lowercase.
#     timemm = models.IntegerField(db_column='timeMM', blank=True, null=True)  # Field name made lowercase.
#     timess = models.IntegerField(db_column='timeSS', blank=True, null=True)  # Field name made lowercase.
#     mainsvoltr = models.DecimalField(db_column='mainsVoltR', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     mainsvolty = models.DecimalField(db_column='mainsVoltY', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     mainsvoltb = models.DecimalField(db_column='mainsVoltB', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     dgvoltr = models.DecimalField(db_column='dgVoltR', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     dgvolty = models.DecimalField(db_column='dgVoltY', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     dgvoltb = models.DecimalField(db_column='dgVoltB', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     dg2battvolt = models.DecimalField(db_column='dg2BattVolt', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     btsbattvolt = models.DecimalField(db_column='btsBattVolt', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     btsbattcur = models.DecimalField(db_column='btsBattCur', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     dgbattvolt = models.DecimalField(db_column='dgBattVolt', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     curch1 = models.DecimalField(db_column='curCH1', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     curch2 = models.DecimalField(db_column='curCH2', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     curch3 = models.DecimalField(db_column='curCH3', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     curch4 = models.DecimalField(db_column='curCH4', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     dg2lcucurr = models.DecimalField(db_column='dg2LcuCurR', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     dg2lcucury = models.DecimalField(db_column='dg2LcuCurY', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     dg2lcucurb = models.DecimalField(db_column='dg2LcuCurB', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     mainscury = models.DecimalField(db_column='mainsCurY', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     mainscurb = models.DecimalField(db_column='mainsCurB', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     dgcurr = models.DecimalField(db_column='dgCurR', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     dgcury = models.DecimalField(db_column='dgCurY', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     dgcurb = models.DecimalField(db_column='dgCurB', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     alarmdata1 = models.CharField(db_column='alarmData1', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     alarmdata2 = models.CharField(db_column='alarmData2', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     alarmdata3 = models.CharField(db_column='alarmData3', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     alarmdata4 = models.CharField(db_column='alarmData4', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     mains_frequency = models.DecimalField(db_column='Mains_Frequency', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     dgfreq = models.DecimalField(db_column='dgFreq', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lcudg2freq = models.DecimalField(db_column='lcuDg2Freq', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     temperature1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     temperature2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     kwhmains = models.DecimalField(db_column='kwhMains', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     kwhdg1 = models.DecimalField(db_column='kwhDG1', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     kwhdg2 = models.DecimalField(db_column='kwhDG2', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     kwhbts = models.DecimalField(db_column='kwhBTS', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     kwhoperator1 = models.DecimalField(db_column='kwhOperator1', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     kwhoperator2 = models.DecimalField(db_column='kwhOperator2', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     kwhoperator3 = models.DecimalField(db_column='kwhOperator3', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     kwhoperator4 = models.DecimalField(db_column='kwhOperator4', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     companyname = models.CharField(db_column='companyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     source_table = models.CharField(db_column='Source_Table', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     source_detail = models.CharField(db_column='Source_Detail', max_length=100, blank=True, null=True)  # Field name made lowercase.

#     # class Meta:
#     #     managed = False
#     #     db_table = 'common_energy_data'
        

class TpmsClientTypeMaster(models.Model):
    ctmid = models.AutoField(primary_key=True)
    client_type_name = models.CharField(max_length=50)
    client_logo = models.CharField(max_length=300)
    id_definition = models.CharField(max_length=20, blank=True, null=True)
    h1name_display = models.CharField(max_length=20, blank=True, null=True)
    h2name_display = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=15)
    client_version = models.CharField(max_length=10)
    created_date = models.DateField()
    updated_date = models.DateField(blank=True, null=True)
    non_com = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tpms_client_type_master'


class TpmsStateMaster(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=30)
    state_code = models.CharField(max_length=20)
    status = models.CharField(max_length=15)
    created_date = models.DateField()
    updated_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tpms_state_master'


class TpmsDistrictMaster(models.Model):
    dist_id = models.AutoField(primary_key=True)
    state_id = models.IntegerField()
    district_name = models.CharField(max_length=30, blank=True, null=True)
    status = models.TextField()
    created_date = models.DateField()
    updated_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tpms_district_master'


class TpmsClusterMaster(models.Model):
    cluster_id = models.AutoField(primary_key=True)
    dist_id = models.IntegerField()
    state_id = models.IntegerField()
    cluster_name = models.CharField(max_length=30, blank=True, null=True)
    status = models.TextField()
    created_date = models.DateField()
    updated_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tpms_cluster_master'
        
        
class TpmsTrackerMaster(models.Model):
    tracker_id = models.AutoField(primary_key=True)
    ctmid = models.IntegerField()
    simid = models.IntegerField(blank=True, null=True)
    aid_l1 = models.IntegerField(blank=True, null=True)
    aid_l2 = models.IntegerField(blank=True, null=True)
    aid_l3 = models.IntegerField(blank=True, null=True)
    aid_l4 = models.IntegerField(blank=True, null=True)
    aid_l5 = models.IntegerField(blank=True, null=True)
    techid = models.IntegerField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    dist_id = models.IntegerField(blank=True, null=True)
    cluster_id = models.IntegerField(blank=True, null=True)
    gsm_imei_no = models.CharField(unique=True, max_length=50)
    site_name = models.CharField(max_length=50, blank=True, null=True)
    system_serial_no = models.CharField(max_length=50, blank=True, null=True)
    site_id = models.CharField(max_length=50, blank=True, null=True)
    site_type = models.CharField(max_length=50, blank=True, null=True)
    globel_id = models.CharField(max_length=50, blank=True, null=True)
    system_version_type = models.CharField(max_length=50, blank=True, null=True)
    i_c_date = models.DateField(blank=True, null=True)
    sow_status = models.CharField(max_length=30, blank=True, null=True)
    no_of_battery_bank = models.CharField(max_length=10, blank=True, null=True)
    door_sensor = models.CharField(max_length=20, blank=True, null=True)
    antenna = models.CharField(max_length=20, blank=True, null=True)
    hooter = models.CharField(max_length=20, blank=True, null=True)
    other_mention_check = models.IntegerField(blank=True, null=True)
    other_mention = models.CharField(max_length=30, blank=True, null=True)
    tpmsbattrybank = models.IntegerField(blank=True, null=True)
    tpmsrru = models.IntegerField(blank=True, null=True)
    tpmsbts = models.IntegerField(blank=True, null=True)
    tpmscable = models.IntegerField(blank=True, null=True)
    tpmsdg = models.IntegerField(blank=True, null=True)
    battery_bank_one = models.CharField(max_length=30, blank=True, null=True)
    battery_bank_two = models.CharField(max_length=30, blank=True, null=True)
    battery_bank_three = models.CharField(max_length=30, blank=True, null=True)
    battery_bank_four = models.CharField(max_length=30, blank=True, null=True)
    shroti_team_name = models.CharField(max_length=30, blank=True, null=True)
    shroti_team_no = models.CharField(max_length=20, blank=True, null=True)
    hub = models.CharField(max_length=50, blank=True, null=True)
    po_no = models.CharField(max_length=30, blank=True, null=True)
    po_date = models.DateField(blank=True, null=True)
    po_line_no = models.CharField(max_length=30, blank=True, null=True)
    total_amt = models.CharField(max_length=10, blank=True, null=True)
    invoice_no = models.CharField(max_length=20, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    gps_device_installed = models.IntegerField()
    gps_imei_no = models.CharField(max_length=20)
    gps_mobile_no = models.CharField(max_length=20)
    energy_meter_installed = models.IntegerField()
    ch1 = models.CharField(max_length=30, blank=True, null=True)
    ch2 = models.CharField(max_length=30, blank=True, null=True)
    ch3 = models.CharField(max_length=30, blank=True, null=True)
    ch4 = models.CharField(max_length=30, blank=True, null=True)
    ch5 = models.CharField(max_length=30, blank=True, null=True)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    status = models.CharField(max_length=10)
    is_chargeable = models.CharField(max_length=1)
    biling_name = models.CharField(max_length=255, blank=True, null=True)
    biling_st_id = models.CharField(max_length=255, blank=True, null=True)
    ptye = models.IntegerField(blank=True, null=True)
    func_type = models.IntegerField()
    no_of_rru = models.CharField(max_length=10, blank=True, null=True)
    no_of_bts = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tpms_tracker_master'

# Model for the live status data from devices
class TiCurrentStatus(models.Model):
    imei = models.CharField(unique=True, max_length=50)
    iams = models.IntegerField()
    iams_change = models.IntegerField()
    tpms = models.IntegerField()
    tpms_change = models.IntegerField()
    volt = models.DecimalField(max_digits=10, decimal_places=2)
    temp = models.DecimalField(max_digits=10, decimal_places=0)
    vdc = models.DecimalField(max_digits=10, decimal_places=2)
    idc1 = models.DecimalField(max_digits=10, decimal_places=2)
    idc2 = models.DecimalField(max_digits=10, decimal_places=2)
    idc3 = models.DecimalField(max_digits=10, decimal_places=2)
    idc4 = models.DecimalField(max_digits=10, decimal_places=2)
    idc5 = models.DecimalField(max_digits=10, decimal_places=2)
    idc6 = models.DecimalField(max_digits=10, decimal_places=2)
    kwh1 = models.DecimalField(max_digits=10, decimal_places=2)
    kwh2 = models.DecimalField(max_digits=10, decimal_places=2)
    kwh3 = models.DecimalField(max_digits=10, decimal_places=2)
    kwh4 = models.DecimalField(max_digits=10, decimal_places=2)
    kwh5 = models.DecimalField(max_digits=10, decimal_places=2)
    kwh6 = models.DecimalField(max_digits=10, decimal_places=2)
    iccid = models.CharField(max_length=25, blank=True, null=True)
    imsi = models.CharField(max_length=25, blank=True, null=True)
    sig = models.IntegerField()
    update_at = models.DateTimeField()
    btlv = models.DecimalField(max_digits=10, decimal_places=0)
    hrt = models.DecimalField(max_digits=10, decimal_places=0)
    v_offset = models.DecimalField(max_digits=10, decimal_places=2)
    t_offset = models.DecimalField(max_digits=10, decimal_places=2)
    iams_mask = models.IntegerField()
    tpms_mask = models.IntegerField()
    hooter_mask = models.IntegerField()
    tpms_no_mask = models.IntegerField()
    dg_auto = models.IntegerField()
    created_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ti_current_status'

class AlEscalationMaster(models.Model):
    site_entry_id = models.AutoField(primary_key=True)
    site_id = models.CharField(max_length=50, db_collation='utf8_general_ci')
    site_number = models.CharField(max_length=20, db_collation='utf8_general_ci')
    imei = models.CharField(unique=True, max_length=20, db_collation='utf8_general_ci')
    l1_number = models.CharField(max_length=20, db_collation='utf8_general_ci', blank=True, null=True)
    l2_number = models.CharField(max_length=20, db_collation='utf8_general_ci', blank=True, null=True)
    l3_number = models.CharField(max_length=20, db_collation='utf8_general_ci', blank=True, null=True)
    l4_number = models.CharField(max_length=20, db_collation='utf8_general_ci', blank=True, null=True)
    l5_number = models.CharField(max_length=20, db_collation='utf8_general_ci', blank=True, null=True)
    btlv_level = models.FloatField(blank=True, null=True)
    temp_level = models.FloatField(blank=True, null=True)
    alarm_mask = models.PositiveIntegerField()
    update_dt = models.DateTimeField()
    client = models.CharField(max_length=30, db_collation='utf8_general_ci', blank=True, null=True)
    circle = models.CharField(max_length=30, db_collation='utf8_general_ci', blank=True, null=True)
    zone = models.CharField(max_length=30, db_collation='utf8_general_ci', blank=True, null=True)
    cluster = models.CharField(max_length=30, db_collation='utf8_general_ci', blank=True, null=True)
    site_id_ref = models.CharField(max_length=30, db_collation='utf8_general_ci', blank=True, null=True)
    global_id = models.CharField(max_length=30, db_collation='utf8_general_ci', blank=True, null=True)
    site_name = models.CharField(max_length=50, db_collation='utf8_general_ci', blank=True, null=True)
    ver = models.CharField(max_length=30, db_collation='utf8_general_ci', blank=True, null=True)
    volt_offset = models.FloatField()
    temp_offset = models.FloatField()
    inc_dt = models.DateField()
    create_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'al_escalation_master'

class RmsAlarmCommon(models.Model):
    imei = models.CharField(max_length=32, primary_key=True)  # Add primary_key=True
    site_id = models.CharField(max_length=64)
    site_name = models.CharField(max_length=128)
    cluster_id = models.CharField(max_length=64)
    dist_id = models.CharField(max_length=64)
    state_id = models.CharField(max_length=64)
    DOOR_ALARM = models.BooleanField()
    MAINS_FAIL = models.BooleanField()
    DG_ON = models.BooleanField()
    DG_Failed_to_start = models.BooleanField()
    DG_FUEL_LEVEL_LOW1 = models.BooleanField()
    SITE_ON_BATTERY = models.BooleanField()
    HIGH_TEMPERATURE = models.BooleanField()
    FIRE_and_SMOKE = models.BooleanField()
    LOW_BATTERY_VOLTAGE = models.BooleanField()
    EMERGENCY_FAULT = models.BooleanField()
    LLOP_FAULT = models.BooleanField()
    DG_OVERLOAD = models.BooleanField()
    DG_FUEL_LEVEL_LOW2 = models.BooleanField()
    ALTERNATOR_FAULT = models.BooleanField()
    DG_Failed_to_stop = models.BooleanField()
    reserve = models.CharField(max_length=128, blank=True, null=True)
    created_dt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rms_alarm_common_table'

