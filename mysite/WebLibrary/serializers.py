from rest_framework import serializers
from .models import *

"""
class AdministratorSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=45)
    password = serializers.CharField(max_length=45)

    def validate_Administrator(self, value):

        Check if password doesn't contain login
        :param value:
        :return:

        if 'password' in value.lower():
            raise serializers.ValidationError(
                "Password cannot be 'password' "
            )
        """


class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'
