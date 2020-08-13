import logging
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from accounts.models import ApiSecretToken


class ApiTokenPermission(permissions.BasePermission):
    message = {'error': 'API not authorised'}

    def has_permission(self, request, view):
        try:
            secret = request.META['HTTP_APP_SECRET']
            token = ApiSecretToken.objects.get(api_key=secret)
            # if token.is_valid():
            #     request.format_numbers = token.is_web_client
            return True
            # return False
        except (ApiSecretToken.DoesNotExist, KeyError):
            logging.critical(
                [
                    "Unauthorised Request",
                    request.__dict__
                ]
            )
            return False


default_permissions = [ApiTokenPermission, ]
auth_permissions = [ApiTokenPermission, IsAuthenticated, ]