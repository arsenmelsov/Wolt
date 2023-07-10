from django.db import models
from Food.models import Food
from Basket.models import Basket
import uuid

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
