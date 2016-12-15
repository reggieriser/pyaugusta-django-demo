from django.db import models


class Specialty(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        verbose_name_plural = 'specialties'

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    dob = models.DateField("date of birth", null=True, blank=True)
    specialties = models.ManyToManyField(Specialty)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)
