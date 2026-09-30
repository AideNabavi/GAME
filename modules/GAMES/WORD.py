
        
# def event_WROD(event):
    
import pygame
import random

from modules.font import *


# =========================================================
# SCREEN 
# =========================================================

HEIGHT = None
WIDTH = None
screen = None


def WIDTH_HEIGHT_gettter(screen_, WIDTH_, HEIGHT_):

    global WIDTH
    global HEIGHT
    global screen

    WIDTH = WIDTH_
    HEIGHT = HEIGHT_
    screen = screen_


# =========================================================
# WORDS
# =========================================================

WORDS = [
    "apple", "orange", "banana", "grape", "lemon",
    "water", "coffee", "bread", "cheese", "butter",
    "chicken", "potato", "tomato", "carrot", "sugar",
    "school", "teacher", "student", "library", "book",
    "pencil", "paper", "window", "door", "table",
    "chair", "garden", "house", "family", "friend",
    "mother", "father", "brother", "sister", "child",
    "computer", "keyboard", "screen", "phone", "camera",
    "internet", "website", "program", "python", "game",
    "music", "movie", "picture", "video", "sound",
    "forest", "mountain", "river", "ocean", "island",
    "beach", "desert", "flower", "tree", "grass",
    "animal", "rabbit", "tiger", "lion", "elephant",
    "monkey", "horse", "bird", "fish", "snake",
    "castle", "bridge", "road", "street",
    "city", "village", "country", "world", "planet",
    "office", "hospital", "market", "store",
    "restaurant", "hotel", "airport", "station", "museum",
    "morning", "evening", "night", "today", "tomorrow",
    "summer", "winter", "spring", "autumn", "weather",
    "happy", "angry", "strong", "small", "large",
    "beautiful", "simple", "difficult", "easy", "important",
    "fast", "slow", "bright", "dark", "young",
    "fire", "earth", "air", "light",
    "energy", "power", "space", "star", "moon",
    "money", "business", "company", "number",
    "answer", "question", "problem", "example", "reason",
    "people", "person", "football", "basketball",
    "tennis", "player", "winner", "lesson",
    "language", "english", "letter", "word",
    "sentence", "story", "reading", "writing",
    "science", "history", "future", "knowledge",
    "travel", "holiday", "ticket", "car",
    "train", "bus", "bicycle", "airplane",
    "message", "email", "breakfast", "lunch",
    "dinner", "kitchen", "bedroom", "bathroom",
    "shirt", "jacket", "shoes", "clothes", "color",
    "circle", "square", "shape", "line",

    "phonebook", "wallet", "pocket", "bottle",
    "basket", "mirror", "clock", "key", "doorway",
    "roof", "floor", "wall",
    "riverbank", "sunlight", "rainbow", "cloud", "storm",

    "dog", "cat", "mouse", "bear", "wolf",
    "fox", "deer", "zebra", "giraffe", "kangaroo",
    "panda", "dolphin", "whale", "shark", "turtle",
    "frog", "eagle", "owl", "parrot",
    "penguin", "duck", "goat", "sheep",
    "cow", "pig", "donkey", "camel",

    "spoon", "fork", "knife", "plate", "glass",
    "cup", "bowl", "broom", "brush", "towel",
    "soap", "toothbrush", "pillow", "blanket", "lamp",
    "box", "bag", "umbrella", "hat",
    "coat", "sock", "glove", "watch", "ring",
    "necklace", "button", "pajamas", "scarf", "belt",

    "marketplace", "bakery", "theater", "cinema",
    "factory", "farm", "garage", "prison", "church",
    "temple", "university", "classroom", "playground", "stadium",
    "park", "tower", "building", "apartment",
    "balcony", "basement",
    "bed", "sofa", "shelf", "drawer", "carpet",

    "piano", "guitar", "violin", "drum", "trumpet",
    "song", "dance", "artist", "actor", "singer",
    "writer", "doctor", "nurse", "driver", "farmer",
    "engineer", "pilot", "chef", "worker", "manager",

    "king", "queen", "prince", "princess", "soldier",
    "hero", "leader", "team", "group", "member",
    "victory", "battle", "challenge", "adventure", "journey",
    "secret", "dream", "idea", "plan", "goal",
    "hope", "love", "peace", "fear", "smile",
    "laugh", "cry", "heart", "mind", "brain",
    "body", "face", "hand", "finger", "foot",
    "head", "hair", "eye", "ear", "nose",

    "riverbed", "waterfall", "volcano", "valley", "forestland",
    "coast", "lake", "pond", "hill",
    "rock", "stone", "sand", "rain",
    "snow", "wind", "thunder", "lightning", "sunshine",
    "sunset", "sunrise", "rainfall", "season", "temperature",

    "gold", "silver", "diamond", "coin", "price",
    "shop", "customer", "product", "service", "payment",

    "robot", "machine", "engine", "battery",
    "mousepad", "speaker", "headphone",
    "radio", "television", "newspaper", "magazine",
    "letterbox", "package", "address", "passport", "document",

    "celebration",
    "chocolate",
    "comfortable",
    "community",
    "dangerous",
    "different",
    "education",
    "elephantine",
    "environment",
    "especially",
    "experience",
    "fantastic",
    "friendship",
    "generation",
    "happiness",
    "information",
    "interesting",
    "knowledgeable",
    "laughter",
    "mechanical",
    "mountainside",
    "neighborhood",
    "opportunity",
    "photograph",
    "population",
    "possibility",
    "professional",
    "something",
    "successful",
    "technology",
    "telephone",
    "together",
    "understanding",
    "wonderful",
    "yesterday",
    "conversation",
    "discovering",
    "imagination",
    "independent",
    "relationship",
    "transportation"
]


