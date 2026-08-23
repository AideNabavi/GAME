






# ----------------------------------------------------- Text Stroke Function 
def draw_text_stroke(surface, text_surface, position, stroke_color=(0,0,0), stroke_size=2):
    
    x, y = position

    # بالا
    surface.blit(
        text_surface,
        (x, y - stroke_size)
    )

    # پایین
    surface.blit(
        text_surface,
        (x, y + stroke_size)
    )

    # چپ
    surface.blit(
        text_surface,
        (x - stroke_size, y)
    )

    # راست
    surface.blit(
        text_surface,
        (x + stroke_size, y)
    )
    
    



