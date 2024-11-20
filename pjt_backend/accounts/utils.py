from django.contrib.auth import get_user_model
from django.core.exceptions import FieldDoesNotExist

# 정수 타입이나 날짜 타입 같은 순환 불가능한 객체의 경우
# 아래 표시된 v = v[0:max_length] 에서 오류가 뜨기 때문에
# 커스텀한 user_field 메소드를 사용해야 한다
# 아니면 allauth.account.utils 모듈에서 직접 수정해야 함

def user_field(user, field, *args, commit=False):
    """
    Gets or sets (optional) user model fields. No-op if fields do not exist.
    """
    if not field:
        return
    User = get_user_model()
    try:
        field_meta = User._meta.get_field(field)
        max_length = field_meta.max_length
    except FieldDoesNotExist:
        if not hasattr(user, field):
            return
        max_length = None
    if args:
        # Setter
        v = args[0]
        if v:
            if '__iter__' in dir(v):
                v = v[0:max_length]
        setattr(user, field, v)
        if commit:
            user.save(update_fields=[field])
    else:
        # Getter
        return getattr(user, field)
