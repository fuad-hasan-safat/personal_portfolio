from django.db import models
from django.conf import settings


class Resume(models.Model):
    pdf = models.FileField(upload_to='resume/pdf')

