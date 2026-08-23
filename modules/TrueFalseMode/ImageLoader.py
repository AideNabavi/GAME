# import pygame

# images = []

# def load_images():
#     global images

#     paths = [
#         "./asset/image/mode_TrueFalse/1.png",
#         "./asset/image/mode_TrueFalse/1.png",
#         "./asset/image/mode_TrueFalse/1.png",
#         "./asset/image/mode_TrueFalse/1.png",
#         "./asset/image/mode_TrueFalse/1.png",
#         "./asset/image/mode_TrueFalse/1.png"
#     ]

#     for path in paths:
#         img = pygame.image.load(path).convert_alpha()

#         img = pygame.transform.smoothscale(
#             img,
#             (140, 140)
#         )

#         images.append(img)





# image_game_mode = []

# def draw_images(screen):

#     if not images:
#         load_images()


#     w, h = screen.get_size()

#     size = 150
#     gap = 100

#     total_width = (size * 3) + (gap * 2)

#     start_x = (w - total_width) // 2
#     start_y = h // 2 - 200

#     image_game_mode.clear()

#     for i, img in enumerate(images):

#         row = i // 3
#         col = i % 3

#         x = start_x + col * (size + gap)
#         y = start_y + row * (size + gap)
        
        
#         rect=img.get_rect(topleft=(x,y))
#         image_game_mode.append(rect)
        
        
#         screen.blit(img,rect)
#         # screen.blit(img, (x, y))