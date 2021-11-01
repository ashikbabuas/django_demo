from django.db import models


class TblTags(models.Model):
    title = models.CharField(max_length=150)


class TblSnippets(models.Model):

    title = models.CharField(max_length=150)
    snippet = models.TextField()
    tags = models.ManyToManyField(TblTags, related_name="tags")
    timestamp = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
