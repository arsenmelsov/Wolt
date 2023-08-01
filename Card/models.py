from django.db import models
from Users.models import User

class Card(models.Model):
    number = models.TextField(null=False)
    date = models.TextField(null=False)
    cvv = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
