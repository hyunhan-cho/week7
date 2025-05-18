from django.db import models

class Post(models.Model):
    title      = models.CharField(max_length=256)
    body       = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post       = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment    = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Comment #{self.id} on {self.post.id}'
    