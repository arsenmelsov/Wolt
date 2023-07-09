from django.db import models
from Users.models import User
from Card.models import Card
import uuid

class UserCard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def str(self):
        return self.name