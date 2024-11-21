from rest_framework import serializers
from allauth.account.adapter import get_adapter
from allauth.account import app_settings as allauth_account_settings
from allauth.socialaccount.models import EmailAddress
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from .models import User

class UserProfileSerializer(serializers.ModelSerializer):
    # class UserJobNameSeiralizer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Job
    #         fields = ('job_name',)
            
    # job = UserJobNameSeiralizer(read_only=True)
    
    class Meta:
        model = User
        fields = ('name', 'email', 'age', 'gender', 'birthday', 'address', 'job')


class CustomRegisterSerializer(RegisterSerializer):
    # 입력 받기 위해 abstratuser 모델에서 추가된 필드들 추가
    name = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    gender = serializers.CharField(required=True)
    birthday = serializers.DateField(required=True)
    address = serializers.CharField(required=True)
    # job_id = serializers.IntegerField(required=True)
    job = serializers.CharField(required=False)
    
    # username 필드 제거
    username = None
    def validate_username(self, username):
        return None
    
    def validate_email(self, email):
        # email 중복되면 에러메시지    
        email = get_adapter().clean_email(email)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email already exists.")
        # 이건 유효성 검사(원래 있던거)
        if allauth_account_settings.UNIQUE_EMAIL:
            if email and EmailAddress.objects.is_verified(email):
                raise serializers.ValidationError(
                    _('A user is already registered with this e-mail address.'),
                )
        return email
    
    # 회원가입시 입력한 데이터 받아오는 메소드
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
            # 'job_id': self.validated_data.get('job_id', ''),
            'job': self.validated_data.get('job', ''),
        }

UserModel = get_user_model()

# 추가된 필드들을 포함한 유저 정보를 프론트서버로 보내기 위한 시리얼라이저
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
        # if hasattr(UserModel, 'job_id'):
        #     extra_fields.append('job_id')
        if hasattr(UserModel, 'job'):
            extra_fields.append('job')
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)