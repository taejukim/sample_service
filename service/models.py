from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Post'
        managed = True
