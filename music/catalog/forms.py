from django import forms
from .models import Artist

class BasicForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100)
	email = forms.EmailField()
	password = forms.CharField(label='password', widget=forms.PasswordInput)
	checkbox = forms.BooleanField(required=False)
	comment = forms.CharField(label='Comment', widget=forms.Textarea)

class ArtistForm(forms.ModelForm):
	class Meta:
		model = Artist
		fields = '__all__'