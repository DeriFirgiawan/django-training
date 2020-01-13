from django.conf.urls import url, include
from django.contrib import admin
from .views import HomeView

urlpatterns = [
	url(r'^blog/', include('blog.urls',namespace='blog')),
    url(r'^$', HomeView.as_view(),name='home'),
    url(r'^admin/', admin.site.urls),
]
