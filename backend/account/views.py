
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import  IsAuthenticated,AllowAny
from rest_framework.decorators import api_view, permission_classes

from helper import IsAdminCompanyJobSearchOrReadOnly

from .models import User
from .serializers import UserSerializer




@api_view(['GET'])
def users(request):
    # must loged in
    if not request.user.is_authenticated:
        return Response(status=401)
    # admin see all users
    if request.user.role == 'admin':
        users = User.objects.all()
    # elif request.user.role == 'company':
    #     users = User.objects.filter(
    #         job_search__job__company == request.user
    #     ).distinct()

    else:
        return Response(
            {'detail': 'Permission denied'},
            status=403
        )

    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE','PATCH'])
@permission_classes([IsAdminCompanyJobSearchOrReadOnly])
def user_detail(request,pk):
    user = get_object_or_404(User,pk=pk)

    # GET - user detail
    if request.method == 'GET':

         # Only admin or owner
        if (request.user.role != 'admin' and
            request.user.id != user.id):
            return Response(
                {'detail': 'Permission denied'},
                status=status.HTTP_403_FORBIDDEN
            )
        return Response(UserSerializer(user).data)
       
    if request.method == 'PATCH':
        serializer = UserSerializer(user,data= request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User updated successfully!','data':serializer.data})
        return Response(serializer.errors,status=400)
    if request.method == 'DELETE':
        user.delete()
        return Response({'message':'User deleted successfully!'}, status=status.HTTP_200_OK)
    
# get logedin user
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)