import pendulum
from django.shortcuts import render

from core.events.models.events import Event

# set current time
current_timestamp = pendulum.now()

# init context
context = {
    'events':
        Event.objects.order_by('-date_published').filter(
            publish=True,
            post_scheduling__lte=current_timestamp,
        )[:3]
}


def page_not_found(request, exception):
    return render(request, 'errors/404.html', context=context, status=404)


def server_error(request):
    return render(request, 'errors/500.html', context=context, status=500)


def bad_request(request, exception):
    return render(request, 'errors/400.html', context=context, status=400)


def permission_denied(request, exception):
    return render(request, 'errors/403.html', context=context, status=403)
