import pendulum
from django.db.models import Case, IntegerField, Q, Value, When
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from core.events.models.events import Event
from core.profiles.models.profiles import Profile
from core.research.models.projects import Project

# set current time
current_timestamp = pendulum.now()


class ResearchView(TemplateView):
    template_name = 'pages/research.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = Profile.objects.order_by('-creation_date').filter(
            Q(role__in=['Director', 'Board', 'Management', 'Admin']) & Q(publish=True) & ~Q(first_name='CCPFEWS')
        )
        context['events'] = Event.objects.order_by('-date_published').filter(
            publish=True,
            post_scheduling__lte=current_timestamp,
        )[:3]
        return context


class ProjectView(ListView):
    model = Project
    queryset = Project.objects.filter(publish=True, post_scheduling__lte=current_timestamp)
    template_name = 'project/projects.html'
    context_object_name = 'projects'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.order_by('-date_published').filter(
            publish=True,
            post_scheduling__lte=current_timestamp,
        )[:3]
        return context

    def get_queryset(self):
        # init query set
        query = super().get_queryset()

        # check for search
        if self.request.GET.get('search'):
            search = self.request.GET.get('search')

            # update query
            query = self.model.objects.filter(
                Q(post_scheduling__lte=current_timestamp) & Q(publish=True) & (
                    Q(title__icontains=search) | Q(category__icontains=search) |
                    Q(other_innovators__icontains=search) | Q(author__first_name__icontains=search) |
                    Q(status__icontains=search)
                )
            ).annotate(
                priority=Case(
                    When(author__first_name__icontains='CCPFEWS', then=Value(0)),
                    When(author__role__icontains='Board', then=Value(1)),
                    When(author__role__icontains='Director', then=Value(2)),
                    When(author__title__icontains='Prof', then=Value(3)),
                    default=Value(5),  # Default value for other categories
                    output_field=IntegerField(),
                )
            ).order_by('priority', '-date_published')

            # get session
            get_session_search = self.request.session.get('search_list', [])

            if search != '':
                if get_session_search:
                    # update session
                    if len(get_session_search) >= 5:
                        get_session_search_trim = get_session_search[:4]
                        get_session_search_trim.insert(0, search)

                        self.request.session['search_list'] = get_session_search_trim
                    else:
                        #  insert new search in front of list
                        get_session_search.insert(0, search)
                        self.request.session['search_list'] = get_session_search

                    # set session as modified
                    self.request.session.modified = True

                else:
                    # set session
                    self.request.session['search_list'] = [search]

        return query


class ProjectDetails(DetailView):
    model = Project
    slug_field = 'project_id'
    template_name = 'project/project-details.html'
    context_object_name = 'project'

    def get_queryset(self):
        return Project.objects.filter(
            project_id=self.kwargs.get('slug'), publish=True, post_scheduling__lte=current_timestamp
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.order_by('-date_published').filter(
            publish=True,
            post_scheduling__lte=current_timestamp,
        )[:3]
        return context
