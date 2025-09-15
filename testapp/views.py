from django.shortcuts import render , redirect
from .models import CreateRecord
from django.views.decorators.cache import cache_page
# Create your views here.

@cache_page(60 * 2 , key_prefix='home_view')
def home(request):
    data = CreateRecord.objects.all()
    print(data)
    return render(request,template_name='index.html' , context={'data':data})

def create(request):
    data = CreateRecord.objects.count()
    new_record = CreateRecord(name = f"name{data+1}" , address = "None")
    new_record.save()
    print(data)
    return render(request , template_name='create.html')