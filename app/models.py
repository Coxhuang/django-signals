from django.db import models


class Student(models.Model):

    name = models.CharField(verbose_name="姓名", max_length=16)
