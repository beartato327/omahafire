from wagtail.core import hooks
from django.contrib.auth.models import Permission

@hooks.register('register_permissions')
def view_restricted_page():
    return Permission.objects.filter(codename="view_restricted_document")