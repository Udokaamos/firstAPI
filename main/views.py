from rest_framework.response import Response
from rest_framework import status 
from django.http import JsonResponse
from rest_framework.decorators import api_view
from main.models import Song
from .serializers import  SongSerializer 
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth import authenticate
from django.forms import model_to_dict
from rest_framework.exceptions import ValidationError



@swagger_auto_schema(method='post', 
                    request_body=SongSerializer(),
                    operation_description="This is a function to add new songs.",
                    responses= {201: openapi.Response("""An example success response is:
                    ``{
                        "message": "successful",
                        "data": [
                            {
                                "title": "Test",
                                "artist": "Test",
                                "publish_date": "Test",
                                "date_created": "User",
                            }
                        ]
                    }``"""),
                        400: openapi.Response("""An example failure is:
                        ``{
                        "message": "failed",
                        "error": {
                            "title": [
                            "This field is required."
                            ],
                            "artist": [
                            "This field is required."
                            ],
                        }``""")
                    }
)
@api_view(['GET', 'POST'])
def song_view(request):
    
    if request.method == 'GET':
        # Get all the users in the database
        all_songs = Song.objects.all()
        
        serializer = SongSerializer(all_songs, many=True)
        
        data = {
           "message":"successful",
           "data": serializer.data
        }
    
    
        # return JsonResponse(data)
        return Response(data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        #Allows user to signup or create account
        serializer = SongSerializer(data=request.data) #deserialize the data
        
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

# @swagger_auto_schema(method='post',
#                     request_body=LoginSerializer())
# @api_view(['POST'])
# def login_view(request):

#     serializer = LoginSerializer(data=request.data)

#     if serializer.is_valid():

#         user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])

#         if user:

#             data = {
#                 'message' : 'success',
#                 'data' : model_to_dict(user, ['id',
#                                                'title',
#                                                'artist',
#                                                'publish_date',
#                                                'date_created',
#                                                ])
#                 }
#             return Response(data, status=status.HTTP_201_CREATED)
#         else:
#             data = {
#                     'message' : 'Please enter a valid email and password'
#                 }
#             return Response(data, status=status.HTTP_401_UNAUTHORIZED)
#     else:
#         data = {
#             'message' : 'failed',
#             'error' : serializer.errors
#         }
#     return Response(data, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['put'],
                    request_body=SongSerializer())
@api_view(['GET', 'PUT', 'DELETE'])
def profile_view(request, song_id):

    try:
        user = Song.objects.get(id=song_id)
    except Song.DoesNotExist:


        data = {
            'message' : 'failed',
            'error' : f"Song with ID {song_id} does not exist."
        }
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SongSerializer(user)

        data = {
            "message":"successful",
            "data": serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = SongSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            if 'password' in serializer.validated_data.keys():
                raise ValidationError(detail={
                    "message":"Edit password action not allowed"
                }, code=status.HTTP_403_FORBIDDEN)
            
            serializer.save()
            data = {
                'message' : 'success',
                'data' : serializer.data
            }
            return Response(data, status=status.HTTP_202_ACCEPTED)
        else:
            data = {
                'message' : 'failed',
                'error' : serializer.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=="DELETE":
        user.delete()

        return Response({}, status=status.HTTP_204_NO_CONTENT)






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
