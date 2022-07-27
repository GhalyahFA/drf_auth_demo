from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import UserRegisterSerializer




class RegisterUserView(CreateAPIView):

	serializer_class = UserRegisterSerializer

class LoginView():
	"""
	to-do:
	add custom/extra model attributes
	custom view behavior

	"""
	pass