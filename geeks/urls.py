from django.contrib import admin
from django.urls import path
#now import the views.py file into this code
from . import views
from django.conf import settings #add this
from django.conf.urls.static import static #add this

urlpatterns=[
    path('admin/', admin.site.urls),
    # path('', views.home_view)
    path('', views.modelformset_view)
]

if settings.DEBUG: #add this
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)