from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializers import ProductSerializer
from .models import Product
from rest_framework import viewsets



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['GET'])
def index(req):
    return Response('hello')


# login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        token['testData'] = "baga"
        # ...
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# register
@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response("new user born")