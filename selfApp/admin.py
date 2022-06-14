from django.contrib import admin
from .models import *

# Register your models here.
class ActorAdmin(admin.ModelAdmin):  
    prepopulated_fields= {'url':('title',)}
    list_editable = ('is_published',)
    list_display = ('title', 'id', 'is_published')
    

admin.site.register(Actor, ActorAdmin)

class CategoryAdmin(admin.ModelAdmin):  
    prepopulated_fields= {'url':('name',)}
    list_display = ('name', 'id')

admin.site.register(Category, CategoryAdmin )
