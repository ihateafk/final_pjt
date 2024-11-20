from rest_framework import serializers
from allauth.account.adapter import get_adapter
from allauth.account import app_settings as allauth_account_settings
from allauth.socialaccount.models import EmailAddress
from django.core.exceptions import ValidationError as DjangoValidationError
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer, UserDetailsSerializer
from django.contrib.auth import get_user_model
from .models import User, Job

class UserProfileSerializer(serializers.ModelSerializer):
    class UserJobNameSeiralizer(serializers.ModelSerializer):
        class Meta:
            model = Job
            fields = ('job_name',)
            
    job = UserJobNameSeiralizer(read_only=True)
    
    class Meta:
        model = User
        fields = ('name', 'email', 'age', 'gender', 'birthday', 'address', 'job_id')


class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    gender = serializers.CharField(required=True)
    birthday = serializers.DateField(required=True)
    address = serializers.CharField(required=True)
    job_id = serializers.IntegerField(required=True)
    
    # username 필드 제거
    username = None
    def validate_username(self, username):
        return None
    
    # email 중복되면 에러메시지    
    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email already exists.")
        
        if allauth_account_settings.UNIQUE_EMAIL:
            if email and EmailAddress.objects.is_verified(email):
                raise serializers.ValidationError(
                    _('A user is already registered with this e-mail address.'),
                )
        return email
    
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
            'name': self.validated_data.get('name', ''),
            'age': self.validated_data.get('age', ''),
            'gender': self.validated_data.get('gender', ''),
            'birthday': self.validated_data.get('birthday', ''),
            'address': self.validated_data.get('address', ''),
            'job_id': self.validated_data.get('job_id', ''),
        }

UserModel = get_user_model()

class CustomUserDetailSerializer(UserDetailsSerializer):
    class Meta:
        extra_fields = []
        # see https://github.com/iMerica/dj-rest-auth/issues/181
        # UserModel.XYZ causing attribute error while importing other
        # classes from `serializers.py`. So, we need to check whether the auth model has
        # the attribute or not
        # if hasattr(UserModel, 'USERNAME_FIELD'):
        #     extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'first_name'):
            extra_fields.append('first_name')
        if hasattr(UserModel, 'last_name'):
            extra_fields.append('last_name')
        if hasattr(UserModel, 'name'):
            extra_fields.append('name')
        if hasattr(UserModel, 'age'):
            extra_fields.append('age')
        if hasattr(UserModel, 'gender'):
            extra_fields.append('gender')
        if hasattr(UserModel, 'birthday'):
            extra_fields.append('birthday')
        if hasattr(UserModel, 'address'):
            extra_fields.append('address')
        if hasattr(UserModel, 'job_id'):
            extra_fields.append('job_id')
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)