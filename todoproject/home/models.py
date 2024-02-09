from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todolist(models.Model):
    task = models.TextField()
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    


    def __str__(self) -> str:
        return self.task