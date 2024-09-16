from rest_framework import serializers
from .models import Customer, User

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'surname', 'customer_id', 'photo', 'created_by', 'modified_by', 'created_at', 'updated_at']
        read_only_fields = ['created_by', 'modified_by']

    def validate_customer_id(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("The client ID must be alphanumeric.")
        return value

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'is_active']
        read_only_fields = ['is_staff', 'is_active']

    def validate_username(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("The username must be alphanumeric.")
        return value