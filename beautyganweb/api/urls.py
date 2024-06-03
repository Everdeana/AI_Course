from django.urls import path

from . import views

urlpatterns = [
    # V1 API
    path('v1/', views.api_index, name='api_index'),
    path('v1/getmodellist', views.api_getmodellist, name='api_getmodellist'),
    path('v1/sendimage/', views.api_sendimage, name='api_sendimage'),

    # V2 API
    path('v2/', views.api_index2, name='api_index2'),
]