from rest_framework.serializers import ModelSerializer
from contatos.models import Contact


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        """By insomnia OR postman ou can upload a file """
        fields = ['ddd','name','number_tel','photo','favorited']

