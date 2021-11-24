from decimal import Context
from django.contrib.auth.models import User, Group
from django.db.models.query import QuerySet
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from habits_tracker_groupe import serializers
from habits_tracker_groupe.models import Done, Habit
from rest_framework.response import Response

from habits_tracker_groupe.serializers import DoneSerializer, GroupSerializer, UserSerializer, HabitSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import status


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
        try: 
            return Done.objects.filter(habits=self.kwargs['habit_pk'])
        except:
            return Done.objects.all()
        
class CurrentUser(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user, context={'request': request})
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(request.user,data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        serializer = UserSerializer(request.user, context={'request': request})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

