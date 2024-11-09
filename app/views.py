from django.shortcuts import render

# Create your views here.
def filter(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'Parvez and hareesh are good friends','dt':dt,'c':1,'d':10}
    return render(request,'filter.html',d)
def newfilters(request):
    d={'data':'Well Come To My World and Im PArvez SyeD'}
    return render(request,'newfilters.html',d)