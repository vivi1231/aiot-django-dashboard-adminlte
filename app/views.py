# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from app.models import PERSON, FACE, ericapp_peoplemove, ericapp_agender


from django.views.generic import TemplateView

from .models import Time_opt
from .filters import Time_optFilter


@login_required(login_url="/login/")
def index(request):
    # results = PERSON.objects.all()
    queryset_P = ericapp_peoplemove.objects.all()
    queryset_F = ericapp_agender.objects.all()
    # people_in = sum([p.in_out for p in queryset_P])
    # people_in_and_out = len([p.in_out for p in queryset_P])
    # pre_people = people_in - (people_in_and_out - people_in)
    # age = [p.age for p in queryset_F]
    # gender = [p.gender for p in queryset_F]

    # Count number of male and age
    # age_M_0 = len(FACE.objects.filter(age='0', gender=True))
    # age_M_10 = len(FACE.objects.filter(age='1', gender=True))
    # age_M_20 = len(FACE.objects.filter(age='2', gender=True))
    # age_M_30 = len(FACE.objects.filter(age='3', gender=True))
    # age_M_40 = len(FACE.objects.filter(age='4', gender=True))
    # age_M_50 = len(FACE.objects.filter(age='5', gender=True))
    # age_M_60 = len(FACE.objects.filter(age='6', gender=True))
    # age_M_70 = len(FACE.objects.filter(age='7', gender=True))

    # # Count number of female and age
    # age_F_0 = len(FACE.objects.filter(age='0', gender=False))
    # age_F_10 = len(FACE.objects.filter(age='1', gender=False))
    # age_F_20 = len(FACE.objects.filter(age='2', gender=False))
    # age_F_30 = len(FACE.objects.filter(age='3', gender=False))
    # age_F_40 = len(FACE.objects.filter(age='4', gender=False))
    # age_F_50 = len(FACE.objects.filter(age='5', gender=False))
    # age_F_60 = len(FACE.objects.filter(age='6', gender=False))
    # age_F_70 = len(FACE.objects.filter(age='7', gender=False))



    return render(request, "index.html")

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


def time(request):
    time_opts = Time_opt.objects.all()
 
    time_optFilter = Time_optFilter(queryset=time_opts)
 
    if request.method == "POST":
        time_optFilter = Time_optFilter(request.POST, queryset=time_opts)
 
    context = {
        'time_optFilter': time_optFilter
    }
 
    return render(request, 'time_opts/widgets.html', context)







































































# @login_required(login_url="/login/")
# def index(request):
#     # results = PERSON.objects.all()
#     queryset_P = PERSON.objects.all()
#     queryset_F = FACE.objects.all()
#     people_in = sum([p.in_out for p in queryset_P])
#     people_in_and_out = len([p.in_out for p in queryset_P])
#     pre_people = people_in - (people_in_and_out - people_in)
#     age = [p.age for p in queryset_F]
#     gender = [p.gender for p in queryset_F]

#     # Count number of male and age
#     age_M_0 = len(FACE.objects.filter(age='0', gender=True))
#     age_M_10 = len(FACE.objects.filter(age='1', gender=True))
#     age_M_20 = len(FACE.objects.filter(age='2', gender=True))
#     age_M_30 = len(FACE.objects.filter(age='3', gender=True))
#     age_M_40 = len(FACE.objects.filter(age='4', gender=True))
#     age_M_50 = len(FACE.objects.filter(age='5', gender=True))
#     age_M_60 = len(FACE.objects.filter(age='6', gender=True))
#     age_M_70 = len(FACE.objects.filter(age='7', gender=True))

#     # Count number of female and age
#     age_F_0 = len(FACE.objects.filter(age='0', gender=False))
#     age_F_10 = len(FACE.objects.filter(age='1', gender=False))
#     age_F_20 = len(FACE.objects.filter(age='2', gender=False))
#     age_F_30 = len(FACE.objects.filter(age='3', gender=False))
#     age_F_40 = len(FACE.objects.filter(age='4', gender=False))
#     age_F_50 = len(FACE.objects.filter(age='5', gender=False))
#     age_F_60 = len(FACE.objects.filter(age='6', gender=False))
#     age_F_70 = len(FACE.objects.filter(age='7', gender=False))



#     return render(request, "index.html",{'count_in':people_in, 'pre_count':pre_people, 'age':age, 'gender':gender, 
#     'age_M_0':age_M_0, 'age_M_10':age_M_10, 'age_M_20':age_M_20, 'age_M_30':age_M_30, 'age_M_40':age_M_40, 'age_M_50':age_M_50, 'age_M_60':age_M_60, 'age_M_70':age_M_70, 
#     'age_F_0':age_F_0, 'age_F_10':age_F_10, 'age_F_20':age_F_20, 'age_F_30':age_F_30, 'age_F_40':age_F_40, 'age_F_50':age_F_50, 'age_F_60':age_F_60, 'age_F_70':age_F_70,})