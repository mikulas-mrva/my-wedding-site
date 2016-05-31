import datetime
import logging

from django.db import models

from ..utils import send_email, EMAIL_TYPE_CHOICES_ATTENDING

logger = logging.getLogger(__name__)


class Visitor(models.Model):
    email = models.EmailField(null=False, verbose_name='Email')
    name = models.CharField(null=False, verbose_name='Jméno', max_length=100)
    attending = models.BooleanField(default=True, verbose_name='Přijdu')
    baker = models.BooleanField(default=False, verbose_name='Rád/a pomůžu s jídlem na party')
    vegan = models.BooleanField(default=False, verbose_name='Jsem vegan')
    vegetarian = models.BooleanField(default=False, verbose_name='Jsem vegetarian')
    gluten_free = models.BooleanField(default=False, verbose_name='Nemůžu lepek')

    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        logger.info('trying to save Visitor', [args, kwargs])
        """ On save, update timestamps """
        if not self.id:
            self.created_at = datetime.datetime.today()
            send_email(EMAIL_TYPE_CHOICES_ATTENDING, recipient=self.email, baker=self.baker)
        self.modified_at = datetime.datetime.today()
        return super(Visitor, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["email"]
        verbose_name_plural = 'Host'
        verbose_name = 'Hosté'
