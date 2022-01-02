from django.shortcuts import render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import datetime
from .models import Artist
from .forms import BasicForm, ArtistForm

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

class ExampleForm(View):
    def get(self, request):
        name = request.GET.get('your_name')
        print('GET')
        print(name)
        return render(request, 'catalog/example_form.html')
    def post(self, request):
        name = request.POST.get('your_name')
        print('POST')
        print(name)
        return render(request, 'catalog/example_form.html')

class FormsBasics(View):
	def get(self, request):
		form = BasicForm()
		post_form = BasicForm()
		context = {
			'form': form,
			'post_form': post_form
		}

		return render(request, 'catalog/forms_basics.html', context)
	def post(self, request):
		post_form = BasicForm(request.POST)
		form = BasicForm()

		if post_form.is_valid():
			name = post_form.cleaned_data['your_name']
			email = post_form.cleaned_data['email']
			print(name)
			print(email)

		context = {
			'post_form': post_form,
			'form': form
		}
		return render(request, 'catalog/forms_basics.html', context)

class ArtistManualCreate(View):
	def get(self, request):
		form = ArtistForm()

		context = {
			'form': form
		}

		return render(request, 'catalog/artist_create_manually.html', context)
	
	def post(self, request):
		form = ArtistForm(request.POST, request.FILES)

		context = {
			'form': form
		}

		if form.is_valid():
			form.save()

		return render(request, 'catalog/artist_create_manually.html', context)