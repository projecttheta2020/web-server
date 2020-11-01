from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from accounts.utils import delete_user_token
from common.consts import ErrorCodes
from common.utils import resolve_response
from permissioning.permissions import default_permissions, auth_permissions
from accounts.utils import AccountValidator
from teacher_profile.enums import Status
from teacher_profile.utils import create_teacher, get_teacher_status


class LoginView(APIView):
    permission_classes = default_permissions

    def post(self, request):
        username = request.data["email"]
        if request.data['create_user']:
            if User.objects.filter(username=username).count():
                return resolve_response(
                    **dict(
                        error=True,
                        msg='User Already Exists'
                    )
                )
            user = User.objects.create_user(username=username, password=request.data['password'], email=username)
            user.save()
            token = Token.objects.create(user=user)
            token.save()
            if request.data['is_teacher']:
                create_teacher(user, username)
            # else:
            #     create_school()
            response = {'id': user.id, 'email': username, 'accessToken': token.key,
                        'onboarding_status': Status.Pending.value}

        else:
            user = AccountValidator(request).get()
            if user is None:
                return resolve_response(
                    **dict(
                        error=True,
                        msg='Invalid User'
                    )
                )
            if not user.is_active:
                return resolve_response(
                    **dict(
                        error=True,
                        msg='User not Active'
                    )
                )
            token = Token.objects.create(user=user)
            token.save()

            response = {'email': user.username, 'accessToken': token.key}
            teacher_status = get_teacher_status(user)
            response['onboarding_status'] = teacher_status.onboarding_status if teacher_status else Status.Pending.value

        return Response(response, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = auth_permissions

    def get(self, request):
        token = delete_user_token(request.user)
        if not token:
            return resolve_response(
                {'errors': True, 'msg': 'Not Logged In', 'code': ErrorCodes.InvalidRequestParams}
            )
        else:
            return Response(status=status.HTTP_200_OK)


