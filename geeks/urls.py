from django.contrib import admin
from django.urls import path
#now import the views.py file into this code
from . import views
from django.conf import settings #add this
from django.conf.urls.static import static #add this

# CRUD - 300275126
urlpatterns=[
    path('admin/', admin.site.urls),
    path('', views.create_view),
    path('get/<id>', views.detail_view ),
    path('update/<id>', views.update_view),
    path('delete/<id>', views.delete_view)
]

if settings.DEBUG: #add this
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)