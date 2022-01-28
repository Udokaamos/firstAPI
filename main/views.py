from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

@api_view(['GET', 'POST'])
def user_view(request):

    if request.method == 'GET':
        all_users = User.objects.all()


        serializer = UserSerializer(all_users, many=True)

        data = {
            "message":"successful",
            "data": serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)
