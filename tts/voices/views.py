from django.shortcuts import render
from .models import voices


# Create your views here.

# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, Guest. You're at the voices index.")


def index(request):
    voice = voices.objects.all().order_by('id_no').values('id_no', 'voice_name')    
    context = {'voice': voice}
    
    # context = {'id_no': qoo.id_no, 'voice_name': qoo.voice_name}
    
    return render(request, 'voices/index.html', context)