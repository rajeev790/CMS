from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    # Add other relevant fields

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    # Add other relevant fields

    def __str__(self):
        return self.title

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add other relevant fields

    def __str__(self):
        return f"Like {self.id} for Post {self.post}"
