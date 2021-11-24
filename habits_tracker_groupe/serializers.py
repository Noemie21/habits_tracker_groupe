import re
from django.contrib.auth.models import User, Group
from django.db.models.query import QuerySet
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from habits_tracker_groupe.models import Done, Habit
from rest_framework.reverse import reverse

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']
        


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class DoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Done
        fields = ['url','at', 'habits']
        
class HabitSerializer(serializers.HyperlinkedModelSerializer):
    def get_done(self, obj):
        print(obj.id)
        return reverse('habit-dones-list', args=[obj.id], request=self.context["request"])


    done = SerializerMethodField()

    class Meta:
        model = Habit
        fields = ['url', 'name', "interval", "qty", "created", "done"]





