from django.db import models
import uuid

class BranchAddress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    street = models.CharField(max_length=50, null=False)
    house = models.IntegerField()
