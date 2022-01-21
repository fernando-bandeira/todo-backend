from django.db import models

class Todo(models.Model):
    title = models.CharField('Title', max_length=120)
    description = models.CharField('Description', max_length=250)
    status = models.BooleanField('Completed', default=False)

    def __str__(self):
        return self.title
