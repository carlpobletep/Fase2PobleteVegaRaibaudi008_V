from django.urls import path
from . import views
urlpatterns = [
	path('',views.CervezaListView.as_view(),name='catalogo'),
	path('cerveza/<int:pk>',views.CervezaListView.as_view(),name='cerveza-list'),
]


