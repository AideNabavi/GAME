import pygame
import random
import sys


pygame.init()


# ============================================================
# SCREEN
# ============================================================

WIDTH = 1200
HEIGHT = 800

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Path Memory"
)

clock = pygame.time.Clock()


# ============================================================
# COLORS
# ============================================================

BACKGROUND = (20, 23, 32)

POINT_COLOR = (80, 170, 255)

POINT_ACTIVE = (90, 220, 140)

LINE_COLOR = (80, 170, 255)

PLAYER_LINE_COLOR = (255, 190, 70)

WHITE = (245, 245, 245)

GRAY = (150, 155, 165)

RED = (230, 70, 80)

GREEN = (70, 210, 120)


# ============================================================
# FONTS
# ============================================================

font_title = pygame.font.Font(
    None,
    48
)

font_normal = pygame.font.Font(
    None,
    30
)

font_small = pygame.font.Font(
    None,
    22
)

font_big = pygame.font.Font(
    None,
    64
)


# ============================================================
# GAME SETTINGS
# ============================================================

POINT_RADIUS = 14

CLICK_RADIUS = 32

LINE_WIDTH = 6

PLAYER_LINE_WIDTH = 7

SHOW_TIME = 1200

RESULT_TIME = 900


# ============================================================
# GAME STATE
# ============================================================

level = 1

score = 0

state = "SHOW"


# ============================================================
# PATH
# ============================================================

path = []

player_path = []

current_player_point = 0


# ============================================================
# TIMERS
# ============================================================

show_start_time = 0

result_start_time = 0


result_text = ""

result_color = WHITE


# ============================================================
# DRAW TEXT
# ============================================================

def draw_text(
    value,
    font,
    color,
    center
):

    surface = font.render(
        str(value),
        True,
        color
    )

    rect = surface.get_rect(
        center=center
    )

    screen.blit(
        surface,
        rect
    )


# ============================================================
# DISTANCE
# ============================================================

def distance(
    p1,
    p2
):

    dx = p1[0] - p2[0]

    dy = p1[1] - p2[1]

    return (
        dx * dx
        + dy * dy
    ) ** 0.5


# ============================================================
# CREATE PATH
# ============================================================

def create_path():

    global path
    global player_path
    global current_player_point
    global state
    global show_start_time

    number_of_points = level + 1

    path = []


    # --------------------------------------------------------
    # Create random points
    # --------------------------------------------------------

    attempts = 0


    while len(path) < number_of_points:

        attempts += 1


        if attempts > 10000:

            break


        x = random.randint(
            100,
            WIDTH - 100
        )

        y = random.randint(
            160,
            HEIGHT - 100
        )


        new_point = (
            x,
            y
        )


        # ----------------------------------------------------
        # Keep points separated
        # ----------------------------------------------------

        valid = True


        for old_point in path:

            if distance(
                new_point,
                old_point
            ) < 80:

                valid = False

                break


        if valid:

            path.append(
                new_point
            )


    # --------------------------------------------------------
    # Reset player
    # --------------------------------------------------------

    player_path = []

    current_player_point = 0


    # --------------------------------------------------------
    # Show path
    # --------------------------------------------------------

    state = "SHOW"

    show_start_time = (
        pygame.time.get_ticks()
    )


# ============================================================
# DRAW HEADER
# ============================================================

def draw_header():

    draw_text(
        "PATH MEMORY",
        font_title,
        WHITE,
        (
            WIDTH // 2,
            45
        )
    )


    draw_text(
        "Level " + str(level),
        font_normal,
        WHITE,
        (
            80,
            45
        )
    )


    draw_text(
        "Score: " + str(score),
        font_normal,
        WHITE,
        (
            WIDTH - 100,
            45
        )
    )


# ============================================================
# DRAW POINT
# ============================================================

def draw_point(
    point,
    color
):

    pygame.draw.circle(
        screen,
        color,
        point,
        POINT_RADIUS
    )


    pygame.draw.circle(
        screen,
        WHITE,
        point,
        POINT_RADIUS,
        2
    )


# ============================================================
# DRAW ORIGINAL PATH
# ============================================================

def draw_original_path():

    if len(path) < 2:

        return


    for i in range(
        len(path) - 1
    ):

        pygame.draw.line(
            screen,
            LINE_COLOR,
            path[i],
            path[i + 1],
            LINE_WIDTH
        )


# ============================================================
# DRAW PLAYER PATH
# ============================================================

def draw_player_path():

    if len(player_path) < 2:

        return


    for i in range(
        len(player_path) - 1
    ):

        pygame.draw.line(
            screen,
            PLAYER_LINE_COLOR,
            player_path[i],
            player_path[i + 1],
            PLAYER_LINE_WIDTH
        )


