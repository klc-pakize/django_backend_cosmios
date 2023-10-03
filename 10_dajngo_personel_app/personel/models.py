from django.db import models
from django.contrib.auth.models import User

class Departman(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    

class Personel(models.Model):

    TITLE = (
        ("Team Lead", 1),
        ("Mid Lead ",2),
        ("Junior",3),
    )

    GENDER = (
        ("f", "Female"),
        ("m", "Mela"),
        ("o", "Other"),
    )

    departman = models.ForeignKey(Departman, on_delete=models.SET_NULL, null=True, related_name='personels')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=10, choices=TITLE, default=3)
    gender = models.CharField(max_length=10, choices=GENDER)
    salary = models.PositiveSmallIntegerField(default=30000)
    start_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.title} - {self.salary}"