from django.db import models
from City.models import City
import uuid

class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=50, null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def str(self):
        return self.name
