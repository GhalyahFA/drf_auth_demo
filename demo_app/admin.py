from django.contrib import admin
from .models import Pokemon, Collection


class PokemonAdmin(admin.ModelAdmin):
	list_display = ('id', 'name',)


# Register your models here.
admin.site.register(Pokemon,PokemonAdmin)
admin.site.register(Collection)
