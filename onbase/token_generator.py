from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, volunteer, timestamp):
        return (
            six.text_type(volunteer.id) + six.text_type(timestamp) + six.text_type(volunteer.is_active)
        )

account_activation_token = TokenGenerator()