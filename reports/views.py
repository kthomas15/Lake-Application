from django.shortcuts import render

from .models import County, Lake, Report

def homepage(request):
    counties = County.objects.order_by('name')
    return render(request, 'reports/index.html', {'counties': counties})

def countydetail(request, county_id):
    county = County.objects.get(id=county_id)
    lakes = Lake.objects.filter(county=county)
    return render(request, 'reports/countydetail.html', {'county': county, 'lakes':lakes})