# =========================================================
# COLORS
# =========================================================

BG = (30, 45, 35)
WHITE = (245, 245, 235)
BLACK = (20, 20, 20)

WOOD = (115, 75, 42)
WOOD_DARK = (75, 45, 25)

EMPTY = (225, 220, 190)

GREEN = (75, 190, 95)
RED = (205, 65, 60)
YELLOW = (240, 200, 70)

GRAY = (120, 120, 120)
BLUE = (75, 150, 220)

LETTER_ACTIVE = (70, 130, 80)


# =========================================================
# GAME SETTINGS
# =========================================================

TIME_LIMIT = 60

MAX_LIVES = 3

GAME_PLAYING = "PLAYING"
GAME_OVER = "GAMEOVER"

game_state = GAME_PLAYING


# =========================================================
# GAME VARIABLES
# =========================================================

word = ""

display_word = []

used_words = []

score = 0
combo = 0
lives = MAX_LIVES

start_time = 0

selected_letter = None

wrong_message_timer = 0

# برای جلوگیری از delay
next_word_time = 0


# =========================================================
# LETTER BUTTONS
# =========================================================

letter_buttons = []

button_size = 65
gap = 10

start_x = 115
start_y = 560


for i in range(26):

    row = i // 9
    col = i % 9

    x = start_x + col * (button_size + gap)
    y = start_y + row * (button_size + gap)

    rect = pygame.Rect(
        x,
        y,
        button_size,
        button_size
    )

    letter_buttons.append(
        (
            chr(65 + i),
            rect
        )
    )


# =========================================================
# GET MISSING COUNT
# =========================================================

def get_missing_count(length):

    if length <= 4:
        return 1

    elif length == 5:
        return 2

    elif length == 6:
        return 3

    elif length == 7:
        return 3

    elif length == 8:
        return 4

    elif length == 9:
        return 4

    else:
        return 5


# =========================================================
# CREATE WORD
# =========================================================

def create_word():

    global word
    global display_word
    global selected_letter

    if len(used_words) >= len(WORDS):

        used_words.clear()

    available = [
        w for w in WORDS
        if w not in used_words
    ]

    word = random.choice(available).upper()

    used_words.append(word.lower())

    missing_count = get_missing_count(
        len(word)
    )

    missing_count = min(
        missing_count,
        len(word)
    )

    positions = random.sample(
        range(len(word)),
        missing_count
    )

    display_word = list(word)

    for pos in positions:

        display_word[pos] = "_"

    selected_letter = None


# =========================================================
# RESET GAME
# =========================================================

def reset_word():

    global score
    global combo
    global lives
    global game_state
    global start_time
    global wrong_message_timer
    global next_word_time
    global selected_letter

    score = 0

    combo = 0

    lives = MAX_LIVES

    used_words.clear()

    selected_letter = None

    wrong_message_timer = 0

    next_word_time = 0

    start_time = pygame.time.get_ticks()

    game_state = GAME_PLAYING

    create_word()


