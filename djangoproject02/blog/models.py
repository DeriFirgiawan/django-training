from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class DataForm(models.Model):
	nama_lengkap			= models.CharField(max_length=255)
	tempat_tanggal_lahir	= models.CharField(max_length=255)
	gender			= (
		('L','Laki-Laki'),
		('P','Perempuan'),
		)
	jenis_kelamin 			= models.CharField(choices=gender,max_length=50)
	alamat					= models.TextField()
	kelurahan				= models.CharField(max_length=255)
	no_hp 					= models.CharField(max_length=50)
	instagram				= models.CharField(max_length=255)
	asal_sekolah			= models.CharField(max_length=50)
	kelas					= models.CharField(max_length=10)
	nama_orang_tua			= models.CharField(max_length=50)
	no_hp_orang_tua			= models.CharField(max_length=50)
	perguruan_tinggi		= models.TextField()
	published				= models.DateTimeField(auto_now_add=True)
	updated					= models.DateTimeField(auto_now=True)
	slug					= models.SlugField(blank=True,editable=False)

	def save(self):
		self.slug = slugify(self.nama_lengkap)
		super().save()

	def get_absolute_url(self):
		url_slug = {'slug':self.slug}
		return reverse('index:berhasil', kwargs= url_slug)

	def __str__(self):
		return "{}. {}".format(self.id,self.nama_lengkap)