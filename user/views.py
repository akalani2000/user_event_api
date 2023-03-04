from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from django.contrib.auth import authenticate

from .models import User
from .serializers import RegistrationSerializer, LoginSerializer, ListSerializer


# Create your views here.
@extend_schema(
    request=RegistrationSerializer
)
@api_view(['POST'])
def register_user(request):
    try:
        serializers = RegistrationSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        email = serializers.validated_data['email']
        password = serializers.validated_data['password']
        firstname = serializers.validated_data['firstname']
        lastname = serializers.validated_data['lastname']
        contact_number = serializers.validated_data['contact_number']
        user = User.object.create_user(email=email, password=password, firstname=firstname, lastname=lastname,
                                       contact_number=contact_number)
        token, _ = Token.objects.get_or_create(user=user)
        serializers.validated_data['token'] = token.key
        return Response(data={
            'id': user.pk,
            'email': user.email,
            'firstname': user.firstname,
            'lastname': user.lastname,
            'contact_number': user.contact_number,
            'token': token.key
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'The exception raised{0}'.format(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@extend_schema(request=LoginSerializer)
@api_view(['POST'])
def login_user(request):
    try:
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(username=email, password=password)
        if user is None:
            return Response(data={'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={
            'id': user.pk,
            'email': user.email,
            'firstname': user.firstname,
            'lastname': user.lastname,
            'contact_number': user.contact_number,
            'token': token.key
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'The exception is raised: {0}'.format(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ListAllUsers(generics.ListAPIView):
    queryset = User.object.filter(is_superuser=False)
    serializer_class = ListSerializer


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        if request.user is None:
            return Response(data={'The user is not logged in'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.auth_token.delete()
        return Response(data={'The user logged out successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'The Exception raised: {0}'.format(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def user_profile(request):
#     try:
#         user = User.object.get(pk=request.user.pk)
#         serializer = ListSerializer(user)
#         if not serializer.is_valid():
#             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response(data={'The Exception raised: {0}'.format(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
