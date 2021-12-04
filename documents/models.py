from django.db import models

class Document(models.Model):
    title = models.TextField()
    content = models.TextField()
