from django.db import models

from wagtail.core.models import Page

from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import FieldPanel


class AboutPage(Page):
    max_count = 1
    body  = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    class Meta:
        verbose_name = "About Page"