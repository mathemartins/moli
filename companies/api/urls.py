from django.urls import path
from django.contrib import admin

from companies.api.views import (
	StartUpCreateAPIView,
	StartUpDetailAPIView,
	StartUpListAPIView,
	StartUpUpdateAPIView,
	StartUpDeleteAPIView,
	InvestorListAPIView,
)

app_name = 'companies'

urlpatterns = [

	# startup - urls
	path('', StartUpListAPIView.as_view(), name='startup-list'),
	path('create', StartUpCreateAPIView.as_view(), name='startup-create'),
	path('<slug:slug>', StartUpDetailAPIView.as_view(), name='startup-detail'),
	path('<slug:slug>/update', StartUpUpdateAPIView.as_view(), name='startup-update'),
	path('<slug:slug>/delete', StartUpDeleteAPIView.as_view(), name='startup-delete'),

	# investor urls
	path('investors', InvestorListAPIView.as_view(), name='investor-list'),
]