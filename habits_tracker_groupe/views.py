from django.contrib.auth.models import User, Group
from django.db.models.query import QuerySet
from rest_framework import viewsets
from rest_framework import permissions
from habits_tracker_groupe.models import Done, Habit

from habits_tracker_groupe.serializers import DoneSerializer, GroupSerializer, UserSerializer, HabitSerializer
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class HabitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

class DoneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = DoneSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Done.objects.filter(habits=self.kwargs['habit_pk'])

