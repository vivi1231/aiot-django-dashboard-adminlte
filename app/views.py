# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from app.models import PERSON, FACE

from django.views.generic import TemplateView


@login_required(login_url="/login/")
def index(request):
    # results = PERSON.objects.all()
    queryset = PERSON.objects.all()
    people_in = sum([p.in_out for p in queryset])
    people_in_and_out = len([p.in_out for p in queryset])
    pre_people = people_in - (people_in_and_out - people_in)

    return render(request, "index.html",{'count_in':people_in, 'pre_count':pre_people})

# class ChartView(TemplateView):
#     template_name = "index.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['qs'] = PERSON.objects.all()
#         return context


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))



def listone(request): 
    try: 
        unit = PERSON.objects.get(id="1") #讀取一筆資料
    except:
        errormessage = " (讀取錯誤!)"
    return render(request, "listone.html", locals())


def listall(request):  
    PERSONS = PERSON.objects.all().order_by('id')  
    #讀取資料表, 依 id 遞增排序(欄位前加入負號-id代表遞減排序)
    return render(request, "listall.html", locals())


def insert(request):  #新增資料
    time = datetime.now()
    in_out = True
    unit = PERSON.objects.create(time=time, in_out=in_out) 
    unit.save()  #寫入資料庫
    PERSONS = PERSON.objects.all().order_by('-id')  #讀取資料表, 依 id 遞減排序
    return render(request, "listall.html", locals())


def modify(request):  #修改資料
    unit = PERSON.objects.get(id='1')
    unit.time =  datetime.now()
    unit.in_out = False
    unit.save()  #寫入資料庫
    students = PERSON.objects.all().order_by('-id')
    return render(request, "listall.html", locals())


def delete(request,id=None):  #刪除資料
    unit = PERSON.objects.get(id='1')
    unit.delete()
    PERSONS = PERSON.objects.all().order_by('-id')
    return render(request, "listall.html", locals())

# @login_required(login_url="/login/")
def showdata(request):
    results = PERSON.objects.all()
    return render(request, 'showdata.html',{'data':results})
