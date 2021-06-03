from django.db import models

class Artist(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	bio = models.TextField(null=True, blank=True, help_text='Give some info about the artist')
	song_total = models.IntegerField()
	choices = models.TextField(choices=[('1', 'Choice 1'), ('2', 'Choice 2')])
	favorite = models.BooleanField(default=False)
	last_modified = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	profile_picture = models.ImageField(upload_to='uploads')
	download = models.FileField(upload_to='uploads')
