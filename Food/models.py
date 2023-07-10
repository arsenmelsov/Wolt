from django.db import models
from Branch.models import Branch
import uuid

class Food(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=50, null=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def str(self):
        return self.name