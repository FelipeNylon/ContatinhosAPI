from django.shortcuts import render
from .models import Contact
from contatos.api.serializers import ContactSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import permissions

class ContactList(ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self,serializer):
        """By insomnia OR postman ou can upload a file """     
        serializer.save(owner= self.request.user)
      
    def get_queryset(self):

        return Contact.objects.filter(owner=self.request.user)
        


class ContactDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id" 

    def perform_create(self,serializer):
        serializer.save(owner= self.request.user)
    
    def get_queryset(self):

        return Contact.objects.filter(owner=self.request.user)