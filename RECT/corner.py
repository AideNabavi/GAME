
import pygame
from modules.RECT.rec import create_smooth_rect


corner = pygame.transform.smoothscale(
    pygame.image.load("./asset/image/menu/achievement.png"),
    (100, 100)
)

corner_face_rec = None



right_card_state = {
    "start_time": None,
    "x": 0,
    "y": 0,
    "target_x": 0,
    "target_y": 0,
    "last_activity": 0,
    "first_show": True
}

corner_rec = []

right_card = create_smooth_rect(
    400,
    220,
    (255, 255, 255),
    radius=200,
    alpha=255,
    shadow=10,
    shadow_alpha=50
)


def darw_corner_face(
    screen,
    card_surface,
    visible_x,
    hidden_x,
    target_x,
    visible_y,
    hidden_y,
    target_y,
    state,
    images,
    texts,
    font,
    mouse_trigger_x=500,
    hide_delay=5.0
):
    now = pygame.time.get_ticks() / 1000.0

    # INITIALIZE: مبدأ حرکت
    if state["start_time"] is None:
        state["start_time"] = now

        state["x"] = visible_x
        state["y"] = visible_y

        state["target_x"] = visible_x
        state["target_y"] = visible_y

        state["last_activity"] = now

    # FIRST SHOW: حرکت از مبدأ به مقصد
    if state["first_show"]:
        if now - state["start_time"] >= 1.0:
            state["target_x"] = target_x
            state["target_y"] = target_y
            state["first_show"] = False

    # AUTO HIDE: برگشت به مختصات مخفی
    elif now - state["last_activity"] >= hide_delay:
        state["target_x"] = hidden_x
        state["target_y"] = hidden_y

    # SMOOTH MOVEMENT X
    state["x"] += (state["target_x"] - state["x"]) * 0.08

    # SMOOTH MOVEMENT Y
    state["y"] += (state["target_y"] - state["y"]) * 0.08

    # SNAP
    if abs(state["target_x"] - state["x"]) < 0.5:
        state["x"] = state["target_x"]

    if abs(state["target_y"] - state["y"]) < 0.5:
        state["y"] = state["target_y"]

    # DRAW CARD
    card_x = int(state["x"])
    card_y = int(state["y"])

    rotated_card = pygame.transform.rotate(card_surface, -45)

    card_rect = rotated_card.get_rect(
        center=card_surface.get_rect(
            topleft=(card_x, card_y)
        ).center
    )

    screen.blit(rotated_card, card_rect)

    # DRAW IMAGE
    corner_rec.clear()

    if images:
        image = images[0]

        image_x = card_x + (
            card_surface.get_width() - image.get_width()
        ) // 2 - 66

        image_y = card_y 

        image_rect = image.get_rect(
            topleft=(image_x, image_y)
        )

        corner_rec.append(image_rect)
        screen.blit(image, image_rect)


def corner_card_event(event, state, target_x, target_y):
    if event.type == pygame.MOUSEMOTION:
        mouse_x, mouse_y = event.pos

        # محدوده گوشه پایین سمت راست صفحه
        if mouse_x >= 1820 and mouse_y >= 980:
            state["last_activity"] = pygame.time.get_ticks() / 1000.0
            state["target_x"] = target_x
            state["target_y"] = target_y
    















#############################################################
right_card_1 = create_smooth_rect(
    400,
    203,
    (255, 255, 255),
    radius=200,
    alpha=255,
    shadow=10,
    shadow_alpha=50
)


corner_face_rec_top=None

corner_rec_1 = []


top = pygame.transform.smoothscale(
    pygame.image.load("./asset/image/menu/achievement.png"),
    (100, 100)
)


top_right_card_state = {
    "start_time": None,
    "x": 0,
    "y": 0,
    "target_x": 0,
    "target_y": 0,
    "last_activity": 0,
    "first_show": True
}


def darw_corner_face_top(
    screen,
    card_surface,
    visible_x,
    hidden_x,
    target_x,
    visible_y,
    hidden_y,
    target_y,
    state,
    images,
    texts,
    font,
    mouse_trigger_x=500,
    hide_delay=5.0
):
    now = pygame.time.get_ticks() / 1000.0

    # INITIALIZE: مبدأ حرکت
    if state["start_time"] is None:
        state["start_time"] = now

        state["x"] = visible_x
        state["y"] = visible_y

        state["target_x"] = visible_x
        state["target_y"] = visible_y

        state["last_activity"] = now

    # FIRST SHOW: حرکت از مبدأ به مقصد
    if state["first_show"]:
        if now - state["start_time"] >= 1.0:
            state["target_x"] = target_x
            state["target_y"] = target_y
            state["first_show"] = False

    # AUTO HIDE: برگشت به مختصات مخفی
    elif now - state["last_activity"] >= hide_delay:
        state["target_x"] = hidden_x
        state["target_y"] = hidden_y

    # SMOOTH MOVEMENT X
    state["x"] += (state["target_x"] - state["x"]) * 0.08

    # SMOOTH MOVEMENT Y
    state["y"] += (state["target_y"] - state["y"]) * 0.08

    # SNAP
    if abs(state["target_x"] - state["x"]) < 0.5:
        state["x"] = state["target_x"]

    if abs(state["target_y"] - state["y"]) < 0.5:
        state["y"] = state["target_y"]

    # DRAW CARD
    card_x = int(state["x"])
    card_y = int(state["y"])

    rotated_card = pygame.transform.rotate(card_surface, -135)

    card_rect = rotated_card.get_rect(
        center=card_surface.get_rect(
            topleft=(card_x, card_y)
        ).center
    )

    screen.blit(rotated_card, card_rect)

    # DRAW IMAGE
    corner_rec_1.clear()

    if images:
        image = images[0]

        image_x = card_x + (
            card_surface.get_width() - image.get_width()
        ) // 2 - 68

        image_y = card_y  + 130

        image_rect = image.get_rect(
            topleft=(image_x, image_y)
        )

        corner_rec_1.append(image_rect)
        screen.blit(image, image_rect)


def corner_top_card_event(event, state, target_x, target_y):
    if event.type == pygame.MOUSEMOTION:
        mouse_x, mouse_y = event.pos

        # محدوده گوشه پایین سمت راست صفحه
        if mouse_x >= 1820 and mouse_y <=80:
            state["last_activity"] = pygame.time.get_ticks() / 1000.0
            state["target_x"] = target_x
            state["target_y"] = target_y
    