from .models import Course, Branch
from rest_framework import serializers

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ("latitude", "longtitude", "address",)

class CourseSerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True)
    class Meta:
        model = Course
        fields = ('id', "name", "description", "logo", "contact", "category", "branches",)


    def create(self, validated_data):
        branches = validated_data.pop('branches')
        course = Course.objects.create(**validated_data)
        for branches in branches:
            Branch.objects.create(**branches, course=course)
        return course




