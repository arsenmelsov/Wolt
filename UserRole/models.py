from django.db import models
from Users.models import User
from Role.models import Role
import uuid

class UserRole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def str(self):
        return self.name