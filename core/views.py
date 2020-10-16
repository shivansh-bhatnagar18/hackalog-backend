from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from .serializers import HackathonSerializer
from .models import Hackathon

class HackathonCreateView(generics.CreateAPIView):
    '''
    API used to create hackathon objects. Can only be accessed by the Super User
    '''
    serializer_class = HackathonSerializer
    permission_classes = [permissions.IsAdminUser]

class HackathonsRUDView(generics.RetrieveUpdateDestroyAPIView):
    '''
    API used to read, update or delete the hackathon objects by their id. Only the Super User has the permissions to update or delete hackathon objects.
    '''
    
    class HackathonPermissions(permissions.BasePermission):
        '''
        1. GET can be accessed even by anonymous users
        2. PUT, PATCH and DELETE can only be accessed by the Super User
        '''
        def has_permission(self, request, view):
            if (request.method in ['PUT','PATCH','DELETE']):
                return bool(request.user and request.user.is_superuser)
            elif (request.method == 'GET'):
                return True
            else:
                return False
    
    permission_classes = [HackathonPermissions]
    serializer_class = HackathonSerializer
    lookup_url_kwarg = 'id'
    queryset = Hackathon.objects.all()
