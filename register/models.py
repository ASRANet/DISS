from __future__ import unicode_literals
from django.db import models
from DISS.email_functionality import email_admin, email_client

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class User(models.Model):
    salutation = models.CharField(max_length=6)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    organisation = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=60)
    telephone = models.CharField(max_length=15)
    email = models.EmailField(max_length=60, unique=True)
    fee_normal = models.BooleanField(default=False)
    fee_student = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        sorted_self = [["Paying Student Fee", self.fee_student], ["Paying Normal Fee", self.fee_normal],
                       ["Email", self.email], ["Telephone", self.telephone], ["Country", self.country],
                       ["Postcode", self.postcode], ["City", self.city], ["Address", self.address],
                       ["Organisation", self.organisation], ["Last Name", self.last_name],
                       ["First name", self.first_name], ["Salutation", self.salutation],
                       ]

        email_client(self, "DISS 2017 Conference Registration", "You are officially registered for DISS 2017")
        email_admin(self, "New DISS 2017 Registrant", "Please find enclosed the details for the new DISS "
                                                      "2017 registrant.", sorted_self)

    def __unicode__(self):
        return self.email
