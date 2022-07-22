from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Inclui as URLs do app ‘patrimonio’
    path('', include('patrimonio.urls', namespace='patrimonio')),
    path('admin/', admin.site.urls),
]
