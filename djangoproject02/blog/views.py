from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from .models import DataForm
from .forms import IsiForm
# Create your views here.

class IsiData(CreateView):
	form_class = IsiForm
	template_name = 'blog/index.html'

class SuccesView(TemplateView):
	template_name = 'blog/succes.html'