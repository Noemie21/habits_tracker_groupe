from django.db import models

class Habit(models.Model):
    name = models.CharField(max_length=100)
    interval = models.IntegerField()
    qty = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Done(models.Model):
    at = models.DateTimeField(auto_now_add=True)
    habits = models.ManyToManyField(Habit, related_name='habits_dones')

    def __str__(self):
        return f'{self.id} - {self.at}'



