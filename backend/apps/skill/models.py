from uuid import uuid4
from django.db import models


class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=130)
    standardized = models.BooleanField(default=False)

    def __str__(self):
        return self.name
