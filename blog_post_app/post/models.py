from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_title = models.CharField(max_length=50)
    post_text = models.TextField(max_length=200)
    post_date = models.DateTimeField(auto_now_add=True)
    post_author = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Posts"
    
    def __str__(self):
        return f'{self.post_title}'