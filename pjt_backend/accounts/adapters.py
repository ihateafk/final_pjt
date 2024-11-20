from allauth.account.adapter import DefaultAccountAdapter
from rest_framework import serializers
from .models import Job

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_username
        from .utils import user_field

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
        if job_id:
            try:
                # Job 객체로 변환
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
