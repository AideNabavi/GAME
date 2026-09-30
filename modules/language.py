import json
import pygame
import arabic_reshaper
from bidi.algorithm import get_display
from modules.EFFECT.hover import hover_image_lan

from modules.font import FONT_SIZES
def get_language_font(font_name):

    size = FONT_SIZES[font_name]

    return pygame.font.Font(
        current_font,
        size
    )
    

language_data = {}
current_language = "en"
current_font = None


def load_language(name):

    global language_data
    global current_language
    global current_font

    current_language = name

    with open(
        f"./asset/languages/{name}.json",
        "r",
        encoding="utf-8"
    ) as file:
        language_data = json.load(file)

    fonts = {
        "en": "./asset/font/en.ttf",
        "fa": "./asset/font/fa.ttf",
        "hi": "./asset/font/hi.ttf",
        "zh": "./asset/font/zh.ttf",
        "ru": "./asset/font/ru.ttf",
        "ar": "./asset/font/ar.ttf",
    }

    current_font = fonts[name]
    return name

def lang(key):

    return language_data.get(key, key)


def get_font(size):

    return pygame.font.Font(
        current_font,
        size
    )


def display_text(key):

    text = lang(key)

    if current_language in ("fa", "ar"):

        text = arabic_reshaper.reshape(text)
        text = get_display(text)

    return text















privacy_cache = {}
def prepare_privacy_text(text, language):

    cache_key = (language, text)

    if cache_key in privacy_cache:
        return privacy_cache[cache_key]

    if language in ("fa", "ar"):

        text = arabic_reshaper.reshape(text)
        text = get_display(text)

    privacy_cache[cache_key] = text

    return text
