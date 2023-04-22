from rest_framework import generics
from rest_framework import viewsets
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, UserSerializer, BookingSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated]
   
class BookingViewSet(viewsets.ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer
   permission_classes = [IsAuthenticated]