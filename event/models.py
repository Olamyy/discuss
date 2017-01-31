from django.db import models
from django.utils import timezone


class Attendee(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    mobile_number = models.CharField(max_length=11, blank=False)
    attendance = models.CharField(max_length=100, blank=False)
    date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return ''.format(self.email, self.firstname, self.lastname)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Sponsor(models.Model):
    sponsor_name = models.CharField(max_length=400, blank=True)
    sponsor_email = models.EmailField(max_length=100, blank=False)
    sponsor_image = models.ImageField(upload_to='sponsors/')

    def __unicode__(self):
        return ''.format(self.sponsor_email, self.sponsor_name)

    def __str__(self):
        return '{}'.format(self.sponsor_name)


class Contact(models.Model):
    message = models.CharField(max_length=500, blank=False)
    email = models.EmailField(max_length=100, blank=False)

    def __unicode__(self):
        return ''.format(self.message, self.email)

    def __str__(self):
        return '{}'.format(self.email)


class NewsletterContact(models.Model):
    email = models.EmailField(max_length=500, blank=False)

    def __unicode__(self):
        return ''.format(self.email)

    def __str__(self):
        return '{}'.format(self.email)



