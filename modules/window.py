import pygame


gallery_image=pygame.image.load("./asset/image/button/gallery.png")

# gallery_image=pygame.transform.smoothscale(gallery_image,(850,1050))



gallery_scale = 0.8
donate_scale = 0
profile_scale = 0

def _window(screen, small_window):
    # current_width, current_height = screen.get_size()
    global gallery_scale, donate_scale, profile_scale

    if small_window == "gallery":

        # screen.blit(gallery_image, (current_width//2 - 425,current_height//2 - 525))

        gallery_scale = draw_zoom_image(
            screen,
            gallery_image,
            gallery_scale
        )

    # elif small_window == "donate":

    #     screen.blit(donate_image, (0,0))


    # elif small_window == "profile":

    #     screen.blit(profile_image, (0,0))
    
    
def draw_zoom_image(
    screen,
    image,
    scale
    
):
    target_size=800
    speed=0.15
    scale += (1 - scale) * speed


    if scale > 0.999:
        scale = 1


    size = int(target_size * scale)


    img = pygame.transform.smoothscale(
        image,
        (size, size)
    )


    rect = img.get_rect(
        center=(
            screen.get_width() // 2,
            screen.get_height() // 2
        )
    )


    screen.blit(img, rect)


    return scale