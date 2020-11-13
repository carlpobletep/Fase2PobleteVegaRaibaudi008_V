from django.shortcuts import render
from .models import Cerveza
from django.views import generic

# Create your views here.

class CervezaListView(generic.ListView):
	model = Cerveza
	template_name='catalogo.html'
	context_object_name='Cerveza_list'
