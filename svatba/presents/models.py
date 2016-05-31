import datetime
import logging
from django.utils.timezone import now


from django.db import models
from svatba.utils import unique_slugify, send_email, EMAIL_TYPE_CHOICES_PRESENT

from .choices import GENERA, GENUS_M, GENUS_F, GENUS_N

logger = logging.getLogger(__name__)


class Present(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=300, verbose_name='Název')
    link = models.CharField(max_length=1000, verbose_name='Odkaz', null=True, blank=True)
    description = models.TextField(verbose_name='Popis', null=True, blank=True)
    price = models.IntegerField(verbose_name='Přibližná cena', null=True, blank=True)
    priority = models.PositiveSmallIntegerField(verbose_name='Priorita')
    unlimited = models.BooleanField(verbose_name='Příspěvek', help_text='může si ho vybrat víc lidí a nikdy se neškrtne',
                                    default=False)
    genus = models.PositiveSmallIntegerField(choices=GENERA, verbose_name='rod', default=GENUS_M)
    plural = models.BooleanField(default=False, verbose_name='plurál', help_text='nech nezaskrtnuto pro singular')
    created_at = models.DateTimeField(editable=False, default=now())
    modified_at = models.DateTimeField(default=now())
    always_taken = models.BooleanField(default=False, verbose_name='Vždy obsazen')

    class Meta:
        ordering = ["priority"]
        verbose_name_plural = 'Dary'
        verbose_name = 'Dar'

    @property
    def is_taken(self):
        if self.always_taken:
            return True
        elif self.unlimited:
            return False
        elif Person.objects.filter(present__id=self.pk):
            return True
        else:
            return False

    # is_taken.short_description = 'zabráno'
    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        """ On save, update timestamps """
        logger.info('trying to save Present', [args, kwargs])
        if not self.id:
            self.created_at = now()
        self.modified_at = now()
        return super(Present, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    @property
    def tento(self):
        if self.plural:
            if self.genus == GENUS_M:
                return 'tyto'
            if self.genus == GENUS_F:
                return 'tyto'
            if self.genus == GENUS_N:
                return 'tato'
        else:
            if self.genus == GENUS_M:
                return 'tento'
            if self.genus == GENUS_F:
                return 'tato'
            if self.genus == GENUS_N:
                return 'toto'



class Person(models.Model):
    present = models.ForeignKey(Present, null=False, verbose_name='dar')
    email = models.EmailField(null=False, verbose_name='email')
    removed = models.BooleanField(default=False, null=False, verbose_name='zruseno')
    created_at = models.DateTimeField(editable=False, default=datetime.datetime.today())
    modified_at = models.DateTimeField(default=datetime.datetime.today())

    def save(self, *args, **kwargs):
        logger.info('trying to save Person', [args, kwargs])
        """ On save, update timestamps """
        if not self.id:
            self.created_at = datetime.datetime.today()
            send_email(EMAIL_TYPE_CHOICES_PRESENT, recipient=self.email, present=self.present)
            logger.critical('SAVE NEW PERSON?')

        self.modified_at = datetime.datetime.today()
        return super(Person, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["email"]
        verbose_name_plural = 'Dárci'
        verbose_name = 'Dárce'

