from django.shortcuts import render
from rest_framework.generics import CreateAPIView, GenericAPIView,ListAPIView, CreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import UserRegisterSerializer,UserLoginSerializer,ListSerializer,CreateSerializer,DetailSerializer
from .models import Pokemon
from .permissions import IsPaidUser


from rest_framework.permissions import IsAuthenticated, IsAdminUser




class RegisterUserView(CreateAPIView):

	serializer_class = UserRegisterSerializer



class LoginView(GenericAPIView):
	"""
	to-do:
	add custom/extra model attributes
	custom view behavior

	"""
	serializer_class = UserLoginSerializer



class PokeListApiView(ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = ListSerializer



class AddPokeApiView(CreateAPIView):
    
    serializer_class = CreateSerializer

    # def perform_create(self,serializer):
    #     return serializer.save(player=self.request.user)


class EditPokeView(RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg ='pokemon_id'
    serializer_class = DetailSerializer
    permission_classes = [IsPaidUser]



