from django import template

register = template.Library()

@register.filter
def get_session_value(session, key):
    return session.get(key, False)
    