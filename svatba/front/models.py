import logging

from django.db import models

from ..utils import send_email, EMAIL_TYPE_CHOICES_MESSAGE

logger = logging.getLogger(__name__)

class Message(models.Model):
    sender = models.EmailField(verbose_name='váš e-mail')
    message = models.TextField(verbose_name='zpráva', max_length=1000)

    class Meta:
        verbose_name_plural = 'Zprávy'
        verbose_name = 'Zpráva'

    def save(self, *args, **kwargs):
        logger.info('trying to save Message', *args, **kwargs)

        logger.error('testovaci error')

        send_email(EMAIL_TYPE_CHOICES_MESSAGE, sender=self.sender, message=self.message)

        return super(Message, self).save(*args, **kwargs)
