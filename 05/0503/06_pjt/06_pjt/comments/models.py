from django.db import models


class CommentResult(models.Model):
    company_name = models.CharField(max_length=100)
    raw_comments = models.TextField(blank=True)
    cleaned_comments = models.TextField(blank=True)
    augmented_comments = models.TextField(blank=True)
    iqr_info = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name