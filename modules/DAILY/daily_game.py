import json
import random
import os
import pygame

GAME_ID = {
    0: "ACTION",
    1: "DETECT",
    2: "DETECT_PRO",
    3: "DIRECTION",
    4: "FAST",
    5: "FAST_ADD_SUB",
    6: "FIND_NUMBER",
    7: "FIND_OPERATOR",
    8: "FOLLOW_THAT",
    9: "HARD",
    10: "HOW_MANY",
    11: "IMAGE_SELECT",
    12: "MATH_GO",
    13: "MEMORY_GO",
    14: "MEMORY",
    15: "MIRROR",
    16: "MOVE_ARROW",
    17: "MORE_LESS_EQUAL",
    18: "SIX_60S",
    19: "TRUE_FALSE",
    20: "REPEAT_AFTER_ME",
    21: "SHAPE_COLOR_NAME",
    22: "FIDN_NUMBER"
}


GAMES_FILE = "./games.json"


def save_games(data):

    with open(GAMES_FILE, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


def load_games():

    if not os.path.exists(GAMES_FILE):
        return None

    try:

        with open(GAMES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except (json.JSONDecodeError, OSError):

        return None


def create_cycle(all_games):

    games = list(all_games.values())

    random.shuffle(games)

    return games

def get_daily_games(all_games, current_date, count=3):

    data = load_games()

    # =====================================================
    # اولین اجرا
    # =====================================================

    if data is None:

        remaining_games = create_cycle(all_games)

        daily_games = remaining_games[:count]
        remaining_games = remaining_games[count:]

        data = {
            "date": current_date,
            "daily_games": daily_games,
            "remaining_games": remaining_games
        }

        save_games(data)

        return daily_games


    # =====================================================
    # اگر همان روز است
    # =====================================================

    if data.get("date") == current_date:

        return data.get("daily_games", [])


    # =====================================================
    # روز جدید
    # =====================================================

    remaining_games = data.get("remaining_games", [])

    daily_games = []


    # =====================================================
    # تا زمانی که 3 بازی انتخاب نشده
    # =====================================================

    while len(daily_games) < count:

        # اگر چرخه تمام شده
        if len(remaining_games) == 0:

            remaining_games = create_cycle(all_games)

        # بازی بعدی را بردار
        daily_games.append(
            remaining_games.pop(0)
        )


    # =====================================================
    # ذخیره وضعیت
    # =====================================================

    data = {
        "date": current_date,
        "daily_games": daily_games,
        "remaining_games": remaining_games
    }

    save_games(data)

    return daily_games


















# این برای گرفتن عکس ها از پوشه  باید در اول بازی صدا زده شود 
today_image_game = []

def get_daily_game_images(game_ids, folder="asset/image/MODE"):
    global today_image_game

    for game_id in game_ids:

        image_path = os.path.join(
            folder,
            f"{game_id}.png"
        )

        if not os.path.exists(image_path):
            today_image_game.append(None)
            continue

        image = pygame.image.load(image_path).convert_alpha()

        today_image_game.append(image)

    return today_image_game
