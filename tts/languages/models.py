from django.db import models


# Create your models here.
class LanguagesModel(models.Model):
    id_no = models.AutoField(primary_key=True)
    language_name = models.TextField(max_length=100)

    def __str__(self):
        return '<languages: {}, id_no: {}>'.format(self.language_name, self.id_no)
