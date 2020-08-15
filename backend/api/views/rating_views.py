
from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Rating
from api.serializers import RatingsSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST', 'DELETE'])
def ratings(request):

    if request.method == 'GET':
        username = request.GET.get('username', None)
        movieid = request.GET.get('movieid', None)

        ratings = Rating.objects.all()
        if movieid:
            # ratings = ratings.filter(movieid=movieid)
            ratings = ratings.filter(movieid__exact=movieid).values('username')
        if username:
            ratings = ratings.filter(username__exact=username).values('movieid')
        # for rating in ratings:
        #     if rating.userid == movieid:
        #         ratings = rating.filter()

        serializer = RatingsSerializer(ratings, many=False)
        return Response(data=ratings, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        rating = Rating.objects.all()
        rating.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        ratings = request.data.get('ratings', None)
        for r in ratings:
            username = r.get('username', None)
            movieid = r.get('movieid', None)
            rate = r.get('rate', None)
            time = r.get('time', None)

            Rating(username=username, movieid=movieid, rate=rate, time=time).save()

        return Response(status=status.HTTP_200_OK)