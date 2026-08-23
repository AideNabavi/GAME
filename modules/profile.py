import pygame

#----------------------------------------------
# profile
p99 = pygame.image.load("./asset/image/profile/p.png").convert_alpha()
p99 = pygame.transform.smoothscale(p99, (220, 220))
p999 = pygame.transform.smoothscale(p99, (300, 300))


selected_profile_image=None


final_profile=None
angle = 0


def rotate_image_center(screen, image, center, angle):

    rotated_image = pygame.transform.rotate(
        image,
        angle
    )

    rotated_rect = rotated_image.get_rect(
        center=center
    )

    screen.blit(
        rotated_image,
        rotated_rect
    )


def draw_profile_live_circle(
    screen,
    selected_profile_image,
    p99,
    current_width
):

    global angle

    if selected_profile_image:

        profile_rect = selected_profile_image.get_rect(
            center=(current_width//2 + 890, 136)
        )

        # عکس پروفایل
        screen.blit(
            selected_profile_image,
            profile_rect
        )


        # زاویه چرخش
        angle += 5


        # قاب چرخان روی مرکز پروفایل
        rotate_image_center(
            screen,
            p99,
            profile_rect.center,
            angle
        )





def draw_profile_in_profile_tab(
    screen,
    selected_profile_image,
    p999,
    current_width,
    current_height
):

    global angle

    if selected_profile_image:
        selected_profile_image=pygame.transform.smoothscale(selected_profile_image,(280,280))
        profile_rect = selected_profile_image.get_rect(
            center=(current_width//2 - 790, current_height - 750 )
        )

        # عکس پروفایل
        screen.blit(
            selected_profile_image,
            profile_rect
        )


        # زاویه چرخش
        angle += 5


        # قاب چرخان روی مرکز پروفایل
        rotate_image_center(
            screen,
            p999,
            profile_rect.center,
            angle
        )










