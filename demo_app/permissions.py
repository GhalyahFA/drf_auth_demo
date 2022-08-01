from rest_framework.permissions import BasePermission


class IsPaidUser(BasePermission):

	def has_object_permission(self,request,view,obj):
		print(obj.pokemons)
		print(request.user)

		return  obj.pokemons== request.user



