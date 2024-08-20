from django.db import models


class CommonPassword(models.Model):
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField()
