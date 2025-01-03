import pendulum
from django.db.models import Case, IntegerField, Q, Value, When
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from core.events.models.events import Event
from core.profiles.models.profiles import Profile
from core.research.models.projects import Project

# set current time
current_timestamp = pendulum.now()


class Team(ListView):
    model = Profile
    queryset = Profile.objects.filter(Q(publish=True) & ~Q(first_name='CCPFEWS'))
    template_name = 'team/team.html'
    context_object_name = 'profiles'
    paginate_by = 6

    def get_queryset(self):
        return Profile.objects.filter(Q(publish=True) & ~Q(first_name='CCPFEWS')).annotate(
            priority=Case(
                When(role__icontains='Director', then=Value(0)),
                When(role__icontains='Board', then=Value(1)),
                When(title__icontains='Prof', then=Value(2)),
                When(role__icontains='Lecturer', then=Value(3)),
                When(title__icontains='Dr', then=Value(4)),
                default=Value(10),  # Default value for other categories
                output_field=IntegerField(),
            )
        ).order_by('priority', '-creation_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.order_by('-date_published').filter(
            publish=True,
            post_scheduling__lte=current_timestamp,
        )[:3]
        return context


class TeamDetails(DetailView):
    model = Profile
    slug_field = 'profile_id'
    template_name = 'team/team-details.html'
    context_object_name = 'profile'

    def get_queryset(self):
        return Profile.objects.filter(
            Q(profile_id=self.kwargs.get('slug')) & Q(publish=True) & ~Q(first_name='CCPFEWS')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.order_by('-date_published').filter(
            publish=True,
            post_scheduling__lte=current_timestamp,
        )[:3]
        context['projects'] = Project.objects.order_by('-date_published').filter(
            publish=True,
            post_scheduling__lte=current_timestamp,
        )
        return context
