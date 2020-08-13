from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from accounts.utils import get_user_token, delete_user_token
from common.consts import ErrorCodes
from common.utils import resolve_response
from permissioning.permissions import default_permissions, auth_permissions
from accounts.utils import AccountValidator


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
            user = User.objects.create_user(username=username, password=request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            token.save()
            response = {'email': username, 'accessToken': token.key}
            return Response(response, status=status.HTTP_200_OK)
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
            return Response(response, status=status.HTTP_200_OK)

        # if not request.data['create_user'] and not self.user_exists():
        #     return resolve_response(**dict(error=True, msg='Please register first'))
        # if request.data['create_user'] and self.user_exists():
        #     return resolve_response(**dict(error=True, msg='User already exists'))


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
