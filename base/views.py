from rest_framework.decorators import api_view  # Correct decorator
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()  # Query all users from the database
    serialized_data = UserSerializer(users, many=True)  # Serialize the queryset
    return Response(serialized_data.data, status=status.HTTP_200_OK)  # Access .data to return serialized content


@api_view(['POST'])
def create_user(request):
    # Create a serializer instance with incoming data
    serializer = UserSerializer(data=request.data)
    
    # Check if the incoming data is valid according to the serializer
    if serializer.is_valid():
        # Save the valid data to the database
        serializer.save()
        
        # Return the serialized data with 201 Created status
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # Return validation errors with a 400 Bad Request status
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        # Fetch the user by primary key
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        # Return 404 if the user is not found
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # For GET requests, return the user data
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # For PUT requests, update the user with the provided data
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # For DELETE requests, delete the user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 