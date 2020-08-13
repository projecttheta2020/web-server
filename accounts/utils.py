from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class AccountValidator(object):
    def __init__(self, request):
        try:
            if request.user.is_authenticated:
                self.user = request.user
                return
        except Exception as e:
            print(e)
        username = request.data.get('email', None)
        try:
            if username is not None:
                self.user = User.objects.get(username=username)
            else:
                self.user = None
        except User.DoesNotExist:
            self.user = None

    def get(self):
        return self.user


def get_user_token(user):
    try:
        return Token.objects.get(user=user)
    except Token.DoesNotExist:
        return None


def delete_user_token(user):
    try:
        Token.objects.get(user=user).delete()
        return True
    except Token.DoesNotExist:
        return False
