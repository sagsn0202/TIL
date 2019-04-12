from django.db import models
from faker import Faker

faker = Faker()


class Client(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ('name',)

    @classmethod
    def dummy(cls, n):
        for i in range(n):
            cls.objects.create(name=faker.name())


class Hotel(models.Model):
    name = models.CharField(max_length=20)
    clients = models.ManyToManyField(Client)

    @classmethod
    def dummy(cls, n):
        for i in range(n):
            cls.objects.create(name=faker.company())


class Student(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id} {self.name}'


class Lecture(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return f'{self.id} {self.title}'


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.student} {self.lecture}'
