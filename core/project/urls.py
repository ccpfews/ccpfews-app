from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(f'{settings.ADMIN_PATH}/', admin.site.urls),
    path('blog/', include('core.blog.urls')),
    path('contact/', include('core.contacts.urls')),
    path('events/', include('core.events.urls')),
    path('research/', include('core.research.urls')),
    path('team/', include('core.profiles.urls')),
    path('', include('core.pages.urls')),
]

# add admin path to urlpatterns
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Overrides the default 400 handler django.views.defaults.bad_request
handler400 = 'core.project.settings.utils.views.bad_request'
# Overrides the default 403 handler django.views.defaults.permission_denied
handler403 = 'core.project.settings.utils.views.permission_denied'
# Overrides the default 404 handler django.views.defaults.page_not_found
handler404 = 'core.project.settings.utils.views.page_not_found'
# Overrides the default 500 handler django.views.defaults.server_error
handler500 = 'core.project.settings.utils.views.server_error'
