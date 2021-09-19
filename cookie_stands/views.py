from rest_framework import generics
from .serializers import CookieStandSerializer
from .models import CookieStand
from .permissions import IsOwnerOrReadOnly
# Create your views here.

# class CookieStandList(generics.ListAPIView):
#   queryset = CookieStand.objects.all()
#   serializer_class = CookieStandSerializer

class CookieStandList(generics.ListCreateAPIView):
  #permission_classes = (IsOwnerOrReadOnly,)
  queryset = CookieStand.objects.all()
  serializer_class = CookieStandSerializer


# class CookieStandDetail(generics.RetrieveAPIView):
#   queryset = CookieStand.objects.all()
#   serializer_class = CookieStandSerializer

# class CookieStandDetail(generics.RetrieveUpdateAPIView):
#   queryset = CookieStand.objects.all()
#   serializer_class = CookieStandSerializer

class CookieStandDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = CookieStand.objects.all()
  serializer_class = CookieStandSerializer

