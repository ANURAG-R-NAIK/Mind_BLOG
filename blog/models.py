from django.db import models
from django.utils import timezone # for getting time posted
from django.contrib.auth.models import User # for getting the user posting the bolg


# new posts created
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField() # no limit for testfield
    date_posted = models.DateTimeField(default = timezone.now) # time that it is posted
    author = models.ForeignKey(User, on_delete = models.CASCADE) 

    def __str__(self):
        return self.title