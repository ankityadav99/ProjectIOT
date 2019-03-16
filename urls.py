"""project_informatica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
#from django.conf.urls import url
from rest_framework import routers
from MARC import views


router1 = routers.DefaultRouter()
router1.register('', views.ProductInfoView)

router2 = routers.DefaultRouter()
router2.register('', views.ProductionProductInfoView)

router3 = routers.DefaultRouter()
router3.register('', views.ProductFeedbackView)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('productinfo/', include(router1.urls)),
    path('productionproductinfo/', include(router2.urls)),
    path('productfeedback/', include(router3.urls))
]
