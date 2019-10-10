from django.db import models
from wagtail.core.models import Page

class HomePage(Page):
    class Meta:
        permissions = (
        ('view_restricted_document', 'can view restricted documents'),
    )
    

