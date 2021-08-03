from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    dateposted = models.DateTimeField(default = timezone.now)
    
