import pygame
from modules.hover import hover_image_for_time_screen

time_images = {
    3: pygame.image.load("./asset/image/time/3.png"),
    5: pygame.image.load("./asset/image/time/5.png"),
    10: pygame.image.load("./asset/image/time/10.png"),
    15: pygame.image.load("./asset/image/time/15.png")

}
# text_sizes = {
#     3: 35,
#     5: 35,
#     10: 35,
#     15: 35
# }

current_sizes = {}
time_sizes = {
    3: 200,
    5: 200,
    10: 200,
    15: 200
}

def draw_time_screen(
    screen,
    fonts,
    time_button_rects,
    current_width,
    current_height,
):

    mouse_pos = pygame.mouse.get_pos()

    times = [3, 5, 10, 15]

    image_size = 200
    hover_size = 220

    gap = 35

    total_width = (
        len(times) * image_size
        + (len(times) - 1) * gap
    )

    start_x = (
        current_width - total_width
    ) // 2

    center_y = current_height // 2 + 200


    for i, time in enumerate(times):

        x = start_x + i * (image_size + gap)


        normal_image = pygame.transform.smoothscale(
            time_images[time],
            (image_size, image_size)
        )

        rect = normal_image.get_rect(
            center=(
                x + image_size // 2,
                center_y
            )
        )


        # ذخیره دکمه
        time_button_rects[time] = rect

        image, image_rect, time_sizes[time] = hover_image_for_time_screen(
            time_images[time],
            rect,
            mouse_pos,
            time_sizes[time]
        )

        # عکس
        screen.blit(
            image,
            image_rect
        )
        # # if rect.collidepoint(mouse_pos):

        # #     if text_sizes[time] < 45:
        # #         text_sizes[time] += 1

        # # else:

        # #     if text_sizes[time] > 35:
        # #         text_sizes[time] -= 1


        # # text = pygame.font.Font(
        # #     "./asset/font/name.ttf",
        # #     text_sizes[time]
        # # ).render(
        # #     f"{time}s",
        # #     True,
        # #     (0,0,0)
        # # )


        # # text_rect = text.get_rect(
        # #     center=(
        # #         image_rect.centerx,
        # #         image_rect.centery + 5
        # #     )
        # # )

        # # screen.blit(
        # #     text,
        # #     text_rect
        # # )