from rest_framework import serializers
from .models import Branches, College


class BranchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'


class CollegeSerializers(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'
