from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('polls/', include(('polls.urls','polls'),namespace='polls')),
    path('admin/', admin.site.urls),
]

