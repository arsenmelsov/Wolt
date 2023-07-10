from django.db import models
from Role.models import Role
from Card.models import Card
from Address.models import Address
from Order.models import Order
import uuid


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)
    phone_number = models.TextField(null=False)
    email = models.EmailField(null=False)
    password = models.CharField(max_length = 50, null=False)
    userRole = models.ManyToManyField(Role)
    userCard = models.ManyToManyField(Card)
    userAddress = models.ManyToManyField(Address)
    userOrder = models.ManyToManyField(Order)

    def str(self):
        return self.name
