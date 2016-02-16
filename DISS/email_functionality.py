from __future__ import unicode_literals
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import os
from email.mime.image import MIMEImage
from reportlab.pdfgen import canvas
from django.http import HttpResponse

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


def email_client(self, subject, text):
    # Send the client an email
    html_content = render_to_string("../templates/baseTemplates/emailToUser.html", {'salutation': self.salutation,
                                                                                    'last_name': self.last_name,
                                                                                    'text_body': text})
    msg = EmailMultiAlternatives(subject, 'Dear ' + self.salutation + ' ' +
                                 self.last_name + '/n' + text,
                                 'diss@asranet.co.uk', [self.email], )
    msg.attach_alternative(html_content, "text/html")
    msg.attach_file('static/Images/asranetLogo.jpg')
    msg.mixed_subtype = 'related'

    f = 'asranetLogo.jpg'
    fp = open(os.path.join(os.path.dirname(__file__), f), 'rb')
    msg_img = MIMEImage(fp.read())
    fp.close()
    msg_img.add_header('Content-ID', '<{}>'.format(f))
    msg.attach(msg_img)
    msg.send()


def email_admin(self, subject, text, sorted_self):
    # Send the admin a PDF of client details
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="clientDetails.pdf"'

    string_buffer = StringIO()

    y = 50
    new_canvas = canvas.Canvas(string_buffer)

    for value in sorted_self:
        y += 50
        new_canvas.drawString(100, y, value[0] + ": " + str(value[1]))
        print value[0] + ": " + str(value[1])
        new_canvas.

    y += 50
    new_canvas.drawString(50, y, "DISS Attendee Details")

    new_canvas.showPage()
    new_canvas.save()

    pdf = string_buffer.getvalue()
    string_buffer.close()

    msg = EmailMultiAlternatives(subject, text, "diss@asranet.co.uk", ["blair.calderwood@asranet.co.uk"])
    msg.attach(self.first_name + self.last_name + "DISS.pdf", pdf, "application/pdf")
    msg.send()
