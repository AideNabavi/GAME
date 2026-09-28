import os
import json
import time
from datetime import datetime


TIME_FILE = "/Users/mac/Desktop/app/online/time.json"

online_unix = 0
last_file_time = None
start_monotonic = 0


def load_online_time():

    global online_unix
    global last_file_time
    global start_monotonic

    try:

        with open(TIME_FILE, "r") as f:
            data = json.load(f)

        # آنلاین معتبر نیست
        if data.get("success") is False:
            return False

        # unix وجود ندارد
        if "unix" not in data:
            return False

        online_unix = data["unix"]

        last_file_time = os.path.getmtime(TIME_FILE)

        start_monotonic = time.monotonic()

        return True

    except Exception as e:

        print(f"❌ Failed to load online time: {e}")
        return False








def clock_ONLINE(screen, font_time, screen_width):

    global last_file_time

    # زمان آخرین تغییر فایل
    current_file_time = os.path.getmtime(TIME_FILE)

    # فقط اگر JSON تغییر کرده باشد دوباره بخوان
    if current_file_time != last_file_time:
        load_online_time()

    # زمان آنلاین + مدت زمانی که از خواندن JSON گذشته
    elapsed = time.monotonic() - start_monotonic

    current_unix = online_unix + elapsed

    now = datetime.fromtimestamp(current_unix)

    time_text = now.strftime("%H:%M:%S")

    time_surface = font_time.render(
        time_text,
        True,
        (255, 255, 255)
    )

    time_pos = (
        screen_width - 110,
        40
    )

    time_rect = time_surface.get_rect(
        topright=time_pos
    )

    screen.blit(time_surface, time_rect)











def clock_OFFLINE(screen, font_time, screen_width):
    now = datetime.now()

    time_text = now.strftime("%H:%M:%S")

    time_surface = font_time.render(
        time_text,
        True,
        (255, 255, 255)
    )

    time_pos = (
        screen_width - 110,
        40
    )

    time_rect = time_surface.get_rect(
        topright=time_pos
    )

    screen.blit(time_surface, time_rect)