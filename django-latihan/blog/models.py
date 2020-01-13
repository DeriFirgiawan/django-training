from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
	judul		= models.CharField(max_length=255)
	isi			= models.TextField()
	updated		= models.DateTimeField(auto_now=True)
	published	= models.DateTimeField(auto_now_add=True)
	slug 		= models.SlugField()

	def save(self):
		self.slug = slugify(self.judul)
		super().save()

	def __str__(self):
		return "{}. {}".format(self.id, self.judul)