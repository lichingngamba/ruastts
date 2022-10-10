from django.db import models

# Create your models here.

class voices(models.Model):
    id_no = models.IntegerField(primary_key=True)
    voice_name = models.TextField(max_length = 40)

    
    def __str__(self):
        return '<voices: {}, id_no: {}>'.format(self.voice_name, self.id_no)
    
    
# id_no = voices.id_no
# voice_name = voices.voice_name
