from django.conf import settings

# Two factor name
ADMIN_TWO_FACTOR_NAME = getattr(settings, 'ADMIN_TWO_FACTOR_NAME', None)

# two factor session expire time (second)
SESSION_COOKIE_AGE = getattr(settings, 'SESSION_COOKIE_AGE', 300)

# Two factor context processors
settings.TEMPLATES[0]['OPTIONS']['context_processors'].append(
    'admin_two_factor.context_processors.two_factor.verification'
)
