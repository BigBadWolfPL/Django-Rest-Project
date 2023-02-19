from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from blog.models import Images
import pytz
import datetime
from rest_framework.authtoken.models import Token


class ExpiringTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise AuthenticationFailed('User inactive or deletad')

        utc_now = datetime.datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)

        # Checking token time-to-live
        # set by the user when adding a photo.
        user_post = Images.objects.all().last()
        user_time = user_post.time

        if user_time < 300 or user_time is None:
            user_time = 300
        elif user_time > 30000:
            user_time = 30000

        if token.created < utc_now - datetime.timedelta(seconds=user_time):
            raise AuthenticationFailed('Token has expired')

        return token.user, token