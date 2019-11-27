from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
#load models.py & forms.py
from .models import Artikel
from .forms import ArtikelForm
# Create your views here.
class ArtikelUpdateView(UpdateView):
	form_class = ArtikelForm
	model = Artikel
	template_name = 'artikel/artikel_update.html'

class ArtikelDeleteView(DeleteView):
	model = Artikel
	template_name = 'artikel/artikel_delete.html'
	success_url = reverse_lazy('artikel:manage')

class ArtikelForm(CreateView):
	form_class = ArtikelForm
	template_name = 'artikel/create.html'

class ArtikelManage(ListView):
	model = Artikel
	template_name = 'artikel/artikel_manage.html'
	context_object_name = 'artikel_list'


class ArtikelPerKategori():
	model = Artikel

	def get_latest_artikel_each_kategori(self):
		kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
		queryset = []

		for kategori in kategori_list:
			artikel = self.model.objects.filter(kategori=kategori).latest('published')
			queryset.append(artikel)

		return queryset


class ArtikePerKategoriListView(ListView):
	model = Artikel
	template_name = 'artikel/artikel_per_kategori.html'
	context_object_name = 'artikel_kategori'
	ordering = ['-published']

	def get_queryset(self):
		self.queryset = self.model.objects.filter(kategori__iexact=self.kwargs['kategori'])
		return super().get_queryset()

class ArtikelKategoriListView(ListView):
	model = Artikel
	template_name = 'artikel/artikel_kategori_list.html'
	contex_object_name = 'artikel_list'

	def get_context_data(self,*args,**kwargs):
		kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
		self.kwargs.update({'kategori_list':kategori_list})
		kwargs = self.kwargs
		return super().get_context_data(*args,**kwargs)

class ArtikelDetailView(DetailView):
	model = Artikel
	template_name = 'artikel/artikel_detail.html'
	context_name = 'artikel'

class ArtikelListView(ListView):
	model = Artikel
	template_name = 'artikel/artikel_list.html'
	context_name = 'artikel_list'
	ordering = ['-published']


class ArtikelHome(TemplateView,ArtikelPerKategori):
	template_name = 'artikel/index.html'


	def get_latest_artikel_each_kategori(self):
		kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
		queryset = []

		for kategori in kategori_list:
			artikel = self.model.objects.filter(kategori=kategori).latest('published')
			queryset.append(artikel)

		return queryset

	def get_context_data(self):
		querysets = self.get_latest_artikel_each_kategori()
		context = {
			'latest_artikel_list':querysets,
			'page_title':'Home',
		}

		return context