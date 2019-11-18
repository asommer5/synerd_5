from rest_framework import serializers
from ..models import Service, Subscriber, Organization
class ServiceSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Service
        fields = ['servicecode', 'servicename', 'description', 'premium', 'allocation']

class SubscriberSerializer(serializers.ModelSerializer):
    class MEta:
        model = Subscriber
        fields = ['subscriberID', 'username', 'subscriptiontypecode', 'servicecode', 'requestdate', 'startdate', 'enddate', 'motifofcancellation', 'beneficiaryID']

class OrganizationSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Organization
        fields = ['organization_code', 'ogranization_name', 'description', 'date_joined', 'address1', 'address2', 'city', 'state', 'zipcode', 'phone_number']
