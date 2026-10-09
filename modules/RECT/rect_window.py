import pygame


# =========================================================
# PUNCH FRAMES
# =========================================================

def create_punch_frames(
    width,
    height,
    color,
    radius=20,
    alpha=255,
    shadow=10,
    shadow_alpha=50,
    scale=2,
    frame_count=30,
    start_scale=0.65,
    overshoot=1.12
):

    frames = []

    for frame in range(frame_count):

        # ---------------------------------------------
        # PROGRESS
        # ---------------------------------------------

        t = frame / (frame_count - 1)

        if t < 0.65:

            p = t / 0.65

            # Ease Out
            p = 1 - (1 - p) ** 3

            current_scale = (
                start_scale
                + (overshoot - start_scale) * p
            )

        else:

            p = (t - 0.65) / 0.35

            # Ease Out
            p = 1 - (1 - p) ** 3

            current_scale = (
                overshoot
                + (1.0 - overshoot) * p
            )

        # ---------------------------------------------
        # SIZE
        # ---------------------------------------------

        current_width = max(
            1,
            int(width * current_scale)
        )

        current_height = max(
            1,
            int(height * current_scale)
        )

        current_radius = max(
            0,
            int(radius * current_scale)
        )

        current_shadow = max(
            0,
            int(shadow * current_scale)
        )

        # ---------------------------------------------
        # SURFACE
        # ---------------------------------------------

        padding = current_shadow

        temp = pygame.Surface(
            (
                (current_width + padding * 2) * scale,
                (current_height + padding * 2) * scale
            ),
            pygame.SRCALPHA
        )

        # ---------------------------------------------
        # SHADOW
        # ---------------------------------------------

        if current_shadow > 0:

            for i in range(
                current_shadow,
                0,
                -1
            ):

                strength = (
                    1 - (i / current_shadow)
                ) ** 3

                current_alpha = int(
                    shadow_alpha * strength
                )

                pygame.draw.rect(
                    temp,
                    (
                        0,
                        0,
                        0,
                        current_alpha
                    ),
                    (
                        (current_shadow - i) * scale,
                        (current_shadow - i) * scale,
                        (current_width + i * 2) * scale,
                        (current_height + i * 2) * scale
                    ),
                    border_radius=(
                        current_radius + i
                    ) * scale
                )

        # ---------------------------------------------
        # MAIN RECTANGLE
        # ---------------------------------------------

        pygame.draw.rect(
            temp,
            (
                *color[:3],
                alpha
            ),
            (
                current_shadow * scale,
                current_shadow * scale,
                current_width * scale,
                current_height * scale
            ),
            border_radius=current_radius * scale
        )

        # ---------------------------------------------
        # DOWNSCALE
        # ---------------------------------------------

        final_surface = pygame.transform.smoothscale(
            temp,
            (
                current_width + padding * 2,
                current_height + padding * 2
            )
        )

        frames.append(final_surface)

    return frames


# =========================================================
# PUNCH STATE
# =========================================================

punch_state = {
    "start_time": None,
    "finished": False
}


# =========================================================
# DRAW PUNCH
# =========================================================

def draw_punch_rect(
    screen,
    frames,
    center,
    state,
    duration=0.55
):

    now = pygame.time.get_ticks() / 1000.0

    # -----------------------------------------------------
    # INITIALIZE
    # -----------------------------------------------------

    if state["start_time"] is None:
        state["start_time"] = now
        state["finished"] = False

    # -----------------------------------------------------
    # TIME
    # -----------------------------------------------------

    elapsed = now - state["start_time"]

    t = elapsed / duration

    if t >= 1.0:
        t = 1.0
        state["finished"] = True

    # -----------------------------------------------------
    # FRAME
    # -----------------------------------------------------

    frame_index = int(
        t * (len(frames) - 1)
    )

    frame_index = max(
        0,
        min(
            frame_index,
            len(frames) - 1
        )
    )

    surface = frames[frame_index]

    # -----------------------------------------------------
    # DRAW
    # -----------------------------------------------------

    rect = surface.get_rect(
        center=center
    )

    screen.blit(
        surface,
        rect
    )


# =========================================================
# RESET
# =========================================================

def reset_punch(state):

    state["start_time"] = None
    state["finished"] = False