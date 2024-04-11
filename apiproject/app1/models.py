from django.db import models
from froala_editor.fields import FroalaField
# Create your models here.
class BlogModel(models.Model):
        title = models.CharField(max_length=100)
        content = FroalaField()
        created_at = models.DateTimeField(auto_now_add=True)
        upload_at = models.DateTimeField(auto_now=True)

        def __str__(self):
                return self.title