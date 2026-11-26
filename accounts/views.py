from rest_framework import generics
                           #this has all the api methods like fetch , update, create, etc 
from rest_framework.permissions import AllowAny
                                       #any user is allowed to send data 

from .serializer import UserRegistrationSerializer


# creating the view, it provies a endpoint for creating records
class UserRegistrationView(generics.CreateAPIView):

    # telling which serilizer to user
    serializer_class = UserRegistrationSerializer
    #anyone can use 
    permission_classes = [AllowAny]