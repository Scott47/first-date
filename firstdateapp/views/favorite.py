"""View module for handling requests about park areas"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from firstdateapp.models import Favorite


class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for park areas

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Favorite
        url = serializers.HyperlinkedIdentityField(
            view_name='favorite',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name', 'theme')


class Favorites(ViewSet):
    """Favorites for Kennywood Amusement Park"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single park area

        Returns:
            Response -- JSON serialized park area instance
        """
        try:
            favorite = Favorite.objects.get(pk=pk)
            serializer = FavoriteSerializer(favorite, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to park areas resource

        Returns:
            Response -- JSON serialized list of park areas
        """
        favorites = Favorite.objects.all()
        serializer = FavoriteSerializer(
            favorites,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)