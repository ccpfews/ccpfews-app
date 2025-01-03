import pendulum
from django.db.models import F
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from core.blog.models.blogs import Blog
from core.events.models.events import Event

# set current time
current_timestamp = pendulum.now()


class BlogPost(ListView):
    model = Blog
    queryset = Blog.objects.all()
    template_name = 'blog/blog.html'
    context_object_name = 'blog'
    paginate_by = 10

    def get_queryset(self):
        # return queryset
        return Blog.objects.filter(publish=True, schedule_publish__lte=current_timestamp)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.order_by('-date_published').all()[:3]
        return context


class BlogDetails(DetailView):
    model = Blog
    queryset = Blog.objects.all()

    slug_field = 'post_id'
    template_name = 'blog/blog-details.html'
    context_object_name = 'blog'

    def get_queryset(self):
        # get id
        post_id = self.kwargs.get('slug')

        # Use a querySet to perform the update
        queryset = self.model.objects.filter(post_id=post_id, publish=True, schedule_publish__lte=current_timestamp)

        if not queryset.exists():
            raise Http404()

        # increase views_count update
        queryset.update(views_count=F('views_count') + 1)

        # return updated queryset
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.order_by('-date_published').all()[:3]
        return context
