from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CustomEmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        print("CustomEmailBackend authenticate method called with email:", email)
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=email)
        except user_model.DoesNotExist:
            print("User with email", email, "does not exist")
            return None
        else:
            if user.check_password(password):
                print("User authentication successful for email:", email)
                return user
        print("User authentication failed for email:", email)
        return None
