from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# 직접 생성한 Model 사용 -> Table 사용
from .models import RefModels

# Create your views here.
def api_index(request):
	return HttpResponse("ChicBytes API v1.0")

def api_index1(request):
	return HttpResponse("ChicBytes API v2.0")

def api_getmodellist(request):
	# DB
	# select * from api_refmodels
	datas = RefModels.objects.all()

	sendData = []

	for data in datas:
		# print(data)

		sendData.append({
			"name" : data.names,
			"image" : data.image,
			"item" : data.item,
			"shop" : data.shop,
			"doc" : data.doc,
			"dates" : data.dates
		})
	return JsonResponse(sendData, safe = False, json_dumps_params = {'ensure_ascii':False}, status = 200)
	
