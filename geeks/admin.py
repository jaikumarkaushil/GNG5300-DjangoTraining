from django.contrib import admin

# Register your models here.
from .models import GeeksModel


class geekModel(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(GeeksModel, geekModel)
