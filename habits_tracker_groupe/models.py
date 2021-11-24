from django.db import models

class Habit(models.Model):
    INTERVALS = (
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Monthly'),
    )
    name = models.CharField(max_length=100)
    interval = models.CharField(max_length=1, choices=INTERVALS)
    qty = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Done(models.Model):
    at = models.DateTimeField(auto_now_add=True)
    habits = models.ManyToManyField(Habit, related_name='habits_dones', blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.at}'



