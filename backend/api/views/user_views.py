
from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Profile
from api.serializers import ProfileSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST', 'DELETE'])
def user_many(request):

    if request.method == 'GET':
        id = request.GET.get('id', None)

        users = Profile.objects.all()
        if id:
            users = users.filter(id__exact=id)
        serializer = ProfileSerializer(users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        user = Profile.objects.all()
        user.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        users = request.data.get('users', None)
        for profile in users:
            username = profile.get('username', None)
            password = profile.get('password', None)
            age = profile.get('age', None)
            occupation = profile.get('occupation', None)
            gender = profile.get('gender', None)

            Profile(username=username, password=password, age=age, occupation=occupation, gender=gender).save()

        return Response(status=status.HTTP_200_OK)