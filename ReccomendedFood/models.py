from django.db import models
from Food.models import Food
import uuid

class ReccomendedFood(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=50, null=False)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def str(self):
        return self.name

