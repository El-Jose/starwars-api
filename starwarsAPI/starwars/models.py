from django.db import models


class BaseModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Planet(BaseModel):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Character(BaseModel):

    name = models.CharField(max_length=100)
    height = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=40, blank=True)
    homeworld = models.ForeignKey(Planet, related_name="residents", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Producer(BaseModel):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(BaseModel):

    episode_id = models.IntegerField()
    director = models.CharField(max_length=100)
    opening_text = models.TextField(max_length=1000)
    release_date = models.DateField()
    title = models.CharField(max_length=100)
    planets = models.ManyToManyField(
        Planet,
        related_name="planets_movie",
        blank=True
    )
    characters = models.ManyToManyField(
        Character,
        related_name="characters_movie",
        blank=True
    )
    producers = models.ManyToManyField(
        Producer,
        related_name="producers_movie",
        blank=True
    )

    def __str__(self):
        return self.title
