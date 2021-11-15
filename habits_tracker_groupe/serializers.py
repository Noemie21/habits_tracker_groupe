from django.contrib.auth.models import User, Group
from django.db.models.fields import NullBooleanField
from rest_framework import serializers
from habits_tracker_groupe.models import Done, Habit


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class HabitSerializer(serializers.HyperlinkedModelSerializer):
    done = serializers.HyperlinkedRelatedField(
        many=True,
        queryset=Done.objects.all(),
        view_name='habit-done',
        allow_null=True
    )
    class Meta:
        model = Habit
        fields = ['url', 'name', "interval", "qty", "done", "created"]
    
    def to_internal_value(self, data):
        test = super().to_internal_value(data)
        test["done"] = None
        return test


class DoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Done
        fields = ['at']
