"""beautyganweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

urlpatterns = [
    # v1 API
    path('v1/', views.api_index, name = 'api_index'),
	# v2 API
    # path('v2/', views.api_index1, name = 'api_index1'),
	# v1 API
    path('v1/getmodellist', views.api_getmodellist, name = 'api_getmodellist'),
    path('v1/sendimage/', views.api_sendimage, name = 'api_sendimage'),
]