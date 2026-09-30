import pygame
#این تابع فقط برای رسم صفحه انتخاب عملیات و مدیریت نمایش/ آیکون‌های + - * / است.




operator_size = {
    "+": 400,
    "-": 400,
    "*": 400,
    "/": 400
}


def draw_operation_screen(
    screen,
    fonts,
    operator_images,
    operator_rects,
    current_width,
    current_height
):
    

    mouse_pos = pygame.mouse.get_pos()

    # # ---------------- Operation Box ----------------

    operator_box = pygame.Rect(
        current_width // 2 - 700 // 2,
        current_height // 2 - 400 // 2,
        650,
        350
    )


    spacing = 450

    x_positions = [
        operator_box.centerx - spacing * 1.5,
        operator_box.centerx - spacing * 0.5,
        operator_box.centerx + spacing * 0.5,
        operator_box.centerx + spacing * 1.5
    ]

    operators = ["+", "-", "*", "/"]

    for i, op in enumerate(operators):

        image = operator_images[op]

        rect = image.get_rect(
            center=(
                x_positions[i],
                current_height // 1.7
            )
        )

        image, image_rect, operator_size[op] = hover_image(
            image,
            rect,
            mouse_pos,
            operator_size[op]
        )
        
        screen.blit(
            image,
            image_rect
        )
        

        # محل کلیک
        operator_rects[op] = image_rect
        
        
        
def hover_image(
    image,
    rect,
    mouse_pos,
    current_size
):

    NORMAL_SIZE = 400
    HOVER_SIZE = 430
    SPEED = 2


    # محدوده ثابت برای تشخیص موس
    hit_rect = pygame.Rect(
        rect.centerx - NORMAL_SIZE // 2,
        rect.centery - NORMAL_SIZE // 2,
        NORMAL_SIZE,
        NORMAL_SIZE
    )

    if hit_rect.collidepoint(mouse_pos):

        if current_size < HOVER_SIZE:
            current_size = int(current_size)
            current_size += SPEED

    else:

        if current_size > NORMAL_SIZE:
            current_size = int(current_size)
            current_size -= SPEED

    new_image = pygame.transform.smoothscale(
        image,
        (
            current_size,
            current_size
        )
    )


    new_rect = new_image.get_rect(
        center=rect.center
    )


    return new_image, new_rect, current_size




