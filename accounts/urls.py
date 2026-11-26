# creating urls which connect web endpoint to this code 

from django.urls import path
from .views import UserRegistrationView

urlpatterns = [
    path(
        #endpoint name
        'register/',
        UserRegistrationView.as_view(),
        name='user-register'
    ),
]