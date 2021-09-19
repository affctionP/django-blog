from django.dispatch import Signal
from .models import PostModel
#post_publish=Signal(providing_args=['task_id'])

"""def do_task():
    if PostModel.status == 'p':
        post_publish(sender='abc_token_done',task_id=123)"""