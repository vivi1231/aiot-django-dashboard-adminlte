# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.db import models
from .models import Time_opt
# Register your models here.
from app.models import PERSON, FACE
# 第三種方式，加入 ModelAdmin 類別，定義顯示欄位、欄位過濾資料、搜尋和排序
class PERSONAdmin(admin.ModelAdmin):
    model = PERSON   
    list_display=('id','time','in_out') # 使用list_display顯示多個欄位
    list_filter=('time', 'in_out') # 使用list_filter資料過濾
    search_fields=('time',) # 使用search_fields依照欄位搜尋
    ordering=('id',) # 使用ordering排序

class FACEAdmin(admin.ModelAdmin): 
    model = FACE  
    list_display=('id','time','gender','age')
    list_filter=('time','gender','age')
    search_fields=('time',)
    ordering=('id',)
 
admin.site.register(PERSON,PERSONAdmin)
admin.site.register(FACE,FACEAdmin)




class Time_optAdmin(admin.ModelAdmin):
    list_display = ('date', 'hour')
    
admin.site.register(Time_opt, Time_optAdmin)