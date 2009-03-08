from django.db import models
from django.utils.translation import ugettext_lazy as _

from datetime import datetime

class Memory(models.Model):
    size = models.CharField(_('size'), max_length=16)

    class Meta:
        ordering = ('id',)
        verbose_name = _('memory')
        verbose_name_plural = _('memory')

    def __unicode__(self):
        return self.size

class HardDisk(models.Model):
    size = models.CharField(_('size'), max_length=16)

    class Meta:
        ordering = ('id',)
        verbose_name = _('hard disk')
        verbose_name_plural = _('hard disk')

    def __unicode__(self):
        return self.size

class Processor(models.Model):
    name = models.CharField(_('name'), max_length=16)

    class Meta:
        ordering = ('id',)
        verbose_name = _('processor')
        verbose_name_plural = ('processor')

    def __unicode__(self):
        return self.name

class Software(models.Model):
    software = models.CharField(_('software'), max_length=64)
    version = models.CharField(_('version'), max_length=16)

    class Meta:
        ordering = ('software', 'version')
        verbose_name = _('software')
        verbose_name_plural = _('software')

    def __unicode__(self):
        return '%s %s ' % (self.software, self.version)

class Event(models.Model):
    name = models.CharField(_('name'), max_length=32, unique=True)
    slug = models.SlugField(_('slug'), max_length=32)
    description = models.TextField(_('description'))
    scheduled = models.DateField(_('date scheduled'))

    class Meta:
        ordering = ('-scheduled', 'name',)
        verbose_name = _('event')
        verbose_name_plural = _('events')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('event-detail', [self.slug])

    @property
    def is_past(self):
        return datetime.now()>self.scheduled

class Site(models.Model):
    event = models.ForeignKey(Event, related_name='sites',
        verbose_name=_('event'))
    software = models.ManyToManyField(Software)
    name = models.CharField(_('name'), max_length=32)
    slug = models.SlugField(_('slug'), max_length=32)
    description = models.TextField(_('description'))
    max_capacity = models.IntegerField(_('max. capacity'), default=0)
    scheduled = models.DateTimeField(_('date scheduled'))
    finished = models.TimeField(_('time finished'))

    class Meta:
        ordering = ('name',)
        verbose_name = _('site')
        verbose_name_plural = _('sites')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('site-detail', None,
            {'event_slug': self.event.slug, 'site_slug': self.slug})

    @property
    def is_full(self):
        if self.max_capacity==0:
            return False
        
        return self.registrant_set.count()>=self.max_capacity

    @property
    def is_past(self):
        return datetime.now()>self.scheduled

class Registrant(models.Model):
    event = models.ForeignKey(Event, related_name='registrants',
        verbose_name=_('event'))
    site = models.ForeignKey(Site, related_name='registrants',
        verbose_name=_('site'))

    first_name = models.CharField(_('first name'), max_length=32)
    last_name = models.CharField(_('last name'), max_length=32)
    email = models.EmailField(_('e-mail'))
    telephone = models.CharField(_('telephone'), max_length=16)

    processor = models.ForeignKey(Processor, verbose_name=_('processor'))
    memory = models.ForeignKey(Memory, verbose_name=_('memory'))
    hard_disk = models.ForeignKey(HardDisk, verbose_name=_('hard disk'))
    software = models.ForeignKey(Software, related_name='registrants',
        verbose_name=_('software'))

    terms_accepted = models.BooleanField(_('terms accepted'))
    
    registered = models.DateTimeField(_('date registered'), editable=False, 
        default=datetime.now)
    scheduled = models.DateTimeField(_('date scheduled'), blank=True, null=True)

    class Meta:
        ordering = ('last_name', 'first_name',)
        verbose_name = _('registrant')
        verbose_name_plural = _('registrants')

    def __unicode__(self):
        return '%s, %s' % (self.last_name, self.first_name)
