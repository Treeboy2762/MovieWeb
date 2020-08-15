from django.db import models
from django.contrib.auth.models import User
# from datetime import datetime
# import time

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default='M')
    age = models.IntegerField(default=25)
    occupation = models.CharField(max_length=200)


#  wrapper for create user Profile
def create_profile(**kwargs):

    user = User.objects.create_user(
        username=kwargs['username'],
        password=kwargs['password'],
        is_active=True,
    )

    profile = Profile.objects.create(
        user=user,
        gender=kwargs['gender'],
        age=kwargs['age'],
        occupation=kwargs['occupation']
    )

    return profile

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=500)
    likes = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    count = models.IntegerField(default=0)

    @property
    def genres_array(self):
        return self.genres.strip().split('|')


class Rating(models.Model):
    # username = models.ForeignKey(User, on_delete=models.CASCADE)
    # movieid = models.ForeignKey(Movie, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    movieid = models.CharField(max_length=200, default="0")
    rate = models.IntegerField(blank=True)
    time = models.DateTimeField(auto_now=True)