# =========================================================
# CHECK WORD COMPLETE
# =========================================================

def is_complete():

    return "_" not in display_word


# =========================================================
# SELECT LETTER
# =========================================================

def select_letter(letter):

    global score
    global combo
    global lives
    global game_state
    global wrong_message_timer
    global next_word_time

    if game_state != GAME_PLAYING:
        return

    letter = letter.upper()

    missing_positions = [
        i
        for i, char in enumerate(display_word)
        if char == "_"
    ]

    correct = False

    for pos in missing_positions:

        if word[pos] == letter:

            correct = True

            break

    # =====================================================
    # CORRECT
    # =====================================================

    if correct:

        for pos in missing_positions:

            if word[pos] == letter:

                display_word[pos] = letter

        score += 50

        if is_complete():

            combo += 1

            score += combo * 25

            # به جای pygame.time.delay
            # کلمه بعدی را کمی بعد نمایش می‌دهیم
            next_word_time = (
                pygame.time.get_ticks()
                + 300
            )

    # =====================================================
    # WRONG
    # =====================================================

    else:

        lives -= 1

        combo = 0

        score = max(
            0,
            score - 25
        )

        wrong_message_timer = 1000

        if lives <= 0:

            game_state = GAME_OVER


# =========================================================
# UPDATE GAME
# =========================================================

def update_word():

    global wrong_message_timer
    global game_state

    current_time = pygame.time.get_ticks()

    # =====================================================
    # WRONG MESSAGE TIMER
    # =====================================================

    if wrong_message_timer > 0:

        wrong_message_timer -= 16

        if wrong_message_timer < 0:

            wrong_message_timer = 0

    # =====================================================
    # NEXT WORD
    # =====================================================

    if (
        game_state == GAME_PLAYING
        and next_word_time > 0
        and current_time >= next_word_time
    ):

        create_word()

        globals()["next_word_time"] = 0

    # =====================================================
    # GAME TIMER
    # =====================================================

    if game_state == GAME_PLAYING:

        elapsed = (
            current_time - start_time
        ) / 1000

        if elapsed >= TIME_LIMIT:

            game_state = GAME_OVER


# =========================================================
# DRAW TEXT CENTER
# =========================================================

def draw_center(
    text,
    font,
    color,
    y
):

    surface = font.render(
        text,
        True,
        color
    )

    screen.blit(
        surface,
        (
            WIDTH // 2 -
            surface.get_width() // 2,
            y
        )
    )


# =========================================================
# DRAW LIVES
# =========================================================

def draw_lives():

    for i in range(MAX_LIVES):

        color = (
            RED
            if i < lives
            else GRAY
        )

        text = fonts["heart"].render(
            "♥",
            True,
            color
        )

        screen.blit(
            text,
            (
                40 + i * 45,
                30
            )
        )


# =========================================================
# DRAW WORD
# =========================================================

def draw_word():

    spacing = 18

    surfaces = []

    for char in display_word:

        color = (
            RED
            if char == "_"
            else WHITE
        )

        surfaces.append(
            fonts["heart"].render(
                char,
                True,
                color
            )
        )

    if not surfaces:
        return

    total_width = sum(
        surface.get_width()
        for surface in surfaces
    ) + spacing * (
        len(surfaces) - 1
    )

    x = (
        WIDTH // 2 -
        total_width // 2
    )

    for surface in surfaces:

        screen.blit(
            surface,
            (
                x,
                220
            )
        )

        x += (
            surface.get_width()
            + spacing
        )


# =========================================================
# DRAW LETTERS
# =========================================================

def draw_letters():

    mouse_pos = pygame.mouse.get_pos()

    for letter, rect in letter_buttons:

        color = LETTER_ACTIVE

        if rect.collidepoint(mouse_pos):

            color = (
                90,
                160,
                100
            )

        pygame.draw.rect(
            screen,
            color,
            rect,
            border_radius=10
        )

        text = fonts["heart"].render(
            letter,
            True,
            WHITE
        )

        text_rect = text.get_rect(
            center=rect.center
        )

        screen.blit(
            text,
            text_rect
        )


