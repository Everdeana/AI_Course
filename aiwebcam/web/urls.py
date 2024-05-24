from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index') # 비어있으면 실행(ex -> path('/list', ~) -> 리스트 페이지
	# 아무 것도 없으면 뒷부분 실행
]