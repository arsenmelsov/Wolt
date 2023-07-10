from django.db import models
from Restaurant.models import Restaurant
from BranchAddress.models import BranchAddress
import uuid

class Branch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    radius = models.IntegerField()
    rating = models.FloatField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    address = models.ForeignKey(BranchAddress, on_delete=models.CASCADE)