# =========================================================
# DRAW GAME
# =========================================================

def draw_game():

    screen.fill(BG)

    # =====================================================
    # TITLE
    # =====================================================

    draw_center(
        "COMPLETE THE WORD",
        fonts["heart"],
        WHITE,
        90
    )

    # =====================================================
    # SCORE
    # =====================================================

    score_text = fonts["heart"].render(
        f"Score: {score}",
        True,
        WHITE
    )

    screen.blit(
        score_text,
        (
            WIDTH -
            score_text.get_width() -
            40,
            35
        )
    )

    # =====================================================
    # LIVES
    # =====================================================

    draw_lives()

    # =====================================================
    # TIMER
    # =====================================================

    elapsed = (
        pygame.time.get_ticks()
        - start_time
    ) / 1000

    remaining = max(
        0,
        TIME_LIMIT - elapsed
    )

    timer_color = (
        RED
        if remaining <= 10
        else WHITE
    )

    timer = fonts["heart"].render(
        f"Time: {int(remaining)}",
        True,
        timer_color
    )

    screen.blit(
        timer,
        (
            WIDTH // 2 -
            timer.get_width() // 2,
            155
        )
    )

    # =====================================================
    # COMBO
    # =====================================================

    if combo > 0:

        combo_text = fonts["heart"].render(
            f"COMBO x{combo}",
            True,
            YELLOW
        )

        screen.blit(
            combo_text,
            (
                WIDTH // 2 -
                combo_text.get_width() // 2,
                300
            )
        )

    # =====================================================
    # WORD
    # =====================================================

    draw_word()

    # =====================================================
    # LETTERS
    # =====================================================

    draw_letters()

    # =====================================================
    # WRONG MESSAGE
    # =====================================================

    if wrong_message_timer > 0:

        text = fonts["heart"].render(
            "-25",
            True,
            RED
        )

        screen.blit(
            text,
            (
                WIDTH // 2 -
                text.get_width() // 2,
                360
            )
        )


# =========================================================
# DRAW GAME OVER
# =========================================================

def draw_gameover():

    screen.fill(BG)

    draw_center(
        "GAME OVER",
        fonts["heart"],
        RED,
        220
    )

    draw_center(
        f"Score: {score}",
        fonts["heart"],
        WHITE,
        310
    )

    draw_center(
        "Press R to play again",
        fonts["heart"],
        WHITE,
        390
    )

    draw_center(
        "Press ESC to exit",
        fonts["heart"],
        WHITE,
        430
    )


# =========================================================
# EVENT HANDLER
# =========================================================

def event_WORD(event):

    global game_state

    # =====================================================
    # KEYBOARD
    # =====================================================

    if event.type == pygame.KEYDOWN:

        # -------------------------------------------------
        # ESC
        # -------------------------------------------------

        if event.key == pygame.K_ESCAPE:

            reset_word()

            return

        # -------------------------------------------------
        # R
        # -------------------------------------------------

        if event.key == pygame.K_r:

            reset_word()

            return

    # =====================================================
    # MOUSE
    # =====================================================

    if event.type == pygame.MOUSEBUTTONDOWN:

        if event.button == 1:

            if game_state == GAME_PLAYING:

                for letter, rect in letter_buttons:

                    if rect.collidepoint(event.pos):

                        select_letter(letter)

                        return


# =========================================================
# MAIN DRAW FUNCTION
# =========================================================

def WORD_():

    update_word()

    if game_state == GAME_PLAYING:

        draw_game()

    elif game_state == GAME_OVER:

        draw_gameover()


# =========================================================
# OPTIONAL COMPATIBILITY
# =========================================================
# اگر قبلاً در فایل اصلی event_WROD صدا زده بودی
# این اسم هم کار خواهد کرد.

def reset_word():
    global word
    global display_word
    global used_words
    global score
    global combo
    global lives
    global start_time
    global selected_letter
    global wrong_message_timer
    global next_word_time
    global game_state

    word = ""

    display_word = []

    used_words.clear()

    score = 0
    combo = 0
    lives = 3

    start_time = pygame.time.get_ticks()

    selected_letter = None

    wrong_message_timer = 0
    next_word_time = 0

    game_state = "PLAYING"

    create_word()