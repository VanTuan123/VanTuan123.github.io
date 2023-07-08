from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp.models import CRCInfo
from myapp.serializers import CRCInfoSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import io 

#from myapp.models import Feature_tuan

# Create your views here.
def index(request):
    #return HttpResponse('<h1> Welcome </h1>')
    #return render(request, 'index.html')
    #name = user.name
    #feature1 = Feature_tuan.objects.all()
    return render(request, 'index.html')