from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	# return HttpResponse("web 인덱스 파일입니다.")
	db_list = "데이터베이스에서 자료를 가져왔습니다."
	return render(request, 'web_index.html', {'data':db_list})

