from django.db import models
from City.models import City
from Users.models import User
import uuid

class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    street = models.CharField(max_length=50, null=False)
    house = models.CharField(max_length=50, null=False)
    apartment = models.IntegerField(blank=True, null=True)
    entrance = models.IntegerField(blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
