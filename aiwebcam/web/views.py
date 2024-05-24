from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request): # web 함수는 request 필수
	return HttpResponse("Web Main Page ")