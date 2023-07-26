from django.conf import settings

from mailjet_rest import Client


def send_email(recipient_email: str, code: str):
    api_key = settings.MAILJET_API_KEY
    api_secret = settings.MAILJET_SECRET_KEY
    mailjet = Client(auth=(api_key, api_secret), version='v3')
    data = {
    'FromEmail': "",
    'FromName': "Your Verification Code",
    'Recipients': [
        {
        "Email": recipient_email,
        "Name": "Someone"
        }
    ],
    'Subject': "Verification Code",
    'Html-part': f"<h3>Verification Code: <b>{code}</b>"
    }
    result = mailjet.send.create(data=data)
    if result.status_code == '200':
        return "success"
