from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from firstdateapp.models import Customer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for customer

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Customer
        url = serializers.HyperlinkedIdentityField(
            view_name='customer',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name', 'favorites')


class Customers(ViewSet):
    """customer for First Date App"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single customer

        Returns:
            Response -- JSON serialized customer instance
        """
        try:
            customer = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(customer, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to customer resource

        Returns:
            Response -- JSON serialized list of customer
        """
        customers = Customer.objects.all()
        serializer = CustomerSerializer(
            customers,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)