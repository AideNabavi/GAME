import pygame
from PIL import Image


def load_gif(path):
    gif = Image.open(path)

    frames = []

    while True:
        frame = gif.convert("RGBA")

        frame_data = frame.tobytes()

        surface = pygame.image.fromstring(
            frame_data,
            frame.size,
            "RGBA"
        )

        frames.append(surface)

        try:
            gif.seek(gif.tell() + 1)
        except EOFError:
            break

    return frames








gif_frames_levels=load_gif("./asset/gif/levels.gif")
gif_frames_mode=load_gif("./asset/gif/mode.gif")
gif_frames_theme=load_gif("./asset/gif/theme.gif")
gif_frames_lan=load_gif("./asset/gif/lan.gif")
gif_frames_about=load_gif("./asset/gif/about.gif")
gif_frames_support=load_gif("./asset/gif/support.gif")
gif_frames_score=load_gif("./asset/gif/gift.gif")
gif_frames_sound=load_gif("./asset/gif/sound.gif")
gif_frames = load_gif("./asset/gif/time.gif")
gif_frames_music = load_gif("./asset/gif/music.gif")
gif_frames_credit = load_gif("./asset/gif/credit.gif")
gif_frames_op = load_gif("./asset/gif/op.gif")
gif_frames_profile= load_gif("./asset/gif/profile.gif")

w_gif=250
h_gif=250
gif_frames = [
    pygame.transform.smoothscale(frame, (w_gif, h_gif))
    for frame in gif_frames
]
gif_frames_music = [
    pygame.transform.smoothscale(frame, (200, 200))
    for frame in gif_frames_music
]
gif_frames_credit = [
    pygame.transform.smoothscale(frame, (w_gif, h_gif))
    for frame in gif_frames_credit
]
gif_frames_op = [
    pygame.transform.smoothscale(frame, (w_gif, h_gif))
    for frame in gif_frames_op
]
gif_frames_sound= [
    pygame.transform.smoothscale(frame, (200, 200))
    for frame in gif_frames_sound
]
gif_frames_score= [
    pygame.transform.smoothscale(frame, (200, 200))
    for frame in gif_frames_score
]
gif_frames_profile= [
    pygame.transform.smoothscale(frame, (200, 200))
    for frame in gif_frames_profile
]
gif_frames_lan= [
    pygame.transform.smoothscale(frame, (200, 200))
    for frame in gif_frames_lan
]
gif_frames_support= [
    pygame.transform.smoothscale(frame, (200, 200))
    for frame in gif_frames_support
]
gif_frames_about= [
    pygame.transform.smoothscale(frame, (200, 200))
    for frame in gif_frames_about
]
gif_frames_theme= [
    pygame.transform.smoothscale(frame, (200, 200))
    for frame in gif_frames_theme
]
gif_frames_levels= [
    pygame.transform.smoothscale(frame, (200, 200))
    for frame in gif_frames_levels
]
gif_frames_mode= [
    pygame.transform.smoothscale(frame, (200, 200))
    for frame in gif_frames_mode
]


gif_index = 0
gif_timer = 0




def gif_setting(screen,gif_name,x,y):
        global gif_timer
        global gif_index
        gif_timer += 1

        if gif_timer >= 1:
            gif_index += 1
            gif_timer = 0

            if gif_index >= len(gif_name):
                gif_index = 0

        screen.blit(
            gif_name[gif_index],
            (
            x,
            y,
            )
        )
        
