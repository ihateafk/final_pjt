from django.contrib.auth import get_user_model
from django.core.exceptions import FieldDoesNotExist

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
