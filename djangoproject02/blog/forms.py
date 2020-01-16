from django.forms import ModelForm
from .models import DataForm

class IsiForm(ModelForm):
    class Meta:
    	model = DataForm
    	fields = [
    		'nama_lengkap',
    		'tempat_tanggal_lahir',
    		'jenis_kelamin',
    		'alamat',
    		'kelurahan',
    		'no_hp',
    		'instagram',
    		'asal_sekolah',
    		'kelas',
    		'nama_orang_tua',
    		'no_hp_orang_tua',
    		'perguruan_tinggi',
    	]