from django.templatetags.static import static
from django.utils.translation import gettext_lazy as _

from core.project.settings import ENV

# init admin path
admin_path = ENV.config('ADMIN_PATH')


UNFOLD = {
    'SITE_TITLE': 'CCPFEWS',
    'SITE_HEADER': 'CCPFEWS',
    'SITE_URL': '/',
    # 'SITE_ICON': lambda request: static('assets/img/favicon.png'),  # both modes, optimize for 32px height
    'SITE_ICON': {
        'light': lambda request: static('assets/favicon/favicon.ico'),  # light mode
        'dark': lambda request: static('assets/favicon/favicon.ico'),  # dark mode
    },
    # 'SITE_LOGO': lambda request: static('logo.svg'),  # both modes, optimize for 32px height
    'SITE_LOGO': {
        'light': lambda request: static('assets/img/logo.jpg'),  # light mode
        'dark': lambda request: static('assets/img/logo.jpg'),  # dark mode
    },
    'SITE_SYMBOL': 'speed',  # symbol from icon set
    'SHOW_HISTORY': True,  # show/hide 'History' button, default: True
    'SHOW_VIEW_ON_SITE': True,  # show/hide 'View on site' button, default: True
    'ENVIRONMENT': 'core.project.settings.unfold.env.environment_callback',
    'DASHBOARD_CALLBACK': 'core.project.settings.unfold.context.dashboard_callback',
    'LOGIN': {
        'image': lambda request: static('assets/img/login-bg.jpg'),
        # 'redirect_after': lambda request: reverse_lazy('admin:APP_MODEL_changelist'),
    },
    'STYLES': [
        lambda request: static('assets/css/unfold/style.css'),
    ],
    # 'SCRIPTS': [
    #     lambda request: static('assets/js/unfold/script.js'),
    # ],
    'COLORS': {
        'primary': {
            '50': '250 245 255',
            '100': '243 232 255',
            '200': '233 213 255',
            '300': '216 180 254',
            '400': '192 132 252',
            '500': '168 85 247',
            '600': '147 51 234',
            '700': '126 34 206',
            '800': '107 33 168',
            '900': '88 28 135',
            '950': '59 7 100',
        },
    },

    'SIDEBAR': {
        'show_search': True,  # Search in applications and models names
        'show_all_applications': True,  # Dropdown with all applications and models
        'navigation': [
            {
                'title': _('Navigation'),
                'separator': True,  # Top border
                'items': [
                    {
                        'title': _('Dashboard'),
                        'icon': 'dashboard',  # Supported icon set: https://fonts.google.com/icons
                        'link': lambda request: f'/{admin_path}/',  # noqa: E501
                        'permission': lambda request: request.user.is_superuser,  # noqa: E501
                    },
                ],
            },
            {
                'title': _('Security'),
                'separator': True,  # Top border
                'items': [
                    {
                        'title': _('Access Attempts'),
                        'icon': 'running_with_errors',  # Supported icon set: https://fonts.google.com/icons
                        'link': lambda request: f'/{admin_path}/defender/accessattempt/',
                        'permission': lambda request: request.user.is_superuser,
                    },
                ],
            },
            {
                'separator': True,  # Top border
                'items': [

                    {
                        'title': _('Users'),
                        'icon': 'badge',
                        'link': lambda request: f'/{admin_path}/users/user/',
                        'permission': lambda request: request.user.is_superuser,
                    },
                    {
                        'title': _('Groups'),
                        'icon': 'groups',
                        'link': lambda request: f'/{admin_path}/auth/group/',
                        'permission': lambda request: request.user.is_superuser,
                    },
                    {
                        'title': _('Site Info'),
                        'icon': 'dns',
                        'link': lambda request: f'/{admin_path}/sites/site/',
                        'permission': lambda request: request.user.is_superuser,
                    },
                ],
            },
            {
                'separator': True,  # Top border
                'items': [

                    {
                        'title': _('Contact Messages'),
                        'icon': 'support',
                        'link': lambda request: f'/{admin_path}/contacts/contact/',
                        'permission': lambda request: request.user.is_superuser,
                    },
                    {
                        'title': _('Consultation'),
                        'icon': 'headset_mic',
                        'link': lambda request: f'/{admin_path}/contacts/consultation/',
                        'permission': lambda request: request.user.is_superuser,
                    },
                    {
                        'title': _('Team'),
                        'icon': 'perm_contact_calendar',
                        'link': lambda request: f'/{admin_path}/profiles/profile/',
                        'permission': lambda request: request.user.is_superuser,
                    },
                    {
                        'title': _('Blog'),
                        'icon': 'post_add',
                        'link': lambda request: f'/{admin_path}/blog/blog/',
                        'permission': lambda request: request.user.is_superuser,
                    },
                    {
                        'title': _('Events'),
                        'icon': 'map',
                        'link': lambda request: f'/{admin_path}/events/event/',
                        'permission': lambda request: request.user.is_superuser,
                    },
                    {
                        'title': _('Projects'),
                        'icon': 'biotech',
                        'link': lambda request: f'/{admin_path}/research/project/',
                        'permission': lambda request: request.user.is_superuser,
                    },
                ],
            },
        ],
    },
}
