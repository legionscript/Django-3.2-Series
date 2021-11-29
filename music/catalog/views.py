from django.shortcuts import render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import datetime
from .models import Artist

class Index(View):
	def get(self, request, *args, **kwargs):
		artist = Artist.objects.get(pk=1)

		context = {
			'artist': artist
		}

		return render(request, 'catalog/index.html', context)

class SampleForm(View):
	def get(self, request, *args, **kwargs):
		print('get')
		return render(request, 'catalog/sample_form.html')

	def post(self, request, *args, **kwargs):
		first_name = request.POST.get('firstName')
		print (first_name)
		return render(request, 'catalog/sample_form.html')

class ListArtists(ListView):
	model = Artist
	template_name = 'catalog/artists.html'
	context_object_name = 'artists'

class DetailArtist(DetailView):
	model = Artist
	context_object_name = 'artist'

class CreateArtist(CreateView):
	model = Artist
	fields = '__all__'

	def get_success_url(self):
		return reverse('index')

class UpdateArtist(UpdateView):
	model = Artist
	fields = '__all__'

	def get_success_url(self):
		return reverse('artist-detail', kwargs={'pk': self.object.pk})

class DeleteArtist(DeleteView):
	model = Artist
	success_url = reverse_lazy('index')