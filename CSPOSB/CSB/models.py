from django.db import models


# Create your models here.
class Course(models.Model):
    cid = models.IntegerField(unique=True, primary_key=True)
    name = models.TextField(unique=True)
    number = models.IntegerField()
    semester = models.TextField()
    department = models.TextField()

    def __str__(self):
        return self.name


class Requirement(models.Model):
    rid = models.IntegerField(unique=True, primary_key=True)
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name


class Degree(models.Model):
    did = models.IntegerField(unique=True, primary_key=True)
    name = models.TextField(unique=True)
    total_credits = models.IntegerField()

    def __str__(self):
        return self.name


class Fulfills(models.Model):
    cid = models.ForeignKey(Course, on_delete=models.CASCADE)
    rid = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    concentration = models.TextField(default="n/a")

    def __str__(self):
        return f'Course: {self.cid} | Requirement: {self.rid}'

    class Meta:
        verbose_name_plural = "Fulfills"


class Requires(models.Model):
    did = models.ForeignKey(Degree, on_delete=models.CASCADE)
    rid = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'Degree: {self.did} | Requirement: {self.rid}'

    class Meta:
        verbose_name_plural = "Requires"
