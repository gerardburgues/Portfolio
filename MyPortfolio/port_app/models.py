from django.db import models
from django.utils import timezone
# Create your models here.

class Projects(models.Model):
    link_git = models.URLField(max_length = 128)
    project_name = models.CharField(max_length = 128)
    explanation  =models.CharField(max_length = 300)
    time_posted = models.DateTimeField (default = timezone.now)

    def __str__(self):
        return self.project_name
