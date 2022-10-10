from django.shortcuts import render
from .models import LanguagesModel


# Create your views here.
def index(request):
    languages = LanguagesModel.objects.all().order_by('id_no').values('id_no', 'language_name')
    context = {'languages': languages}

    return render(request, 'languages/base.html', context)