# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from app.models import PERSON, FACE
# 第三種方式，加入 ModelAdmin 類別，定義顯示欄位、欄位過濾資料、搜尋和排序
class PERSONAdmin(admin.ModelAdmin):   
    list_display=('id','time'','in_out')
    list_filter=('cName','cSex')
    search_fields=('cName',)
    ordering=('id',)

class FACEAdmin(admin.ModelAdmin):   
    list_display=('id','cName','cSex','cBirthday','cEmail','cPhone','cAddr')
    list_filter=('cName','cSex')
    search_fields=('cName',)
    ordering=('id',)
 
admin.site.register(student,studentAdmin)