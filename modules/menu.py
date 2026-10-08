import pygame


ICON_SIZE = (200, 200)


images = [
    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/menu/dashboard.png"
        ).convert_alpha(),
        ICON_SIZE
        ),
    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/menu/games.png"
        ).convert_alpha(),
        ICON_SIZE
        ),
    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/menu/online.png"
        ).convert_alpha(),
        ICON_SIZE
        ),
    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/menu/leaderboard.png"
        ).convert_alpha(),
        ICON_SIZE
        ),
    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/menu/setting.png"
        ).convert_alpha(),
        ICON_SIZE
        ),
    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/menu/support.png"
        ).convert_alpha(),
        ICON_SIZE
        ),
    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/menu/exit.png"
        ).convert_alpha(),
        ICON_SIZE
        ),

]

images_setting = [
    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/setting/music.png"
        ).convert_alpha(),
        ICON_SIZE
        ),
    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/setting/sound.png"
        ).convert_alpha(),
        ICON_SIZE
        ),
    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/setting/user.png"
        ).convert_alpha(),
        ICON_SIZE
        ),
    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/setting/lan.png"
        ).convert_alpha(),
        ICON_SIZE
        ),
    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/setting/more.png"
        ).convert_alpha(),
        ICON_SIZE
        ),
    pygame.transform.smoothscale(
        pygame.image.load(
            "./asset/image/setting/back.png"
        ).convert_alpha(),
        ICON_SIZE
        )

]

names = [
    "dashboard",
    "game library",
    "online",
    "leaderborad",
    "setting",
    "support",
    "exit"
]
names_setting = [
    "music",
    "sound",
    "account",
    "language",
    "more",
    "back"]


item_rects = []
item_rects_setting = []

scroll_y = 0

target_scroll_y = 0.0


def draw_six_scroll_items(
    screen,
    images,
    names,
    panel_rect,
    item_height,
    image_count,
    mode,
    scroll_y=0,
    font=None
):

    # =========================================================
    # CLEAR OLD RECTS
    # =========================================================

    item_rects.clear()
    item_rects_setting.clear()

    # =========================================================
    # CLIP AREA
    # =========================================================

    old_clip = screen.get_clip()

    screen.set_clip(panel_rect)

    # =========================================================
    # DRAW 7 ITEMS
    # =========================================================

    for i in range(image_count):

        image = images[i]
        name = names[i]

        # -----------------------------------------------------
        # ITEM Y
        # -----------------------------------------------------

        item_y = (
            panel_rect.y
            + i * item_height
            + scroll_y
        )

        # -----------------------------------------------------
        # IMAGE RECT
        # -----------------------------------------------------

        image_rect = image.get_rect(
            midleft=(
                panel_rect.x + 20,
                item_y + item_height // 2
            )
        )

        # -----------------------------------------------------
        # SAVE RECT
        # -----------------------------------------------------
        if mode == "menu":
            item_rects.append(
                image_rect.copy()
            )
        if mode == "setting":
            item_rects_setting.append(
                image_rect.copy()
            )

        # -----------------------------------------------------
        # DRAW IMAGE
        # -----------------------------------------------------

        screen.blit(
            image,
            image_rect
        )

        # -----------------------------------------------------
        # NAME
        # -----------------------------------------------------

        if font is not None:

            text_surface = font.render(
                name,
                True,
                (255, 135, 40)
            )

            text_rect = text_surface.get_rect(
                midleft=(
                    image_rect.right + 25,
                    image_rect.centery
                )
            )

            screen.blit(
                text_surface,
                text_rect
            )

    # =========================================================
    # RESTORE CLIP
    # =========================================================

    screen.set_clip(old_clip)
    
    
    
    
    
    
    
    
def handle_six_scroll_event(
    event,
    panel_rect,
    target_scroll_y,
    item_height
):

    if event.type == pygame.MOUSEWHEEL:

        if panel_rect.collidepoint(
            pygame.mouse.get_pos()
        ):

            target_scroll_y += event.y * 1100

            # -----------------------------------------
            # TOP LIMIT
            # -----------------------------------------

            target_scroll_y = min(
                0,
                target_scroll_y 
            )

            # -----------------------------------------
            # BOTTOM LIMIT
            # -----------------------------------------

            content_height = 7 * item_height

            max_scroll = -(
                content_height
                - panel_rect.height
            )

            target_scroll_y = max(
                max_scroll,
                target_scroll_y
            )

    return target_scroll_y