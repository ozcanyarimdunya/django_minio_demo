from django.db import models


class Todo(models.Model):
    """
    A simple model that has name, cover image and document file
    We assume that cover and document will be saved to minio server
    """
    name = models.CharField(max_length=120)
    cover = models.FileField(upload_to='uploads/')
    document = models.FileField()

    def __str__(self):
        return self.name
