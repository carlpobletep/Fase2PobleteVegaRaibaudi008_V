from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Cerveza(models.Model):
	"""Model representing an author."""
	Nombre = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='images')
	precio=models.IntegerField(null=True)

	class Meta:
		ordering = ['Nombre']

	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.Nombre}'	
		
