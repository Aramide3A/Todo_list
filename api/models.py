from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo_list(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.CharField(max_length=50, blank= False)
    description = models.TextField(max_length=300, blank=True, null = True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
