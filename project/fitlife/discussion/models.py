from django.db import models

class Discussion(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    likes = models.PositiveIntegerField(default=0)  # Count of likes
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the discussion was created

    def __str__(self):
        return self.title


class Reply(models.Model):
    discussion = models.ForeignKey(Discussion, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the reply was created
    updated_at = models.DateTimeField(auto_now=True)      # Timestamp for when the reply was last updated

    def __str__(self):
        return f"Reply to {self.discussion.title} by {self.id}"
