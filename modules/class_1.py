# import pygame


# class Transition:

#     def __init__(self):

#         self.active = False
#         self.progress = 0
#         self.old_screen = None
#         self.new_screen = None



#     def start(self, old_screen, new_screen):

#         self.old_screen = old_screen.copy()
#         self.new_screen = new_screen.copy()

#         self.progress = 0
#         self.active = True



#     def update(self):

#         if self.active:

#             self.progress += 5


#             if self.progress >= 255:

#                 self.progress = 255
#                 self.active = False



#     def draw(self, screen):

#         if not self.active:
#             return

#         pygame.draw.rect(
#             screen,
#             (255,0,0),
#             (0,0,100,100)
#         )

#         # صفحه جدید پشت

#         screen.blit(
#             self.new_screen,
#             (0,0)
#         )


#         # صفحه قدیمی جلو

#         old = self.old_screen.copy()


#         old.set_alpha(
#             255 - self.progress
#         )


#         screen.blit(
#             old,
#             (
#                 -self.progress,
#                 0
#             )
#         )