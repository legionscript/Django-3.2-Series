from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Artist

# def current_datetime(request):
# 	now = datetime.datetime.now()
# 	# html = "<html><body><p>It is now %s.</p></body></html>" % now
# 	# return HttpResponse(html)

# 	context = {
# 		'now': now
# 	}

# 	return render(request, 'catalog/index.html', context)

def index(request):
	artist = Artist.objects.get(pk=1)

	context = {
		'artist': artist
	}

	return render(request, 'catalog/index.html', context)

def sample_form(request):
	if request.method == 'POST':
		first_name = request.POST.get('firstName')
		print (first_name)
		return render(request, 'catalog/sample_form.html')
	else:
		print('get')
		return render(request, 'catalog/sample_form.html')

