import json
import pygame
import arabic_reshaper
from bidi.algorithm import get_display
from modules.hover import hover_image_lan

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
        "ru": "./asset/font/ru.ttf"
    }

    current_font = fonts[name]


def lang(key):
    return language_data.get(key, key)


def get_font(size):
    return pygame.font.Font(
        current_font,
        size
    )


def display_text(key):
    text = lang(key)

    if current_language == "fa":
        text = arabic_reshaper.reshape(text)
        text = get_display(text)

    return text














