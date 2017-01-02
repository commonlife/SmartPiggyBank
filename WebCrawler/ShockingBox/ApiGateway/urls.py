"""ShockingBox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import ShockingDealView
from .views import MoneyView
from .views import MoneySaveView

app_name = 'ApiGateway'

urlpatterns = [
    url(r'^money/save', MoneySaveView.as_view(), name='save_money'),
    url(r'^money/', MoneyView.as_view(), name='money'),
    url(r'^shocking_deal/', ShockingDealView.as_view(), name='shocking_deal'),
]
