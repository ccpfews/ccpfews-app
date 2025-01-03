import pendulum
from django.conf import settings

from core.blog.models.blogs import Blog
from core.contacts.models import Consultation, Contact
from core.events.models.events import Event
from core.profiles.models.profiles import Profile
from core.research.models.projects import Project

# set current time
current_timestamp = pendulum.now()


def dashboard_callback(request, context):
    """
    Callback to prepare custom variables for index template which is used as dashboard
    template. It can be overridden in application by creating custom admin/index.html.
    """
    context.update({
        'admin_path': settings.ADMIN_PATH,
        'ongoing_project_counter': Project.objects.select_related('author').filter(status='On-going').count(),
        'contact_unread_counter': Contact.objects.filter(has_read=False).count(),
        'contact_counter': Contact.objects.all().count(),
        'consult_unread_counter': Consultation.objects.filter(has_read=False).count(),
        'post_views_counter': Blog.objects.select_related('author').all().count(),
        'event_counter': Event.objects.all().count(),
        'event_counter_year': Event.objects.filter(date_published__year=current_timestamp.year).count(),
        'team_counter': Profile.objects.all().count(),
        'project_counter': Project.objects.all().count(),
    },)

    return context
