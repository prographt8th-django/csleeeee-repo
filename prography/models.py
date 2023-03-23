from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class HumanModel(BaseModel):
    name = models.CharField(max_length=32, unique=True, null=True, blank=True)
    description = models.TextField(max_length=500)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
