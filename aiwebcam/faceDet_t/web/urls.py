from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adduser/', views.adduser, name='adduser'),
    path('video_feed', views.video_feed, name='video_feed'),

    # 테스트 경로
    # path('face_test/', views.face_test, name='face_test'),

]