import json
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.core.models import Page

from wagtail.core.fields import  StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.api.v2.serializers import PageSerializer
from base.models import BaseStreamBlock, HomeCtaSectionSerializer, ImageSerializedField
from rest_framework import serializers
from rest_framework.fields import Field


from wagtail.api import APIField


@register_snippet
class ServiceStep(models.Model):
    title = models.CharField('title', max_length=255)
    description = models.TextField('description', help_text="cta text")

    step_info_one = models.CharField('step_info_one', max_length=50, null=True, blank=True)
    step_info_two = models.CharField('step_info_two', max_length=255,null=True, blank=True)

    
    panels = [ 
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('step_info_one'),
        FieldPanel('step_info_two'),   
            
    ]

    

    def __str__(self) -> str:
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'service_step'
        verbose_name_plural = 'service_step_list'

class ServiceStepSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceStep
        fields = '__all__'

class ServicePage(Page):
    introduction = models.CharField('introduction', max_length=255)
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True
    )
    price = models.CharField(max_length=20)
    product_link = models.CharField(max_length=255)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )

    cta = models.ForeignKey('base.HomeCtaSection', blank=True, null=True, on_delete=models.SET_NULL)
    step_one = models.ForeignKey('service.ServiceStep',blank=True, null=True, on_delete=models.SET_NULL,related_name='step_one' )
    step_two = models.ForeignKey('service.ServiceStep', blank=True, null=True, on_delete=models.SET_NULL, related_name='step_two')
    step_three = models.ForeignKey('service.ServiceStep', blank=True, null=True, on_delete=models.SET_NULL, related_name='step_three')

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
        
        FieldPanel('price'),
        FieldPanel('product_link'),
        FieldPanel('cta'),
        FieldPanel('step_one'),
        FieldPanel('step_two'),
        FieldPanel('step_three')
  
    ]

    parent_page_types = ['ServiceIndexPage']

    api_fields = [
        #APIField('cta_1'),
        APIField('introduction'),
        APIField('body'),
        #APIField('heros'),  # this will nest the relevant BlogPageAuthor objects in the api response
        APIField('price'),
        APIField('product_link'),

        APIField('image', serializer=ImageSerializedField()),
        APIField('cta', serializer=HomeCtaSectionSerializer() ),
        APIField('step_one', serializer=ServiceStepSerializer()),
        APIField('step_two', serializer=ServiceStepSerializer()),
        APIField('step_three', serializer= ServiceStepSerializer())
    ]


class SerivePageChildrenSerializer(serializers.ModelSerializer):
    image= ImageSerializedField()
    class Meta:
        model=ServicePage
        fields= '__all__'

    # def to_representation(self, childpages):
    #     return [ json.dumps(child) 
    #     for child in  childpages]

# class SerivePageChildrenSerializer(Field):

#     def to_representation(self, childpages):
#         return [ {'id': child.id , 
#         'body': child.body, 
#         'url': child.detail_url , 
#         'img': child.} for child in  childpages]

class ServiceIndexPage(Page):
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and '
        '3000px.'
    )

    home_msg = models.CharField(max_length=255,null=True, blank=True)
    home_msg_sub = models.CharField(max_length=255,null=True, blank=True)

    cta = models.ForeignKey('base.HomeCtaSection', blank=True, null=True, on_delete=models.SET_NULL)
    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        FieldPanel('cta'),
        FieldPanel('home_msg'),
        FieldPanel('home_msg_sub'),
        ImageChooserPanel('image'),
    ]

    # Can only have BreadPage children
    subpage_types = ['ServicePage']


    api_fields = [
        #APIField('cta_1'),
        APIField('introduction'),
        APIField('image', serializer=ImageSerializedField()),
        APIField('home_msg'),
        APIField('home_msg_sub'),
        #APIField('heros'),  # this will nest the relevant BlogPageAuthor objects in the api response
        APIField('get_children_api', serializer=SerivePageChildrenSerializer(many=True) ),
    ]

    # Returns a queryset of BreadPage objects that are live, that are direct
    # descendants of this index page with most recent first
    def get_services(self):
        return ServicePage.objects.live().descendant_of(
            self).order_by('-first_published_at')

    # Allows child objects (e.g. BreadPage objects) to be accessible via the
    # template. We use this on the HomePage to display child items of featured
    # content
    @property
    def get_children_api(self):
        return self.get_children().specific().live()


    def children(self):
        return self.get_children().specific().live()

    # Pagination for the index page. We use the `django.core.paginator` as any
    # standard Django app would, but the difference here being we have it as a
    # method on the model rather than within a view function
    def paginate(self, request, *args):
        page = request.GET.get('page')
        paginator = Paginator(self.get_services(), 12)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    # Returns the above to the get_context method that is used to populate the
    # template
    def get_context(self, request):
        context = super(ServiceIndexPage, self).get_context(request)

        # BreadPage objects (get_breads) are passed through pagination
        services = self.paginate(request, self.get_services())

        context['services'] = services

        return context
