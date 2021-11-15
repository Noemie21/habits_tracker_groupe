from django.urls import include, path
from rest_framework import routers
from habits_tracker_groupe import views
from django.views.generic import TemplateView
from habits_tracker_groupe.models import Done, Habit


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'habits', views.HabitViewSet)
router.register(r'dones', views.DoneViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),
]