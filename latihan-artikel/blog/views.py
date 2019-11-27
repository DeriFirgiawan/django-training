from django.shortcuts import render
#mengimpor dari class based view
from django.views.generic.base import TemplateView
#menginpor dari class based view
from django.views.generic import ListView,DetailView,FormView
#mengimport data dari models.py
from .models import Artikel
# mengimpor data dari forms.py
from .forms import ArtikelForm

from django.urls import reverse_lazy
# Create your views here.

class ArtikelFormView(FormView):
	form_class = ArtikelForm
	template_name = 'blog/create.html'
	success_url = reverse_lazy('home:list',kwargs={'penulis':'all'})
	extra_context = {
		'page_title':'Create Postingan',
	}

	def get_context_data(self,*args,**kwargs):
		self.kwargs.update(self.extra_context)
		kwargs = self.kwargs
		return super().get_context_data(*args,**kwargs)

	def form_valid(self,form):
		form.save()
		return super().form_valid(form)


class ArtikelDetailView(DetailView):
	model = Artikel
	extra_context = {
		'page_title':'List Content',
	}

	def get_context_data(self,*args,**kwargs):
		self.kwargs.update(self.extra_context)
		artikel_lain = self.model.objects.exclude(slug=self.kwargs['slug'])
		self.kwargs.update({'artikel_lain':artikel_lain})
		kwargs = self.kwargs

		return super().get_context_data(*args,**kwargs)



class ArtikelListView(ListView):
	model = Artikel
	oredering = ['update']
	#paginate_by = 2
	extra_context = {
		'page_title':'List Postingan',
	}
	def get_queryset(self):
		if self.kwargs['penulis'] != 'all':
			self.queryset = self.model.objects.filter(penulis__iexact= self.kwargs['penulis'])
			self.kwargs.update({
				'penulis':self.kwargs['penulis'],
				})
		return super().get_queryset()


	def get_context_data(self,*args,**kwargs):
		self.kwargs.update(self.extra_context)
		kwargs = self.kwargs
		return super().get_context_data(*args,**kwargs)




class HomeView(TemplateView):
	template_name = 'blog/index.html'
	context = {}

	def get_context_data(self):
		context = {
			'page_title':'Selamat Datang',
			'heading':'Mari Kita Membaca',
		}

		return context