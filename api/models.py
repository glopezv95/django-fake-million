from django.db import models
from django.utils.translation import gettext as _

class Client(models.Model):

    name = models.CharField(_("Name"), max_length=50)
    last_name = models.CharField(_("Lastname"), max_length=50)
    gender = models.CharField(_("Gender"), max_length=50)
    phone_number = models.BigIntegerField(_("Phone Number"))
    job = models.CharField(_("Job"), max_length=100)
    studies = models.CharField(_("Studies"), max_length=50)
    country = models.CharField(_("Country"), max_length=100)
    birth_date = models.DateField(_("Birth Date"), auto_now=False, auto_now_add=False)
    salary = models.FloatField(_("Salary"))
    age = models.IntegerField(_("Age"))
    date_added = models.DateField(_("Date Added"), auto_now=True, auto_now_add=False)
    date_created = models.DateField(_("Date Created"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

    def __str__(self):
        return self.name