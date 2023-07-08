from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp.models import CRCInfo
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import io 
from myapp.CRCInfoSerialize import CRCInfoSerialize
from crc import Calculator, Configuration

@csrf_exempt
def testrequest(request):
    if (request.method == 'POST'):
        json_data = request.body
        stream = io.BytesIO(json_data)
        mydata = JSONParser().parse(stream)
        myserializers = CRCInfoSerialize(data = mydata)
        if myserializers.is_valid():
           CRCResult = str(hex(CRC8H2F(myserializers.data['data'])))
           res = {'CRC_Result' : CRCResult}
           return HttpResponse(JSONRenderer().render(res), content_type = 'application/json')
        else:
           res = {"msg": "Failed"}
           return HttpResponse(JSONRenderer().render(res), content_type = 'application/json')
    else:
        if (request.method == 'GET'):
         CRCInfoxx = CRCInfo(data='GET request', title = 'this is GETs response')
         CRCInfoxx.save()
         serializer = CRCInfoSerialize(CRCInfoxx)
         content = JSONRenderer().render(serializer.data)
         return JsonResponse(serializer.data)
def CRC8H2F(data: str):
   data = data.replace('0x','')
   strlist = data.split()
   databyte = bytes([int(x, 16) for x in strlist])
   config = Configuration(
      width = 8,
      polynomial = 0x2F,
      init_value = 0xFF,
      final_xor_value=0xFF,
      reverse_input=False,
      reverse_output=False,
   )
   caculator = Calculator(config)
   CRCResult = caculator.checksum(databyte)
   return CRCResult
