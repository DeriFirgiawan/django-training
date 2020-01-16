from django.conf.urls import url

from .views import IsiData,SuccesView

urlpatterns = [
	url(r'^succes/(?P<slug>[\w-]+)$', SuccesView.as_view(), name='berhasil'),
	url(r'^$', IsiData.as_view(), name='home'),
]