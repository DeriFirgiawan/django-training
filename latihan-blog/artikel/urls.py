from django.conf.urls import url
from .views import (
	ArtikelHome,
	ArtikelListView,
	ArtikelDetailView,
	ArtikelKategoriListView,
	ArtikePerKategoriListView,
	ArtikelManage,
	ArtikelForm,
	ArtikelDeleteView,
	ArtikelUpdateView,
	)

urlpatterns = [
	url(r'^manage/update/(?P<pk>\d+)$', ArtikelUpdateView.as_view(),name='update'),
	url(r'^manage/delete/(?P<pk>\d+)$', ArtikelDeleteView.as_view(),name='delete'),
	url(r'^manage/$', ArtikelManage.as_view(),name='manage'),
	url(r'^tambah/$', ArtikelForm.as_view(),name='create'),
	url(r'^perkategori/(?P<kategori>[\w-]+)$', ArtikePerKategoriListView.as_view(),name='listkategori'),
	url(r'^kategori/$',ArtikelKategoriListView.as_view(),name='category'),
	url(r'^detail/(?P<slug>[\w-]+)$', ArtikelDetailView.as_view(),name='detail'),
	url(r'^artikel/$', ArtikelListView.as_view(),name='list'),
	url(r'^$', ArtikelHome.as_view(),name='index'),
]