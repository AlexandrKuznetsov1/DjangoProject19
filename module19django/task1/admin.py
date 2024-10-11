from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    # расшериваем поля для редактирования в панель администрирования
    list_display = ('name', 'balance', 'age',)
    # добавляем строку поиска по имени
    search_fields = ('name',)
    # фильтр сортировки по балансу
    list_filter = ('balance',)
    # настройка внутри панели
    fields = [('name', 'balance', 'age',),]
    # секции
    # fieldsets = (
    #     ('Buyer',{'fields':
    #                   ('name', 'balance', 'age',)}))


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # расшериваем поля для редактирования в панель администрирования
    list_display = ('title', 'description', 'cost', 'size', 'age_limited',)
    # добавляем строку поиска по названию
    search_fields = ('title',)
    # фильтр сортировки по цене
    list_filter = ('cost',)
    # настройка внутри панели
    fields = [('title', 'description', 'cost', 'size', 'age_limited',),]
    # секции
    # fieldsets = ((
    #     ('Game',{'fields':
    #         ('title', 'description', 'cost', 'size',)})),
    #              ('GameLimited', {'fields':('title', 'description', 'age_limited',)}))
