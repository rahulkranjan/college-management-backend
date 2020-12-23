from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# from rest_framework import viewsets
# from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from .serializers import BranchSerializers, CollegeSerializers
from .models import College, Branches
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# from rest_framework.pagination import PageNumberPagination


class BranchAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                    mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin):
    # permission_classes = (permissions.IsAuthenticated, AdminPermissions, SuperAdminPermissions,
    #                       VendorPermissions, Delivery_PartnerPermissions, ClintPermissions)
    serializer_class = BranchSerializers
    queryset = Branches.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['branch_name', 'created_at', 'status', 'slug']
    search_fields = ['branch_name']
    # ordering_fields = ['name']

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class CollegeAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    # permission_classes = (permissions.IsAuthenticated, AdminPermissions, SuperAdminPermissions,
    #                       VendorPermissions, Delivery_PartnerPermissions, ClintPermissions)
    serializer_class = CollegeSerializers
    queryset = College.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['college_name', 'created_at', 'status', 'slug']
    search_fields = ['college_name']
    # ordering_fields = ['name']

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)
