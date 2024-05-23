from django.shortcuts import render
from django.http import HttpResponse
from .models import Test1

# Create your views here.

def index(request):
	# return HttpResponse("web 인덱스 파일입니다.")
	db_list = Test1.objects.all()
	db_list1 = "데이터1"
	db_list2 = "데이터2"
	return render(request, 'web_index.html', {'data':db_list, 'data1':db_list1, 'data2':db_list2})

