from django.core.exceptions import ValidationError

from rest_framework import serializers


from django.contrib.auth import get_user_model, authenticate, password_validation

User = get_user_model()

def field_length(fieldname):
    field = next(field for field in User._meta.fields if field.name == fieldname)
    return field.max_length

class RegisterUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=field_length("email"), required=True)
    password1 = serializers.CharField(
        max_length=field_length("password"),
        required=True,
        style={"input_type": "password"},
    )
    password2 = serializers.CharField(
        max_length=field_length("password"),
        required=True,
        style={"input_type": "password"},
    )

    def validate(self, attrs):
        if User.objects.filter(email=attrs["email"]).exists():
            raise serializers.ValidationError("A user with this email already exists")

        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError("Passwords do not match")

        try:
            password_validation.validate_password(attrs["password1"])
        except ValidationError as e:
            raise serializers.ValidationError(str(e))

        return attrs

    def create_user(self, email, password):
        # this is a separate method so it's easy to override
        return User.objects.create_user(username=email, email=email, password=password)

    def save(self):
        email = self.validated_data["email"]
        password = self.validated_data["password1"]

        print(email,password)
        return self.create_user(email, password)