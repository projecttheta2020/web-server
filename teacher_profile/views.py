from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.utils import resolve_response
from permissioning.permissions import teacher_permissions
from teacher_profile.enums import Status
from teacher_profile.models import TeacherProfileDetails, TeacherStatus
from teacher_profile.saerializer import TeacherOnboardingSerializer


class TeacherOnboarding(APIView):
    permission_classes = teacher_permissions
    model = TeacherProfileDetails
    serializer_class = TeacherOnboardingSerializer
    queryset = TeacherProfileDetails.objects.all()

    def post(self, request):
        try:
            instance = self.model.objects.get(user=request.user)
        except self.model.DoesNotExist:
            print('teacher does not exist')
            return resolve_response(
                **dict(
                    error=True,
                    msg='Teacher Does Not Exist'
                )
            )
        serializer = self.serializer_class(data=request.data, instance=instance)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            teacher_status = TeacherStatus.objects.get_or_create(user=request.user)[0]
            teacher_status.onboarding_status = Status.Completed.value
            teacher_status.save()

        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        try:
            instance = self.model.objects.get(user=request.user)
        except self.model.DoesNotExist:
            print('teacher does not exist')
            return resolve_response(
                **dict(
                    error=True,
                    msg='Teacher Does Not Exist'
                )
            )

        data = self.serializer_class(instance=instance).data

        return Response(data, status=status.HTTP_200_OK)

