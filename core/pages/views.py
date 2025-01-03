import pendulum
from django.db.models import Case, IntegerField, Q, Value, When
from django.views.generic import TemplateView

from core.blog.models.blogs import Blog
from core.events.models.events import Event
from core.profiles.models.profiles import Profile
from core.research.models.projects import Project

# set current time
current_timestamp = pendulum.now()


class Home(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Profile.objects.filter(Q(publish=True) & ~Q(first_name='CCPFEWS')).annotate(
            priority=Case(
                When(role__icontains='Director', then=Value(0)),
                When(role__icontains='Board', then=Value(1)),
                When(title__icontains='Prof', then=Value(2)),
                When(role__icontains='Lecturer', then=Value(3)),
                When(title__icontains='Dr', then=Value(4)),
                default=Value(10),  # Default value for other categories
                output_field=IntegerField(),
            )
        ).order_by('priority', '-creation_date')[:3]

        context['events'] = Event.objects.order_by('-date_published').filter(
            publish=True,
            post_scheduling__lte=current_timestamp,
        )[:4]

        context['projects'] = Project.objects.filter(publish=True, post_scheduling__lte=current_timestamp).annotate(
            priority=Case(
                When(author__first_name__icontains='CCPFEWS', then=Value(0)),
                When(author__role__icontains='Board', then=Value(1)),
                When(author__role__icontains='Director', then=Value(2)),
                When(author__title__icontains='Prof', then=Value(3)),
                default=Value(5),  # Default value for other categories
                output_field=IntegerField(),
            )
        ).order_by('priority', '-date_published')[:4]

        context['posts'] = Blog.objects.order_by('-date_published').filter(
            publish=True,
            schedule_publish__lte=current_timestamp,
        )[:4]

        return context


class About(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = Profile.objects.filter(Q(publish=True) & ~Q(first_name='CCPFEWS')).annotate(
            priority=Case(
                When(role__icontains='Director', then=Value(0)),
                When(role__icontains='Board', then=Value(1)),
                When(title__icontains='Prof', then=Value(2)),
                When(role__icontains='Lecturer', then=Value(3)),
                When(title__icontains='Dr', then=Value(4)),
                default=Value(10),  # Default value for other categories
                output_field=IntegerField(),
            )
        ).order_by('priority', '-creation_date')[:3]

        context['projects'] = Project.objects.filter(publish=True, post_scheduling__lte=current_timestamp).annotate(
            priority=Case(
                When(author__first_name__icontains='CCPFEWS', then=Value(0)),
                When(author__role__icontains='Board', then=Value(1)),
                When(author__role__icontains='Director', then=Value(2)),
                When(author__title__icontains='Prof', then=Value(3)),
                default=Value(5),  # Default value for other categories
                output_field=IntegerField(),
            )
        ).order_by('priority', '-date_published')[:4]

        context['events'] = Event.objects.order_by('-date_published').filter(
            publish=True,
            post_scheduling__lte=current_timestamp,
        )[:3]

        return context
