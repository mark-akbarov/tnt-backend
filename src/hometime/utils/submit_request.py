from django.conf import settings
from django.utils import timezone

import telebot

from hometime.models.hometime import HomeTime
from user.models.user import User


bot = telebot.TeleBot(settings.HOMETIME_BOT_API_TOKEN)
chat_id = settings.HOMETIME_CHAT_ID


def submit_request(
    driver: User, 
    reason: str, 
    location_by_state: str, 
    start_date: str, 
    return_date: str,
    status: str,
    ):
    home_time = HomeTime.objects.create(
        driver=driver, 
        reason=reason, 
        location_by_state=location_by_state, 
        start_date=start_date,
        return_date=return_date
        )
    text = f"""
Request ID: {home_time.id}
Driver: {driver}
Requested for: {start_date} to {return_date}
Unit ID: {driver.unit_id}
VIN ID: {driver.vin_id}
Days Requested in Advance: {(start_date-timezone.now().date()).days}
Status: {status}
"""
    return bot.send_message(chat_id=chat_id, text=text)
