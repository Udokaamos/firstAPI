from rest_framework.response import Response
from rest_framework import status 
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

User = get_user_model()


@swagger_auto_schema(method='post', 
                    request_body=UserSerializer(),
                    operation_description="This is a function to create new users.",
                    responses= {201: openapi.Response("""An example success response is:
                    ``{
                        "message": "successful",
                        "data": [
                            {
                                "id": 1,
                                "first_name": "Test",
                                "last_name": "User",
                                "email": "test@user.com",
                                "phone": "234123456789",
                                "date_joined":"2022-01-26T10:33:45.239782Z"
                            }
                        ]
                    }``"""),
                        400: openapi.Response("""An example failure is:
                        ``{
                        "message": "failed",
                        "error": {
                            "email": [
                            "This field is required."
                            ],
                            "password": [
                            "This field is required."
                            ],
                            "phone": [
                            "This field is required."
                            ]
                        }``""")
                    }
)
@api_view(['GET', 'POST'])
def user_view(request):
    
    if request.method == 'GET':
        # Get all the users in the database
        all_users = User.objects.all()
        
        serializer = UserSerializer(all_users, many=True)
        
        data = {
           "message":"successful",
           "data": serializer.data
        }
    
    
        # return JsonResponse(data)
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        #Allows user to signup or create account
        serializer = UserSerializer(data=request.data) #deserialize the data
        
        if serializer.is_valid(): #validate the data that was passed
            serializer.save()
            data = {
                'message' : 'success',
                'data'  : serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                'message' : 'failed',
                'error'  : serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

# from distutils.log import error
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view
# from .serializers import UserSerializer
# from django.contrib.auth import get_user_model


# User = get_user_model()

# @api_view(['GET', 'POST'])
# def user_view(request):

#     if request.method == 'GET':
#         all_users = User.objects.all()


#         serializer = UserSerializer(all_users, many=True)

#         data = {
#             "message":"successful",
#             "data": serializer.data
#         }

#         # return JsonResponse(data)
#         return Response(data, status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         #Allows user to signup or create account
#         serializer = UserSerializer(data=request.data) #deserialize

#         if serializer.is_valid(): #validate the data that was passed
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             data = {
#                 'message' : 'failed',
#                 'error' : serializer.errors
#             }
