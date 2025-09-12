from django.shortcuts import render,HttpResponse, redirect
from.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import custom_login_required
from django.core.paginator import Paginator
from django.db.models import Max


from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RmsAlarmCommonSerializer

class RmsAlarmCommonList(APIView):
    def get(self, request, format=None):
        latest = RmsAlarmCommon.objects.using('third_db').aggregate(
            latest_date=Max('created_dt')
        )['latest_date']

        alarms = RmsAlarmCommon.objects.using('third_db').filter(
            created_dt__date=latest.date()
        )

        serializer = RmsAlarmCommonSerializer(alarms, many=True)
        return Response(serializer.data)



# Create your views here.
# @custom_login_required
# def index(request):
#     commondata = CommonEnergyData.objects.using('second_db').all
#     print(commondata)
#     return render(request, 'index.html')
   # return HttpResponse("this is homepage")
@custom_login_required
def index(request):
    return render(request, 'index.html')
   
@custom_login_required
def analytics(request):
    return render(request, 'analytics.html')

@custom_login_required
def battery(request):
    return render(request, "battery.html")
    
@custom_login_required
def useradmin(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        LoginTableForRms.objects.create(
            name=name,
            user_name=username,
            password=password,   
            role=role
        )
        messages.success(request, f"User {name} added successfully!")
        return redirect("useradmin")

    return render(request, 'useradmin.html')

@custom_login_required
def energy(request):
    return render(request, "energy.html")

@custom_login_required
def grid_billing(request):
    return render(request, "grid_billing.html")

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import LoginTableForRms

@csrf_exempt
def login(request):
    print('login:-----')
    if request.method == "POST":
        username = request.POST.get("username")
        print('user name:-', username)
        password = request.POST.get("password")
        print('password:-', password)

        try:
            # Get the user object based on username and password
            user = LoginTableForRms.objects.get(user_name=username, password=password)
            
            # Print only the role of the user
            print('role:', user.role)

            # Save in session
            request.session["user_id"] = user.id
            request.session["role"] = user.role

            return JsonResponse({
                "status": "success",
                "message": f"Welcome {user.name}!",
                "role": user.role
            })
        except LoginTableForRms.DoesNotExist:
            return JsonResponse({
                "status": "error",
                "message": "Invalid username or password."
            }, status=401)

    return render(request, 'login.html')


@custom_login_required   
def filters(request):
    state_data = TpmsStateMaster.objects.using('third_db').all.order_by('state_name')
    print(state_data)
    return render(request, 'filters.html', {'state_data': state_data})

@custom_login_required
def live_alarms(request):
    # Find the latest date
    latest = RmsAlarmCommon.objects.using('third_db').aggregate(
        latest_date=Max('created_dt')
    )['latest_date']

    # Filter alarms only from that date
    alarms = RmsAlarmCommon.objects.using('third_db').filter(
        created_dt__date=latest.date()
    )

    state_data = TpmsStateMaster.objects.using('third_db').all().order_by('state_name')

    context = {
        'alarms': alarms,
        'state_data': state_data,
        'hide_site_name': True,
        'hide_global_no': True,
        'hide_imei_no': True,
        'hide_enter_days': True,
        'hide_date': True,
    }
    return render(request, 'live_alarms.html', context)


@custom_login_required
def maps(request):
    return render(request, "maps.html")

@custom_login_required
def reports(request):
    return render(request, "reports.html")

def status(request):
    # Filter values ko form se lein
    site_name = request.GET.get('site_name', '')
    global_no = request.GET.get('global_no', '')
    imei = request.GET.get('imei', '')
    zone = request.GET.get('zone', '')
    cluster = request.GET.get('cluster', '')

    # AlEscalationMaster table se saara data lein
    sites_master_list = AlEscalationMaster.objects.using('second_db').all().order_by('site_name') # Order by name

    # Filters apply karein
    if site_name: sites_master_list = sites_master_list.filter(site_name__icontains=site_name)
    if global_no: sites_master_list = sites_master_list.filter(global_id__icontains=global_no)
    if imei: sites_master_list = sites_master_list.filter(imei__icontains=imei)
    if zone: sites_master_list = sites_master_list.filter(zone=zone)
    if cluster: sites_master_list = sites_master_list.filter(cluster=cluster)

    # === PAGINATION LOGIC START ===
    # 1. Paginator object banayein: 10 items per page
    paginator = Paginator(sites_master_list, 10) 
    # 2. URL se page number lein (e.g., ?page=2)
    page_number = request.GET.get('page')
    # 3. Uss page ka data 'page_obj' mein store karein
    page_obj = paginator.get_page(page_number)
    # === PAGINATION LOGIC END ===

    # Filtered page ke IMEIs ki list lein
    imei_list = [site.imei for site in page_obj]

    # Live status data fetch karein
    status_data = TiCurrentStatus.objects.using('second_db').filter(imei__in=imei_list)
    status_map = {status.imei: status for status in status_data}
    
    # Data ko combine karein
    for site in page_obj:
        site.status_data = status_map.get(site.imei)
        
    # Dropdowns ke liye unique zones aur clusters lein
    distinct_zones = AlEscalationMaster.objects.using('second_db').values('zone').distinct()
    distinct_clusters = AlEscalationMaster.objects.using('second_db').values('cluster').distinct()

    context = {
        # IMPORTANT: 'results' ki jagah ab 'page_obj' bhejenge
        'page_obj': page_obj, 
        'zones': distinct_zones,
        'clusters': distinct_clusters,
        'site_name': site_name, 'global_no': global_no, 'imei': imei,
        'current_zone': zone, 'current_cluster': cluster,
        'hide_alarm_type':True,
        'hide_imei_no':True,
        'hide_enter_days':True,
        'hide_date': True,
    }
    
    return render(request, "status.html", context)

@custom_login_required
def rovo_call(request):
    return render (request, "rovo_call.html")
    
    
@csrf_exempt
def get_districts_for_filter(request, state_id):
   

    if state_id and state_id != "All":
        districts = TpmsDistrictMaster.objects.using('third_db').filter(state_id=state_id)
        district_options = [{'id': district.dist_id, 'name': district.district_name} for district in districts]
         
    else:
        district_options = []

    return JsonResponse({'districts': district_options})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def get_clusters_for_filter(request, dist_id):
    
    try:
        if dist_id and dist_id != "All":
            clusters = TpmsClusterMaster.objects.using('third_db').filter(dist_id=dist_id)
            # Use cluster_id, not dist_id for the ID field
            cluster_options = [{'id': cluster.cluster_id, 'name': cluster.cluster_name} for cluster in clusters]
            
        else:
            cluster_options = []
        return JsonResponse({'clusters': cluster_options}, safe=False)
    except Exception as e:
        print("Error in get_clusters_report_total:", str(e))
        return JsonResponse({'error': str(e)}, status=500)
    


