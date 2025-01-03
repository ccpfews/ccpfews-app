import pendulum
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from core.events.models.events import Event

# set current time
current_timestamp = pendulum.now()


class EventPost(ListView):
    model = Event
    queryset = Event.objects.all()
    template_name = 'event/events.html'
    context_object_name = 'events'
    paginate_by = 6

    def get_queryset(self):
        # return queryset
        return Event.objects.filter(publish=True, post_scheduling__lte=current_timestamp)


class EventDetails(DetailView):
    model = Event
    slug_field = 'event_id'
    template_name = 'event/event-details.html'
    context_object_name = 'event'

    def get_queryset(self):
        return Event.objects.filter(
            event_id=self.kwargs.get('slug'), publish=True, post_scheduling__lte=current_timestamp
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.order_by('-date_published').filter(
            publish=True,
            post_scheduling__lte=current_timestamp,
        )[:3]
        return context
