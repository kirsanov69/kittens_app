from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Breed(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Kitten(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age_months = models.IntegerField()
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Rating(models.Model):
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kitten = models.ForeignKey(Kitten, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rating