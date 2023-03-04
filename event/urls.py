from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

# urlpatterns = [
#     path('add_event', views.add_event, name='add-event'),
#     path('event_list', views.event_list, name='event-list'),
#     path('update_event/<str:pk>/', views.update_event, name='update-event'),
#     path('patch_event/<str:pk>/', views.patch_event, name='patch-event'),
#     path('get_event/<str:pk>/', views.get_event, name='get-event'),
#     path('delete_event/<str:pk>/', views.delete_event, name='delete-event')
# ]

router = DefaultRouter()
router.register('', viewset=views.EventViewSet, basename='event')
urlpatterns = router.urls
