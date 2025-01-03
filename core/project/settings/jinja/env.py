from django.contrib import messages
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment

from .filters import current_datetime, dateformat, intcomma, timesince


def JinjaEnvironment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'get_messages': messages.get_messages,
        'trim_blocks': True,
        'Istrip_blocks': True,
    })
    env.filters.update({
        'dateformat': dateformat,
        'timesince': timesince,
        'intcomma': intcomma,
        'currentdatetime': current_datetime,
    })

    return env
