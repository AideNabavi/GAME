import pygame


# ==================================================
# VARIABLES
# ==================================================

selected_background = 0

background_images = []

theme_images = []

theme_rects = []

theme_sizes = [

    (350,220),
    (350,220),
    (350,220),
    (350,220),
    (350,220),
    (350,220)

]

# ==================================================
# LOAD BACKGROUNDS
# ==================================================

def load_backgrounds(screen):

    global background_images


    background_images = []


    width, height = screen.get_size()


    for i in range(1,7):

        img = pygame.image.load(
            f"./asset/image/background/{i}.png"
        ).convert()


        img = pygame.transform.smoothscale(
            img,
            (width, height)
        )


        background_images.append(img)



# ==================================================
# LOAD THEME IMAGES
# ==================================================

def load_theme_images():

    global theme_images


    theme_images = []


    for i in range(1,7):

        img = pygame.image.load(
            f"./asset/image/background/{i}.png"
        ).convert_alpha()


        img = pygame.transform.smoothscale(
            img,
            (350,220)
        )


        theme_images.append(img)






theme_sizes = [

    (350, 220),
    (350, 220),
    (350, 220),
    (350, 220),
    (350, 220),
    (350, 220)

]


def draw_theme(screen, gap_x, gap_y):

    global theme_rects
    global theme_sizes

    theme_rects = []

    mouse_pos = pygame.mouse.get_pos()

    center_x = screen.get_width() // 2
    center_y = screen.get_height() // 2 +150

    # اندازه کل گروه 3 × 2
    total_width = 2 * gap_x
    total_height = gap_y

    start_x = center_x - total_width // 2
    start_y = center_y - total_height // 2

    for i, img in enumerate(theme_images):

        row = i // 3
        col = i % 3

        x = start_x + col * gap_x
        y = start_y + row * gap_y

        rect = img.get_rect(
            center=(x, y)
        )

        image, image_rect, theme_sizes[i] = hover_image_theme(
            img,
            rect,
            mouse_pos,
            theme_sizes[i]
        )

        screen.blit(image, image_rect)

        theme_rects.append(
            (i, image_rect)
        )

    return theme_rects

# ==================================================
# THEME POSITIONS
# ==================================================

# theme_positions = [

#     (150,120),
#     (550,120),
#     (950,120),

#     (150,430),
#     (550,430),
#     (950,430)

# ]



# # ==================================================
# # DRAW THEME PAGE
# # ==================================================

# def draw_theme(screen):

#     global theme_rects
#     global theme_sizes


#     theme_rects = []


#     mouse_pos = pygame.mouse.get_pos()



#     for i,pos in enumerate(theme_positions):


#         rect = theme_images[i].get_rect(
#             topleft=pos
#         )


#         image, image_rect, theme_sizes[i] = hover_image_theme(
#             theme_images[i],
#             rect,
#             mouse_pos,
#             theme_sizes[i]
#         )


#         screen.blit(
#             image,
#             image_rect
#         )


#         theme_rects.append(
#             (i,image_rect)
#         )


# # ==================================================
# CLICK THEME
# ==================================================

def theme_event(event):

    global selected_background


    if event.type == pygame.MOUSEBUTTONDOWN:


        if event.button == 1:


            for i, rect in theme_rects:


                if rect.collidepoint(event.pos):


                    selected_background = i




# ==================================================
# DRAW CURRENT BACKGROUND
# ==================================================

def draw__background(screen):


    screen.blit(
        background_images[selected_background],
        (0,0)
    )



# ==================================================
# START LOAD
# ==================================================

def init_theme(screen):

    load_backgrounds(screen)

    load_theme_images()
    
    
    
    
    
    
    
    


def hover_image_theme(
    image,
    rect,
    mouse_pos,
    current_size
):

    NORMAL_SIZE = (350,220)
    HOVER_SIZE = (380,230)

    SPEED = 5


    width, height = current_size


    if rect.collidepoint(mouse_pos):

        if width < HOVER_SIZE[0]:
            width += SPEED

        if height < HOVER_SIZE[1]:
            height += SPEED


    else:

        if width > NORMAL_SIZE[0]:
            width -= SPEED

        if height > NORMAL_SIZE[1]:
            height -= SPEED



    new_image = pygame.transform.smoothscale(
        image,
        (
            int(width),
            int(height)
        )
    )


    new_rect = new_image.get_rect(
        center=rect.center
    )


    return new_image, new_rect, (width,height)