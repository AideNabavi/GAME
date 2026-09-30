import pygame


def set_game_cursor():
    # بارگذاری تصویر نشانگر
    cursor_image = pygame.transform.smoothscale(pygame.image.load(
        "asset/image/cursor.png"
    ).convert_alpha(),(70,70))

    # تبدیل تصویر به Cursor
    cursor = pygame.cursors.Cursor(
        (0, 0),
        cursor_image
    )

    # اعمال نشانگر جدید
    pygame.mouse.set_cursor(cursor)


def reset_cursor():
    # بازگرداندن نشانگر پیش‌فرض
    pygame.mouse.set_cursor(
        pygame.cursors.Cursor()
    )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import pygame
import random
import math

click_effects = []

def create_click_effect(pos):

    particles = []

    for _ in range(10):

        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(60, 150)

        particles.append({
            "x": pos[0],
            "y": pos[1],
            "vx": math.cos(angle) * speed,
            "vy": math.sin(angle) * speed,
            "size": random.randint(3, 9),
        })

    click_effects.append({
        "particles": particles,
        "start": pygame.time.get_ticks()
    })


def draw_click_effect(screen):

    now = pygame.time.get_ticks()

    for effect in click_effects[:]:

        elapsed = now - effect["start"]

        duration = 450
        progress = elapsed / duration

        if progress >= 1:
            click_effects.remove(effect)
            continue

        alpha = int(255 * (1 - progress))

        for particle in effect["particles"]:

            # حرکت ذره
            particle["x"] += particle["vx"] / 60
            particle["y"] += particle["vy"] / 60

            # کمی کاهش سرعت
            particle["vx"] *= 0.97
            particle["vy"] *= 0.97

            # کوچک شدن ذره
            size = int(
                particle["size"] * (1 - progress)
            )

            if size <= 0:
                continue

            pygame.draw.circle(
                screen,
                (255, 255, 255, alpha),
                (
                    int(particle["x"]),
                    int(particle["y"])
                ),
                size
            )