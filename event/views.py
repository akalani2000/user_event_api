from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import EventSerializer
from rest_framework import viewsets


# Create your views here.
# @extend_schema(
#     request=EventSerializer
# )
# @api_view(['POST'])
# def add_event(request):
#     serializer = EventSerializer(data=request.data)
#     try:
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data={"the event created successfully"}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e:
#         return Response(data={"the exception is raised {0}".format(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# @extend_schema(
#     request=EventSerializer
# )
# @api_view(['PUT'])
# def update_event(request, pk):
#     event = Event.objects.get(pk=pk)
#     serializer = EventSerializer(instance=event, data=request.data)
#     try:
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data={"the event updated successfully"}, status=status.HTTP_200_OK)
#         else:
#             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     except Exception as e:
#         return Response(data={"the exception is raised {0}".format(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# @extend_schema(
#     request=EventSerializer
# )
# @api_view(['PATCH'])
# def patch_event(request, pk):
#     event = Event.objects.get(pk=pk)
#     serializer = EventSerializer(instance=event, data=request.data, partial=True)
#     try:
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data={"The event updated successfully"}, status=status.HTTP_200_OK)
#         else:
#             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     except Exception as e:
#         return Response(data={"the exception is raised {0}".format(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# @api_view(['GET'])
# def event_list(request):
#     events = Event.objects.all()
#     serializer = EventSerializer(events, None, many=True)
#     if serializer is not None:
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     else:
#         return Response(data={"No events found"}, status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['GET'])
# def get_event(request, pk):
#     event = Event.objects.get_or_404(pk=pk)
#     serializer = EventSerializer(event)
#     return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['DELETE'])
# def delete_event(request, pk):
#     event = Event.objects.get_or_404(pk=pk)
#     event.delete()
#     return Response(data={"The event deleted successfully"}, status=status.HTTP_200_OK)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
