from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """Сериалайзер модели контакта"""
    class Meta:
        model = Contact
        fields = '__all__'
