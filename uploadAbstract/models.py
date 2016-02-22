from __future__ import unicode_literals
from django.db import models
from DISS.email_functionality import email_admin, email_client

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class SubmittedAbstract(models.Model):
    salutation = models.CharField(max_length=6)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=60, unique=True)
    paper_title = models.CharField(max_length=60)
    abstract = models.CharField(max_length=2000)

    def save(self, *args, **kwargs):

        sorted_self = [["Salutation", self.salutation], ["First name", self.first_name], ["Last Name", self.last_name],
                       ["Email", self.email], ["Paper Title", self.paper_title], ["Abstract", self.abstract],
                       ]

        email_client(self, "DISS 2017 Abstract Upload", "You have uploaded an abstract.")
        email_admin(self, "New DISS 2017 Abstract", "Please find enclosed the details for the new DISS "
                                                    "2017 abstract upload.", sorted_self)

    def __unicode__(self):
        return self.email
