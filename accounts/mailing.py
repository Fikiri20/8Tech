from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_registration_email(*, to: str, subject: str, context: dict,):

    html_content = render_to_string('registration_success_email.html', context)

    # text_content = strip_tags(html)

    email = EmailMultiAlternatives(
        subject=subject,
        to=[to],
        from_email='8teqsolution@gmail.com',

    )
    email.body = html_content
    email.content_subtype = "html"
    email.send()

    