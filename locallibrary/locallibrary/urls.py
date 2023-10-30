from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
    path('catalog/', include('catalog.urls')),
]
