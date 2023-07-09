from django.db import models
import uuid

class Card(models.Model):
    number = models.TextField(null=False)
    date = models.TextField(null=False)
    cvv = models.TextField(null=False)

    def str(self):
        return self.name
