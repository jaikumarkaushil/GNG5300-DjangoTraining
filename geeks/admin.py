from django.contrib import admin

# Register your models here.
from .models import GeeksModel
from .models import Album
from .models import Song


class geekModel(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(GeeksModel, geekModel)

class modelId(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Album)
admin.site.register(Song)


