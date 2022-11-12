from __future__ import unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from rest_framework.fields import Field
from rest_framework import serializers

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Collection, Page, Orderable
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from wagtail.api import APIField

from .blocks import BaseStreamBlock

# from .serializers import PeopleSerializer, HomeHeroSerializer, HomeCtaOneSerializer


@register_snippet
class People(index.Indexed, ClusterableModel):
    """
    A Django model to store People objects.
    It uses the `@register_snippet` decorator to allow it to be accessible
    via the Snippets UI (e.g. /admin/snippets/base/people/)

    `People` uses the `ClusterableModel`, which allows the relationship with
    another model to be stored locally to the 'parent' model (e.g. a PageModel)
    until the parent is explicitly saved. This allows the editor to use the
    'Preview' button, to preview the content, without saving the relationships
    to the database.
    https://github.com/wagtail/django-modelcluster
    """
    first_name = models.CharField("First name", max_length=254)
    last_name = models.CharField("Last name", max_length=254)
    job_title = models.CharField("Job title", max_length=254)
    testimony = models.TextField("testimony",  help_text="testimony message" ) 

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('first_name', classname="col6"),
                FieldPanel('last_name', classname="col6"),
            ])
        ], "Name"),
        FieldPanel('job_title'),
        FieldPanel('testimony'),
        ImageChooserPanel('image')
    ]

    search_fields = [
        index.SearchField('first_name'),
        index.SearchField('last_name'),
    ]

    api_fields =  [
        APIField('first_name'),
        APIField('last_name'),
        APIField('testimony'),
        APIField('job_title')
    ]

    @property
    def thumb_image(self):
        # Returns an empty string if there is no profile pic or the rendition
        # file can't be found.
        try:
            return self.image.get_rendition('fill-50x50').img_tag()
        except:  # noqa: E722 FIXME: remove bare 'except:'
            return ''

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

DISPLAY_STYLE_CHOICES = (
    ('LEFT', 'img left'),
    ('CENT', 'img center'),
    ('RIGH', 'img right'),
    ('FORM', 'form in'),

)




@register_snippet
class HeroSection(index.Indexed, ClusterableModel):
    title  = models.CharField("title", max_length=254)
    description = models.TextField("description", help_text="description of hero")
    background_img = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    display_style = models.CharField(choices=DISPLAY_STYLE_CHOICES, default='RIGH', max_length=5)
    button_action = models.ForeignKey( 
                                        'wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',
                                        verbose_name='Hero CTA link',
                                        help_text='Choose a page to link to for the Call to Action',)
    button_one_text = models.CharField('button_one_text', max_length=50, null=True, blank=True)
    button_one_link = models.CharField('button_one_link', max_length=255, null=True, blank=True )
    button_two_text = models.CharField('button_two_text', max_length=50, null=True, blank=True)
    button_two_link = models.CharField('button_two_link', max_length=255, null=True, blank=True )


    panels = [ 
        FieldPanel('title'),
        FieldPanel('description'),
        ImageChooserPanel('background_img'),
        FieldPanel('display_style'),
        FieldPanel('button_one_text'),
        FieldPanel('button_one_link'),
        FieldPanel('button_two_text'),
        FieldPanel('button_two_link'),
    
        PageChooserPanel('button_action'),
            
    ]

    api_fields = [
        APIField('title'),
        APIField('description'),
        APIField('display_style')
    ]

    def __str__(self) -> str:
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Hero'
        verbose_name_plural = 'Hero_list'




@register_snippet
class HomeCtaSection(models.Model):
    title = models.CharField('title', max_length=255)
    description = models.TextField('description', help_text="cta text")
    section_img = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    background_img = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    display_style = models.CharField(choices=DISPLAY_STYLE_CHOICES, default='RIGH', max_length=5)
    button_action = models.ForeignKey( 
                                        'wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+',
                                        verbose_name='Hero CTA link',
                                        help_text='Choose a page to link to for the Call to Action',)
    button_text = models.CharField('button_text', max_length=50, null=True, blank=True)
    button_link = models.CharField('button_link', max_length=255,null=True, blank=True)

    panels = [ 
        FieldPanel('title'),
        FieldPanel('description'),
        ImageChooserPanel('section_img'),
        FieldPanel('display_style'),
        FieldPanel('button_text'),
        FieldPanel('button_link'),   
        PageChooserPanel('button_action'),
            
    ]

    def __str__(self) -> str:
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'home_cta'
        verbose_name_plural = 'home_cta_list'


