from allauth.account.adapter import DefaultAccountAdapter
from rest_framework import serializers
from .models import Job

# adapter는 django-allauth의 기본 동작(로그인, 회원가입, 비번변경 등등)을
# 커스텀 하고 싶을때 쓰는 모듈이다

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_username
        from .utils import user_field

        # cleaned_data는 RegisterSerializer의 get_cleaned_data()로 받아온 값
        # 즉, 회원가입 할때 입력한 값들이 들어있는 딕셔너리이다
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        name = data.get('name')
        age = data.get('age')
        gender = data.get('gender')
        birthday = data.get('birthday')
        address = data.get('address')
        job_id = data.get('job_id')
        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if name:
            user_field(user, "name", name)
        if age:
            user_field(user, "age", age)
        if gender:
            user_field(user, "gender", gender)
        if birthday:
            user_field(user, "birthday", birthday)
        if address:
            user_field(user, "address", address)
        # job_id를 외래키로 Job 테이블에서 job_name을 가져올 것이기 때문에
        # job_id를 키로 갖는 튜플을 job 테이블에서 가져와 할당한다
        if job_id:
            try:
                job_instance = Job.objects.get(pk=job_id)
                user.job_id = job_instance
            except Job.DoesNotExist:
                raise serializers.ValidationError("Invalid job_id provided.")
        if "password1" in data:
            user.set_password(data["password1"])
        elif "password" in data:
            user.set_password(data["password"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user
