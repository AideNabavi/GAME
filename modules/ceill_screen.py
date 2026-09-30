import pygame


ceill = 0
ceill_entered = False
ceill_text = ""


ceill_button_rects = {}



ceill_button_rects = {}
operator_size = {
    "100":400,
    "1000":400,
    "10000":400
}


image_100 = pygame.image.load(
    "./asset/image/ceil/1.png"
).convert_alpha()

image_1000 = pygame.image.load(
    "./asset/image/ceil/2.png"
).convert_alpha()

image_10000 = pygame.image.load(
    "./asset/image/ceil/3.png"
).convert_alpha()


operator_images = {
    "100": image_100,
    "1000": image_1000,
    "10000": image_10000
}



def draw_ceil_screen(
    screen,
    fonts,
    current_width,
    current_height
):

    mouse_pos = pygame.mouse.get_pos()


    operator_box = pygame.Rect(
        current_width // 2 - 700 // 2,
        current_height // 2 - 400 // 2,
        650,
        350
    )


    spacing = 450


    x_positions = [
        operator_box.centerx - spacing,
        operator_box.centerx,
        operator_box.centerx + spacing
    ]


    operators = ["100", "1000", "10000"]


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


        ceill_button_rects[op] = image_rect
        
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
            current_size += SPEED

    else:

        if current_size > NORMAL_SIZE:
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