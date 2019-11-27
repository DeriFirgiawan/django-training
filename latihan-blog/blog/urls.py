from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
	url(r'^', include('artikel.urls', namespace='artikel')),
    url(r'^admin/', admin.site.urls),
]
