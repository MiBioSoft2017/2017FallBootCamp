from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('MyApp.urls')),
    url(r'^admin/', admin.site.urls),
]
