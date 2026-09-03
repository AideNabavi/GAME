import pygame
import random
import time
import os
from modules.font import fonts


# -----------------------------
# Colors
# -----------------------------


CARD_BACK_IMAGE = "./asset/image/MODE/card_back.png"
# CARD_COLOR = (70, 70, 70)
card_back = pygame.image.load(
    CARD_BACK_IMAGE
).convert_alpha()




BG = (30, 30, 30)
OPEN_COLOR = (200, 100, 100)
TEXT_COLOR = (255, 255, 255)



# -----------------------------
# Game Settings
# -----------------------------

total_cards = 16

CARD_SIZE = 120
GAP = 10


cards = []


score = 0


first_card = None
second_card = None


waiting = False
wait_start = 0



show_cards = True
start_time = time.time()



GAME_TIME = 60

timer_start = None
game_over = False



score_text = None


def start_memory_game():

    global timer_start
    global show_cards
    global start_time
    global game_over
    global first_card
    global second_card
    global waiting


    timer_start = time.time()

    show_cards = True

    start_time = time.time()

    game_over = False

    first_card = None
    second_card = None

    waiting = False
    
    
    
    
    # -----------------------------
# Load Images
# -----------------------------

CARD_IMAGE_FOLDER = "./asset/image/MODE/memory_detect/"


all_images = []


for file in os.listdir(CARD_IMAGE_FOLDER):

    if file.endswith((".png", ".jpg", ".jpeg")):

        img = pygame.image.load(
            os.path.join(CARD_IMAGE_FOLDER, file)
        ).convert_alpha()


        all_images.append(img)



def reset_memory_game(WIDTH, HEIGHT):

    global timer_start
    global show_cards
    global start_time
    global game_over
    global first_card
    global second_card
    global waiting
    global wait_start
    global score
    global score_text

    # -----------------------------
    # Reset score
    # -----------------------------

    score = 0

    # -----------------------------
    # Reset game state
    # -----------------------------

    game_over = False

    first_card = None
    second_card = None

    waiting = False
    wait_start = 0

    # -----------------------------
    # Reset timers
    # -----------------------------

    timer_start = time.time()

    start_time = time.time()

    # -----------------------------
    # Show cards again
    # -----------------------------

    show_cards = True

    # -----------------------------
    # Create new cards
    # -----------------------------

    create_cards(
        WIDTH,
        HEIGHT
    )
    
# -----------------------------
# Create Cards
# -----------------------------

def create_cards(WIDTH, HEIGHT):

    global cards

    cards = []


    selected_images = random.sample(
        all_images,
        total_cards // 2
    )


    card_images = selected_images * 2

    random.shuffle(card_images)



    cols = 4

    rows = (total_cards + cols - 1) // cols



    grid_width = (
        cols * CARD_SIZE
        +
        (cols - 1) * GAP
    )


    grid_height = (
        rows * CARD_SIZE
        +
        (rows - 1) * GAP
    )



    start_x = (WIDTH - grid_width) // 2

    start_y = (HEIGHT - grid_height) // 2



    index = 0



    for row in range(rows):

        for col in range(cols):


            if index >= total_cards:
                break



            rect = pygame.Rect(

                start_x + col * (CARD_SIZE + GAP),

                start_y + row * (CARD_SIZE + GAP),

                CARD_SIZE,

                CARD_SIZE

            )



            cards.append({

                "rect": rect,

                "image": card_images[index],

                "open": True,

                "found": False

            })



            index += 1








card_back = pygame.transform.smoothscale(
    card_back,
    (CARD_SIZE, CARD_SIZE)
)

# -----------------------------
# Memory Game
# -----------------------------
def memory_(screen, WIDTH, HEIGHT):

    global timer_start
    global score
    global score_text
    global show_cards
    global start_time
    global waiting
    global first_card
    global second_card
    global wait_start
    global total_cards
    global game_over


    # =========================================================
    # TIMER
    # =========================================================

    elapsed_time = time.time() - timer_start

    remaining_time = (
        GAME_TIME - int(elapsed_time)
    )

    if remaining_time <= 0:

        remaining_time = 0

        game_over = True


    # =========================================================
    # TIMER TEXT
    # =========================================================

    time_text = fonts["heart"].render(

        f"Time: {remaining_time}",

        True,

        TEXT_COLOR

    )

    screen.blit(

        time_text,

        (
            WIDTH - time_text.get_width() - 20,
            20
        )

    )


    # =========================================================
    # SHOW CARDS
    # =========================================================

    if show_cards:

        if time.time() - start_time >= 5:

            show_cards = False

            for card in cards:

                card["open"] = False


    # =========================================================
    # CLOSE WRONG CARDS
    # =========================================================

    if waiting:

        if time.time() - wait_start >= 1:

            if first_card is not None:

                first_card["open"] = False

            if second_card is not None:

                second_card["open"] = False


            first_card = None

            second_card = None

            waiting = False


    # =========================================================
    # DRAW CARDS
    # =========================================================

    for card in cards:

        # -----------------------------------------------------
        # FOUND CARDS
        # -----------------------------------------------------

        if card["found"]:

            continue


        # =====================================================
        # SHOWING CARDS AT START
        # =====================================================

        if show_cards:

            # -----------------------------------------------
            # LIGHT YELLOW BACKGROUND
            # -----------------------------------------------

            pygame.draw.rect(

                screen,

                (255, 245, 180),

                card["rect"],

                border_radius=15

            )


            # -----------------------------------------------
            # CARD IMAGE
            # -----------------------------------------------

            img = pygame.transform.smoothscale(

                card["image"],

                (90, 90)

            )


            img_rect = img.get_rect(

                center=card["rect"].center

            )


            screen.blit(

                img,

                img_rect

            )


        # =====================================================
        # OPEN CARD
        # =====================================================

        elif card["open"]:

            # -----------------------------------------------
            # LIGHT YELLOW BACKGROUND
            # -----------------------------------------------

            pygame.draw.rect(

                screen,

                (255, 245, 180),

                card["rect"],

                border_radius=15

            )


            # -----------------------------------------------
            # CARD IMAGE
            # -----------------------------------------------

            img = pygame.transform.smoothscale(

                card["image"],

                (90, 90)

            )


            img_rect = img.get_rect(

                center=card["rect"].center

            )


            screen.blit(

                img,

                img_rect

            )


        # =====================================================
        # CLOSED CARD
        # =====================================================

        else:

            screen.blit(

                card_back,

                card["rect"]

            )


    # =========================================================
    # SCORE
    # =========================================================

    score_text = fonts["heart"].render(

        f"Score: {score}",

        True,

        TEXT_COLOR

    )


    screen.blit(

        score_text,

        (
            20,
            HEIGHT - 70
        )

    )
    
    
    
def memory_click(mouse_pos):

    global first_card
    global second_card
    global waiting
    global wait_start
    global score


    if show_cards:
        return


    if waiting:
        return



    for card in cards:


        if card["rect"].collidepoint(mouse_pos):


            if not card["open"] and not card["found"]:


                card["open"] = True



                if first_card is None:


                    first_card = card



                elif second_card is None:


                    second_card = card



                    if first_card["image"] == second_card["image"]:


                        first_card["found"] = True

                        second_card["found"] = True


                        score += 10


                        first_card = None

                        second_card = None



                    else:


                        waiting = True

                        wait_start = time.time()


                break