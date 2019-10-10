from django.shortcuts import render

# Create your views here.
def injuryOnDuty(request):
    return render(request,'injuryonduty.html')
    
def vehicleAccident(request):
    return render(request,'vehicleaccident.html')
    
def hazMatExposure(request):
    return render(request,'hazmatexpsoure.html')
    
def biologicalExposure(request):
    return render(request,'biologicalexposure.html')