@register_snippet
class WorkedWithSection(models.Model):
    title = models.CharField('title', max_length=255)
    section_img_1 = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    section_img_2 = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    section_img_3 = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    section_img_4 = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    section_img_5 = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    section_img_6 = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [ 
        FieldPanel('title'),
        ImageChooserPanel('section_img_1'),
        ImageChooserPanel('section_img_2'),
        ImageChooserPanel('section_img_3'),
        ImageChooserPanel('section_img_4'),
        ImageChooserPanel('section_img_5'),
        ImageChooserPanel('section_img_6'),
    ]

    def __str__(self) -> str:
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'worked_with'
        verbose_name_plural = 'worked_with_list'



@register_snippet
class FooterText(models.Model):
    """
    This provides editable text for the site footer. Again it uses the decorator
    `register_snippet` to allow it to be accessible via the admin. It is made
    accessible on the template via a template tag defined in base/templatetags/
    navigation_tags.py
    """
    body = RichTextField()

    panels = [
        FieldPanel('body'),
    ]

    def __str__(self):
        return "Footer text"

    class Meta:
        verbose_name_plural = 'Footer Text'




    


class HomeHeroRelationship(Orderable, models.Model):
    page = ParentalKey('HomePage', related_name= 'home_hero_relationship', on_delete=models.CASCADE)
    hero = models.ForeignKey('base.HeroSection', related_name='hero_home_relationship', on_delete=models.CASCADE)

    panels = [
        SnippetChooserPanel('hero')
    ]

class HomePeopleRelationship(Orderable, models.Model):
    page = ParentalKey('HomePage', related_name= 'home_people_relationship', on_delete=models.CASCADE)
    testimony = models.ForeignKey('base.People', related_name='people_home_relationship', on_delete=models.CASCADE)
    
    panels = [
            SnippetChooserPanel('testimony')
        ]
    
    api_fields = [
        APIField('page'),
        APIField('testimony')
    ]

class HomeCtaOneRelationship(Orderable, models.Model):
    page = ParentalKey('HomePage', related_name = 'home_cta_one_relationship', on_delete=models.CASCADE)
    cta_one = models.ForeignKey('base.HomeCtaSection', related_name='cta_one_home_relationship', on_delete=models.CASCADE)

    panels = [
        SnippetChooserPanel('cta_one')
    ]



class ImageSerializedField(Field):
    """A custom serializer used in Wagtails v2 API."""

    def to_representation(self, value):
        """Return the image URL, title and dimensions."""
        return {
            "url": value.file.url,
            "title": value.title,
            "width": value.width,
            "height": value.height,
        }


class HerosectionOneSerializer(serializers.ModelSerializer):

    background_img = ImageSerializedField()
    class Meta:
        model = HeroSection
        fields = '__all__'

class PeopleOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'

class HomeHeroSerializer(serializers.ModelSerializer):
    hero = HerosectionOneSerializer()
    class Meta:
        model = HomeHeroRelationship
        fields = '__all__'



class HomeCtaSectionSerializer(serializers.ModelSerializer):
    section_img = ImageSerializedField()
    class Meta:
        model = HomeCtaSection
        fields = '__all__'



class HomeCtaOneSerializer(serializers.ModelSerializer):
    cta_one = HomeCtaSectionSerializer()
    class Meta:
        model = HomeCtaOneRelationship
        fields = '__all__'



class PeopleSerializer(serializers.ModelSerializer):
    testimony = PeopleOneSerializer()
    class Meta:
        model = HomePeopleRelationship
        fields = '__all__'


class StandardPage(Page):
    """
    A generic content page. On this demo site we use it for an about page but
    it could be used for any type of page content that only needs a title,
    image, introduction and body field
    """

    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True
    )
    cta = models.ForeignKey('base.HomeCtaSection', blank=True, null=True, on_delete=models.SET_NULL, related_name='standard_cta')

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        StreamFieldPanel('body'),
        ImageChooserPanel('image'),
        FieldPanel('cta')
    ]

    api_fields = [
        APIField('introduction'),
        APIField('body'),
        APIField('cta', serializer=HomeCtaSectionSerializer() ),
        APIField('image',serializer=ImageSerializedField())
    ]


