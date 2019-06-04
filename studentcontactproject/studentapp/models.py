from django.db import models

class StudentData(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length=50)
    sloc = models.CharField(max_length=50)
    sfee = models.IntegerField()

