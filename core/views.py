from django.shortcuts import render
from datetime import datetime
from core.models import HDPO

# Create your views here.
def Energy(request):
    WhatHourAreNow = datetime.now()
    ActualValues = HDPO.objects.all().order_by("-DjangoTimeStamp")
    TS = ActualValues[0].DjangoTimeStamp
    MW = ActualValues[0].PowerActive
    Mvar = ActualValues[0].PowerReactive
    Level = ActualValues[0].Level
    energy_dictionary = {
        'TS': TS,
        'MW': MW,
        'Mvar': Mvar,
        'Level': Level,
        'CurrentTime': WhatHourAreNow,
    }
    return render (request, 'energy-live.html', energy_dictionary)

def EnergyUpdate(request):
    myNewObject = HDPO()
    myNewObject.DjangoTimeStamp = datetime.now()
    myNewObject.PowerActive = datetime.now().minute + datetime.now().microsecond/1000000
    myNewObject.PowerReactive = datetime.now().second
    myNewObject.Level = datetime.now().hour + (datetime.now().second/10)
    myNewObject.Escape = datetime.now().microsecond/100000
        
    new_energy_dictionary = {
        'TS': myNewObject.DjangoTimeStamp,
        'MW': myNewObject.PowerActive,
        'Mvar': myNewObject.PowerReactive,
        'Level': myNewObject.Level,
    }
    
    myNewObject.save()
    return render (request, 'energy-update.html', new_energy_dictionary)
    
def DailyEnergy(request):
    dataFromDailyEnergy = HDPO.objects.values_list("DjangoTimeStamp", "PowerActive", "PowerReactive", "Level").order_by("-DjangoTimeStamp")[:10]
    BiggerThan = HDPO.objects.filter(Level__gt=10)
    #work with dates!
    dictionaryDailyEnergy = {
        'dataFromDailyEnergy': dataFromDailyEnergy
    }

    return render(request, "energy-daily.html", dictionaryDailyEnergy)