class HomePage(Page):
    """
    The Home Page. This looks slightly more complicated than it is. You can
    see if you visit your site and edit the homepage that it is split between
    a:
    - Hero area
    - Body area
    - A promotional area
    - Moveable featured site sections
    """

    #mine start
    

    # Body section of the HomePage
    #cta_1 = models.ForeignKey('base.HomeCtaSection', null=True, blank=True,on_delete=models.SET_NULL, related_name='+')
    body = StreamField(
        BaseStreamBlock(), verbose_name="Home content block", blank=True
    )
    worked_with = models.ForeignKey('base.WorkedWithSection', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    cta_2 = models.ForeignKey('base.HomeCtaSection', null=True, blank=True,on_delete=models.SET_NULL, related_name='+')
    content_panels = Page.content_panels + [
        
        StreamFieldPanel('body'),
        InlinePanel('home_hero_relationship', label="Hero(s)", panels=None, min_num=1),
        InlinePanel('home_people_relationship', label="Testimony(s)", panels=None, min_num=1),
        InlinePanel('home_cta_one_relationship', label="Cta_one", panels=None ),
        #FieldPanel('cta_1'),
        FieldPanel('worked_with'),
        FieldPanel('cta_2'),

        ]

    api_fields = [
        #APIField('cta_1'),
        APIField('body'),
        APIField('worked_with'),
        #APIField('heros'),  # this will nest the relevant BlogPageAuthor objects in the api response
        APIField('home_people_relationship', serializer= PeopleSerializer(many=True)),
        APIField('home_hero_relationship', serializer=HomeHeroSerializer(many=True)),
        APIField('home_cta_one_relationship', serializer=HomeCtaOneSerializer(many=True) )
    ]

    def __str__(self):
        return self.title

    def heros(self):

        heros = [ n.hero for n in self.home_hero_relationship.all()]

        return heros

        
    def people(self):
        people = [n.people for n in self.home_people_relationship.all()]

        return people
    def cta_one(self):

        cta_one = [n.cta_one for n in self.home_cta_one_relationship.all()]
        return cta_one
    



# class GalleryPage(Page):
#     """
#     This is a page to list locations from the selected Collection. We use a Q
#     object to list any Collection created (/admin/collections/) even if they
#     contain no items. In this demo we use it for a GalleryPage,
#     and is intended to show the extensibility of this aspect of Wagtail
#     """

#     introduction = models.TextField(
#         help_text='Text to describe the page',
#         blank=True)
#     image = models.ForeignKey(
#         'wagtailimages.Image',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+',
#         help_text='Landscape mode only; horizontal width between 1000px and '
#         '3000px.'
#     )
#     body = StreamField(
#         BaseStreamBlock(), verbose_name="Page body", blank=True
#     )
#     collection = models.ForeignKey(
#         Collection,
#         limit_choices_to=~models.Q(name__in=['Root']),
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         help_text='Select the image collection for this gallery.'
#     )

#     content_panels = Page.content_panels + [
#         FieldPanel('introduction', classname="full"),
#         StreamFieldPanel('body'),
#         ImageChooserPanel('image'),
#         FieldPanel('collection'),
#     ]

#     # Defining what content type can sit under the parent. Since it's a blank
#     # array no subpage can be added
#     subpage_types = []


class FormField(AbstractFormField):
    """
    Wagtailforms is a module to introduce simple forms on a Wagtail site. It
    isn't intended as a replacement to Django's form support but as a quick way
    to generate a general purpose data-collection form or contact form
    without having to write code. We use it on the site for a contact form. You
    can read more about Wagtail forms at:
    https://docs.wagtail.org/en/stable/reference/contrib/forms/index.html
    """
    page = ParentalKey('FormPage', related_name='form_fields', on_delete=models.CASCADE)


class FormPage(AbstractEmailForm):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField(BaseStreamBlock())
    thank_you_text = RichTextField(blank=True)

    # Note how we include the FormField object via an InlinePanel using the
    # related_name value
    content_panels = AbstractEmailForm.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]


