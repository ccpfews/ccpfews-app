import pendulum
from django import template
from django.db.models import Count
from django.db.models.functions import ExtractHour
from django.utils import timezone
from django.utils.timezone import timedelta

from core.blog.models.blogs import Blog
from core.contacts.models import Consultation, Contact

# init register
register = template.Library()

# get the current time
current_timestamp = pendulum.now('Africa/Johannesburg')

# days computations in local johannesburg time
# each count include current day
previous_27_days_from_today = timezone.localtime(current_timestamp - timedelta(days=27))


@register.filter(name='blog_views_chart')
def blog_views_chart(value='Undergrad'):
    # aggregate counts per hour
    hourly_counts = (
        Blog.objects.select_related('author').annotate(hour=ExtractHour('date_published',)
                                                       ).values('hour',).annotate(count=Count('post_id')
                                                                                  ).order_by('date_published',)
    )

    # init holding list
    holding_post_list = [[1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1,
                                                                                                          0], [1, 0],
                         [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0],
                         [1, 0]]

    # init holding list
    for entry in hourly_counts:
        holding_post_list[entry['hour']][1] = entry['count']

    return holding_post_list


@register.filter(name='consultation_unread_message_chart')
def consultation_unread_message_chart(value):
    # aggregate counts per hour
    hourly_counts = (
        Consultation.objects.filter(has_read=False).annotate(hour=ExtractHour('date_received')
                                                             ).values('hour').annotate(count=Count('consult_email')
                                                                                       ).order_by('date_received')
    )

    # init holding list
    holding_consult_list = [[-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0],
                            [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0],
                            [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0]]

    for entry in hourly_counts:
        holding_consult_list[entry['hour']][1] = -entry['count']

    # return updated list
    return holding_consult_list


@register.filter(name='contact_unread_message_chart')
def contact_unread_message_chart(value):
    # aggregate counts per hour
    hourly_counts = (
        Contact.objects.filter(has_read=False).annotate(hour=ExtractHour('date_received')
                                                        ).values('hour').annotate(count=Count('email')
                                                                                  ).order_by('date_received')
    )

    # init holding list
    holding_contact_list = [[-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0],
                            [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0],
                            [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0], [-1, -0]]

    for entry in hourly_counts:
        holding_contact_list[entry['hour']][1] = -entry['count']

    # return updated list
    return holding_contact_list
