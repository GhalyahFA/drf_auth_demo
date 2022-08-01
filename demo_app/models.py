from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pokemon(models.Model):
    class PokemonType(models.TextChoices):
        WATER = "WA"
        GRASS = "GR"
        GHOST = "GH"
        STEEL = "ST"
        FAIRY = "FA"

    name = models.CharField(max_length=30)
    type = models.CharField(max_length=2, choices=PokemonType.choices)
    hp = models.PositiveIntegerField(
        validators=[MinValueValidator(50), MaxValueValidator(350)]
    )
    active = models.BooleanField(default=True)

    # Localizations
    name_fr = models.CharField(max_length=30, default="", blank=True)
    name_jp = models.CharField(max_length=30, default="", blank=True)
    name_ar = models.CharField(max_length=30, default="", blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
    	return self.name



class Collection(models.Model):
	trainer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="collections")
	collection = models.ManyToManyField(Pokemon,related_name="pokemons")

	def __str__(self):
		return f"{self.trainer.first_name} { self.trainer.last_name}"