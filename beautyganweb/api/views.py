from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def api_index(request):
	return HttpResponse("ChicBytes API v1.0")

def api_index1(request):
	return HttpResponse("ChicBytes API v2.0")

def api_getmodellist(request):
	sendData = {
		"name" : "Jang",
		"image" : "https://pbs.twimg.com/media/E2-Z_pTXEAEhfBP?format=jpg&name=900x900",
		"item" : "립스틱",
		"shop" : "https://shop.dior.co.kr/products/y0356009?gad_source=1&gclid=EAIaIQobChMI2IO0_Nu2hgMVJcRMAh1ZfQ1CEAAYASAAEgKzhfD_BwE",
		"doc" : "꾸뛰르 컬러 립스틱 - 벨벳 및 사틴 피니쉬 - 하이드레이팅 플로럴 립케어 - 롱웨어",
		"dates" : "2024-05-31"
	}
	return JsonResponse(sendData, safe = False, json_dumps_params = {'ensure_ascii':False}, status = 200)
	
