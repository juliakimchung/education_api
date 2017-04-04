from rest_framework import serializers
from . import models

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            "email": {'write_only': True}
        }
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'rating'
            
        )
        model = models.Review

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'