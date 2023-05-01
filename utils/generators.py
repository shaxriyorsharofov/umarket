import random
import string
import datetime

from django.utils.text import slugify


def unique_order_id_generator(instance):
    order_id = random_string_generator()
    return f"{order_id}-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



