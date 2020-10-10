from rest_framework import serializers

from teacher_profile.models import TeacherProfileDetails


class TeacherOnboardingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfileDetails
        fields = ['job_role', 'preferred_subjects', 'total_experience', 'highest_education', 'preferred_city', 'start_date']