# ============================================================
# DRAW SHOW SCREEN
# ============================================================

def draw_show():

    screen.fill(
        BACKGROUND
    )


    draw_header()


    draw_text(
        "MEMORIZE THE PATH",
        font_normal,
        LINE_COLOR,
        (
            WIDTH // 2,
            105
        )
    )


    # --------------------------------------------------------
    # Original path
    # --------------------------------------------------------

    draw_original_path()


    # --------------------------------------------------------
    # Points
    # --------------------------------------------------------

    for i, point in enumerate(path):

        draw_point(
            point,
            POINT_COLOR
        )


        # Number

        draw_text(
            str(i + 1),
            font_small,
            WHITE,
            (
                point[0],
                point[1] - 30
            )
        )


# ============================================================
# DRAW PLAY SCREEN
# ============================================================

def draw_play():

    screen.fill(
        BACKGROUND
    )


    draw_header()


    draw_text(
        "REPEAT THE PATH",
        font_normal,
        PLAYER_LINE_COLOR,
        (
            WIDTH // 2,
            105
        )
    )


    # --------------------------------------------------------
    # Player path
    # --------------------------------------------------------

    draw_player_path()


    # --------------------------------------------------------
    # Points
    # --------------------------------------------------------

    for i, point in enumerate(path):

        if i < len(player_path):

            color = POINT_ACTIVE

        elif i == current_player_point:

            color = POINT_COLOR

        else:

            color = GRAY


        draw_point(
            point,
            color
        )


    # --------------------------------------------------------
    # Progress
    # --------------------------------------------------------

    draw_text(
        f"{len(player_path)} / {len(path)}",
        font_normal,
        WHITE,
        (
            WIDTH // 2,
            HEIGHT - 45
        )
    )


# ============================================================
# DRAW RESULT
# ============================================================

def draw_result():

    screen.fill(
        BACKGROUND
    )


    draw_header()


    draw_text(
        result_text,
        font_big,
        result_color,
        (
            WIDTH // 2,
            HEIGHT // 2
        )
    )


# ============================================================
# FIND POINT
# ============================================================

def find_point(
    mouse_position
):

    for index, point in enumerate(path):

        if distance(
            mouse_position,
            point
        ) <= CLICK_RADIUS:

            return index


    return None


# ============================================================
# PLAYER SELECT POINT
# ============================================================

def select_point(
    index
):

    global current_player_point
    global state
    global score
    global result_text
    global result_color
    global result_start_time


    # --------------------------------------------------------
    # Already selected
    # --------------------------------------------------------

    if index in player_path:

        return


    # --------------------------------------------------------
    # Check correct point
    # --------------------------------------------------------

    if index == current_player_point:

        player_path.append(
            path[index]
        )


        current_player_point += 1


        # ----------------------------------------------------
        # Complete
        # ----------------------------------------------------

        if current_player_point >= len(path):

            score += level * 100

            result_text = "CORRECT!"

            result_color = GREEN

            result_start_time = (
                pygame.time.get_ticks()
            )

            state = "RESULT"


    # --------------------------------------------------------
    # Wrong
    # --------------------------------------------------------

    else:

        result_text = "WRONG!"

        result_color = RED

        result_start_time = (
            pygame.time.get_ticks()
        )

        state = "RESULT"


# ============================================================
# MAIN
# ============================================================

create_path()


running = True


while running:

    # ========================================================
    # EVENTS
    # ========================================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


        # ----------------------------------------------------
        # Keyboard
        # ----------------------------------------------------

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                running = False


        # ----------------------------------------------------
        # Mouse
        # ----------------------------------------------------

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                if state == "PLAY":

                    index = find_point(
                        event.pos
                    )


                    if index is not None:

                        select_point(
                            index
                        )


    # ========================================================
    # SHOW
    # ========================================================

    if state == "SHOW":

        now = pygame.time.get_ticks()


        if (
            now - show_start_time
            >= SHOW_TIME
        ):

            state = "PLAY"


        draw_show()


    # ========================================================
    # PLAY
    # ========================================================

    elif state == "PLAY":

        draw_play()


    # ========================================================
    # RESULT
    # ========================================================

    elif state == "RESULT":

        draw_result()


        now = pygame.time.get_ticks()


        if (
            now - result_start_time
            >= RESULT_TIME
        ):

            if result_text == "CORRECT!":

                level += 1


            create_path()


    # ========================================================
    # UPDATE
    # ========================================================

    pygame.display.flip()

    clock.tick(60)


# ============================================================
# QUIT
# ============================================================

pygame.quit()

sys.exit()