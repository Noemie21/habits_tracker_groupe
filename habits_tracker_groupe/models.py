from django.db import models

class Done(models.Model):
    at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.at

class Habit(models.Model):
    name = models.CharField(max_length=100)
    interval = models.IntegerField()
    qty = models.IntegerField()
    done = models.ForeignKey(Done, blank=True,on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

