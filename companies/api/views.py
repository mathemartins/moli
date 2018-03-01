from rest_framework.generics import (
	CreateAPIView,
	ListAPIView, 
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	UpdateAPIView,
	DestroyAPIView,
)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
)

from companies.models import StartUp, Investor
from companies.api.permissions import IsOwnerOrReadOnly
from companies.api.serializers import (
	StartUpCreateUpdateSerializer,
	StartUpDetailSerializer,
	StartUpListSerializer, 
	InvestorSerializer,
)


class StartUpCreateAPIView(CreateAPIView):
	queryset = StartUp.objects.all()
	serializer_class = StartUpCreateUpdateSerializer

	permission_classes = [IsAuthenticated]



class StartUpListAPIView(ListAPIView):
	queryset = StartUp.objects.all()
	serializer_class = StartUpListSerializer



class StartUpDetailAPIView(RetrieveAPIView):
	queryset = StartUp.objects.all()
	serializer_class = StartUpDetailSerializer
	lookup_field = 'slug'



class StartUpUpdateAPIView(RetrieveUpdateAPIView):
	queryset = StartUp.objects.all()
	serializer_class = StartUpCreateUpdateSerializer
	lookup_field = 'slug'

	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



class StartUpDeleteAPIView(DestroyAPIView):
	queryset = StartUp.objects.all()
	serializer_class = StartUpDetailSerializer
	lookup_field = 'slug'




class InvestorListAPIView(ListAPIView):
	queryset = Investor.objects.all()
	serializer_class = InvestorSerializer