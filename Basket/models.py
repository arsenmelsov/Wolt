from django.db import models
from Courier.models import Courier

class Basket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    cost = models.IntegerField()
    arrival_time = models.TimeField()
    rating = models.FloatField()
    payment_status = models.BooleanField(null=False)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
