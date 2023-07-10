from django.db import models
import uuid

class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=50, null=False)

    def str(self):
        return self.name
