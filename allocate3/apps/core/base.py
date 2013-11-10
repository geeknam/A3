from django.db import models
from django.template.defaultfilters import slugify
from django_countries import CountryField
import functools


SlugField = functools.partial(
    models.SlugField,
    max_length=255,
    db_index=True
)
PriceField = functools.partial(
    models.DecimalField,
    decimal_places=2,
    max_digits=10,
    default=0.00
)

class AddressMixin(models.Model):
    address_1 = models.CharField(max_length=300, null=True, blank=True)
    address_2 = models.CharField(max_length=300, null=True, blank=True)
    suburb = models.CharField(max_length=300, null=True, blank=True)
    state = models.CharField(max_length=300, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    phone = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        abstract = True

class BaseSlugMixin(object):
    """
    SlugMixin typically depends on TitleMixin to
    create slugs from.  If title is not available
    Name will be attempted.
    """

    @property
    def get_slug_text(self):
        """ Return the title or name to use for slugs """
        try:
            slug_raw = getattr(self, 'title', None)
            if not slug_raw:
                slug_raw = self.name
            return slugify(slug_raw)
        except AttributeError:
            #TODO what is this exception "depression" all about?
            # raise Exception("title or name field required for SlugMixin")
            pass

    def set_auto_indexed_slug(self):
        """
            Look for a vacant slug that has a unique index appended
            and assign it.
        """
        model = self.__class__
        slug = slug_org = self.get_slug_text
        index = 0
        while model.objects.filter(slug=slug).exists():
            index += 1
            slug = slug_org + '-' + str(index)
        self.slug = slug


    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = self.get_slug_text
        super(BaseSlugMixin, self).save(*args, **kwargs)


class SlugMixin(BaseSlugMixin, models.Model):

    slug = SlugField()

    class Meta:
        abstract = True


class SlugUniqueMixin(BaseSlugMixin, models.Model):

    slug = SlugField(unique=True)

    class Meta:
        abstract = True