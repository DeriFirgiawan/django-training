from django.conf.urls import url
from .views import HomeView,ArtikelListView,ArtikelDetailView,ArtikelFormView
#mengimpor dari Class Based View
from django.views.generic import ListView,DetailView,FormView
#mengimpor dari models.py
from .models import Artikel
#mengimpor data dari forms.py
from .forms import ArtikelForm

urlpatterns = [
	url(r'^create/$', ArtikelFormView.as_view(),name='create'),
	#url(r'^create/$', FormView.as_view(form_class = ArtikelForm,template_name='blog/create.html'),name='create'),
	url(r'^detail/(?P<slug>[\w-]+)$', ArtikelDetailView.as_view(model=Artikel),name='detail'),
	#url(r'^detail(?P<slug>[\w+]-)$', ArtikelDetailView.as_view(),name='detail'),
	url(r'^postingan/(?P<penulis>\w+)/(?P<page>\d+)$', ArtikelListView.as_view(),name='list'),
	url(r'^postingan/(?P<penulis>\w+)$', ArtikelListView.as_view(),name='list'),
	url(r'^$', HomeView.as_view(),name='index'),
	#url(r'^postingan/$', ListView.as_view(model=Artikel),name='list'),
]