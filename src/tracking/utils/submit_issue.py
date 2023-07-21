from django.conf import settings

import telebot

from user.models.base import User
from tracking.models.truck import TrailerIssue, TruckIssue


bot = telebot.TeleBot(settings.API_TOKEN)


def submit_truck_issue(driver: User, issue: str, photos: list, status: str):
    truck_issue = TruckIssue.objects.create(driver=driver, issue=issue, status=status)
    truck_issue.photos.set(photos)
    text = f"""
Truck Issue ID: {truck_issue.id}
Driver: {driver.username}
Issue Type: {issue}
Status: {truck_issue.status}
Unit ID: {driver.unit_id}
VIN ID: {driver.vin_id}
Created Time: {format_datetime(truck_issue.created_at)}
"""
    bot.send_media_group(chat_id=settings.CHAT_ID, media=send_compressed_photos(photos, caption=text))


def submit_trailer_issue(driver: User, issue: str, photos: list, status: str):
    trailer_issue = TrailerIssue.objects.create(driver=driver, issue=issue, status=status)
    trailer_issue.photos.set(photos)
    text = f"""
Trailer Issue ID: {trailer_issue.id}
Driver: {driver.username}
Issue Type: {issue}
Status: {trailer_issue.status}
Unit ID: {driver.unit_id}
VIN ID: {driver.vin_id}
Created Time: {format_datetime(trailer_issue.created_at)}
"""
    bot.send_media_group(chat_id=settings.CHAT_ID, media=send_compressed_photos(trailer_issue.photos.all(), caption=text))


def send_compressed_photos(photos: list, caption: str):
    photo_paths = [f"../media/{photo.image}" for photo in photos]
    return [telebot.types.InputMediaPhoto(open(f"{photo_paths[num]}", "rb"), caption=caption if num == 0 else '') for num in range(len(photo_paths))]


def format_datetime(created_time: str) -> str:
    from datetime import datetime
    parsed_time = datetime.strptime(str(created_time), "%Y-%m-%d %H:%M:%S.%f%z")
    formatted_time = parsed_time.strftime("%B %d, %Y %I:%M %p")
    return formatted_time
