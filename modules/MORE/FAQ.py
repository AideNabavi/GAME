import pygame

from modules.font import fonts


# ============================================================
# FAQ TEXT
# ============================================================

privacy_text = """


Last Updated: September 2026



________________________________________________________


What is Fast Mathter Club?

Fast Mathter Club is a brain game club created for
thinking, learning, and entertainment.

The games are designed to challenge and exercise different
mental skills such as memory, logic, concentration, reaction
speed, mathematical thinking, problem-solving, accuracy,
and attention.


________________________________________________________


How many games are available?

The current version of Mental Math Challenge includes
40 games.

The game club is planned to grow to 60 games in future
updates.

Currently, 10 games are free and additional games are
available as Premium games.


________________________________________________________


Can I play the games offline?

Yes.

The current version of Mental Math Challenge is designed
to work offline.

An internet connection is not required to play the
current games.

Future versions may introduce online features.


________________________________________________________


How many players can play the games?

Mental Math Challenge is designed to support different
game modes, including:

• 1-player games
• 2-player games
• 3-player games
• 4-player games

The current version mainly includes single-player games.

Multiplayer games are planned for future versions.


________________________________________________________


How do I start a game?

Open the Games section from the main menu and select
the game you want to play.

Before starting a game, instructions are provided to
explain the rules and how to play.


________________________________________________________


How do I know what to do in each game?

Each game includes an instruction screen before gameplay.

The instruction screen explains the objective, rules,
and what the player needs to do.


________________________________________________________


What happens when I lose a game?

You can play the game again.

A Restart button is available in the games, allowing
you to restart the challenge and try again.


________________________________________________________


How do I earn XP?

You can earn XP by completing your Daily Workout
challenges.

Completing more daily challenges allows you to earn
more XP.


________________________________________________________


Can I replay games?

Yes.

You can replay available games to practice, improve your
performance, and try to achieve better results.


________________________________________________________


What is Daily Workout?

Daily Workout is a daily challenge system in
Mental Math Challenge.

Every day at 7:00 AM, the game can notify you that
your daily challenges are ready.

You can open the game and complete your daily games
to earn XP.


________________________________________________________


What is Guest Mode?

Guest Mode allows you to play the games without creating
a player profile.

Guest Mode is intended for players who want to play
without saving profile information.


________________________________________________________


What information is stored in my profile?

The current offline version stores limited profile
information locally on your device.

This may include:

• Username
• Selected avatar
• Selected country flag

This information is used to display and personalize
your player profile.


________________________________________________________


Can I change my avatar?

Yes.

You can change your selected avatar from:

Settings → Account


________________________________________________________


Can I change the game language?

Yes.

Mental Math Challenge currently supports:

• English
• Persian
• Arabic
• Chinese
• Hindi
• Russian


________________________________________________________


Can I change the music and sound effects?

Yes.

You can manage music and sound effects from the
Settings section.

The game includes 12 music tracks.

You can select different music tracks or turn the
music off.

You can also adjust the sound effects or turn them
on or off.


________________________________________________________


What should I do if I find a bug?

You can report bugs through:

Support → Report Bug

You can report a problem using the available report
form or contact the support team through the available
contact methods, including email and Telegram.


________________________________________________________


What should I do if my game crashes?

If the game crashes, closes unexpectedly, or you
experience a technical problem, please use the
Report Bug section to report the problem.

Providing details about what happened can help us
investigate and fix the issue.


________________________________________________________


What information does the current version collect?

The current offline version stores only limited
profile information locally on your device.

This may include:

• Username
• Selected avatar
• Selected country flag

The current offline version does not require or
collect:

• Email address
• Password
• Phone number
• Home address
• Exact location
• Payment information


________________________________________________________


Why does the game need an internet connection?

The current version does not require an internet
connection for gameplay.

Future versions may introduce online features such as:

• Online multiplayer
• Online accounts
• Cloud saves
• Online leaderboards
• Chat rooms
• Social features

If these features are introduced, the game and its
Privacy Policy will be updated accordingly.


________________________________________________________


Can I delete my profile or saved data?

Yes.

You can remove locally stored game and profile data
by deleting the game's local data or uninstalling
the application.

Deleting local data may remove:

• Game progress
• Scores and records
• Achievements and statistics
• Game settings
• Username
• Avatar
• Country flag


________________________________________________________


Will Mental Math Challenge receive new features?

Yes.

Future versions may introduce new games, multiplayer
modes, online features, additional social features,
and other improvements.

Features may change as the game continues to develop.


________________________________________________________


How can I contact support?

If you have questions, find a bug, or need help with
the game, you can contact us through the available
support options.

Email:
nabavi447@gmail.com

Telegram:
Available through the Support section in the game.


________________________________________________________
"""


# ============================================================
# COLORS
# ============================================================

FAQ_TITLE_COLOR = (60, 60, 60)

FAQ_DATE_COLOR = (120, 80, 40)

# رنگ سؤال‌ها
FAQ_QUESTION_COLOR = (210, 120, 30)

# رنگ جواب‌ها
FAQ_ANSWER_COLOR = (50, 50, 50)

# رنگ خطوط جداکننده
FAQ_LINE_COLOR = (150, 110, 70)


# ============================================================
# SCROLL VARIABLES
# ============================================================

scroll_y = 0

scroll_velocity = 0

friction = 0.94


# ============================================================
# OPEN FAQ
# ============================================================

# None یعنی هیچ سؤالی باز نیست
#
# مثلاً:
# 0 = سؤال اول
# 1 = سؤال دوم
# 2 = سؤال سوم

open_faq_index = None


# ============================================================
# QUESTION RECTS
# ============================================================

faq_question_rects = []


# ============================================================
# FAQ DATA
# ============================================================

FAQ_ITEMS = [

    (
        "What is Fast Mathter Club?",
        """Fast Mathter Club is a brain game club created for
thinking, learning, and entertainment.

The games are designed to challenge and exercise different
mental skills such as memory, logic, concentration, reaction
speed, mathematical thinking, problem-solving, accuracy,
and attention."""
    ),

    (
        "How many games are available?",
        """The current version of Mental Math Challenge includes
40 games.

The game club is planned to grow to 60 games in future
updates.

Currently, 10 games are free and additional games are
available as Premium games."""
    ),

    (
        "Can I play the games offline?",
        """Yes.

The current version of Mental Math Challenge is designed
to work offline.

An internet connection is not required to play the
current games.

Future versions may introduce online features."""
    ),

    (
        "How many players can play the games?",
        """Mental Math Challenge is designed to support different
game modes, including:

• 1-player games
• 2-player games
• 3-player games
• 4-player games

The current version mainly includes single-player games.

Multiplayer games are planned for future versions."""
    ),

    (
        "How do I start a game?",
        """Open the Games section from the main menu and select
the game you want to play.

Before starting a game, instructions are provided to
explain the rules and how to play."""
    ),

    (
        "How do I know what to do in each game?",
        """Each game includes an instruction screen before gameplay.

The instruction screen explains the objective, rules,
and what the player needs to do."""
    ),

    (
        "What happens when I lose a game?",
        """You can play the game again.

A Restart button is available in the games, allowing
you to restart the challenge and try again."""
    ),

    (
        "How do I earn XP?",
        """You can earn XP by completing your Daily Workout
challenges.

Completing more daily challenges allows you to earn
more XP."""
    ),

    (
        "Can I replay games?",
        """Yes.

You can replay available games to practice, improve your
performance, and try to achieve better results."""
    ),

    (
        "What is Daily Workout?",
        """Daily Workout is a daily challenge system in
Mental Math Challenge.

Every day at 7:00 AM, the game can notify you that
your daily challenges are ready.

You can open the game and complete your daily games
to earn XP."""
    ),

    (
        "What is Guest Mode?",
        """Guest Mode allows you to play the games without creating
a player profile.

Guest Mode is intended for players who want to play
without saving profile information."""
    ),

    (
        "What information is stored in my profile?",
        """The current offline version stores limited profile
information locally on your device.

This may include:

• Username
• Selected avatar
• Selected country flag

This information is used to display and personalize
your player profile."""
    ),

    (
        "Can I change my avatar?",
        """Yes.

You can change your selected avatar from:

Settings → Account"""
    ),

    (
        "Can I change the game language?",
        """Yes.

Mental Math Challenge currently supports:

• English
• Persian
• Arabic
• Chinese
• Hindi
• Russian"""
    ),

    (
        "Can I change the music and sound effects?",
        """Yes.

You can manage music and sound effects from the
Settings section.

The game includes 12 music tracks.

You can select different music tracks or turn the
music off.

You can also adjust the sound effects or turn them
on or off."""
    ),

    (
        "What should I do if I find a bug?",
        """You can report bugs through:

Support → Report Bug

You can report a problem using the available report
form or contact the support team through the available
contact methods, including email and Telegram."""
    ),

    (
        "What should I do if my game crashes?",
        """If the game crashes, closes unexpectedly, or you
experience a technical problem, please use the
Report Bug section to report the problem.

Providing details about what happened can help us
investigate and fix the issue."""
    ),

    (
        "What information does the current version collect?",
        """The current offline version stores only limited
profile information locally on your device.

This may include:

• Username
• Selected avatar
• Selected country flag

The current offline version does not require or
collect:

• Email address
• Password
• Phone number
• Home address
• Exact location
• Payment information"""
    ),

    (
        "Why does the game need an internet connection?",
        """The current version does not require an internet
connection for gameplay.

Future versions may introduce online features such as:

• Online multiplayer
• Online accounts
• Cloud saves
• Online leaderboards
• Chat rooms
• Social features

If these features are introduced, the game and its
Privacy Policy will be updated accordingly."""
    ),

    (
        "Can I delete my profile or saved data?",
        """Yes.

You can remove locally stored game and profile data
by deleting the game's local data or uninstalling
the application.

Deleting local data may remove:

• Game progress
• Scores and records
• Achievements and statistics
• Game settings
• Username
• Avatar
• Country flag"""
    ),

    (
        "Will Mental Math Challenge receive new features?",
        """Yes.

Future versions may introduce new games, multiplayer
modes, online features, additional social features,
and other improvements.

Features may change as the game continues to develop."""
    ),

    (
        "How can I contact support?",
        """If you have questions, find a bug, or need help with
the game, you can contact us through the available
support options.

Email:
nabavi447@gmail.com

Telegram:
Available through the Support section in the game."""
    ),
]


# ============================================================
# DRAW FAQ
# ============================================================

def draw_FAQ(screen, privacy_box):

    global scroll_y
    global scroll_velocity
    global faq_question_rects

    # ========================================================
    # SCROLL
    # ========================================================

    scroll_y += scroll_velocity

    scroll_velocity *= friction

    if abs(scroll_velocity) < 0.1:
        scroll_velocity = 0

    # ========================================================
    # TOP LIMIT
    # ========================================================

    if scroll_y < 0:
        scroll_y = 0
        scroll_velocity = 0

    # ========================================================
    # CLIP
    # ========================================================

    screen.set_clip(privacy_box)

    # ========================================================
    # QUESTION RECTS RESET
    # ========================================================

    faq_question_rects = []

    # ========================================================
    # START Y
    # ========================================================

    y = privacy_box.y + 40 - scroll_y

    # ========================================================
    # FAQ TITLE
    # ========================================================

    title_surface = fonts["TITLE_NEW"].render(
        "FAQ",
        True,
        FAQ_TITLE_COLOR
    )

    screen.blit(
        title_surface,
        (
            privacy_box.x + 40,
            int(y)
        )
    )

    y += 60

    # ========================================================
    # LAST UPDATED
    # ========================================================

    date_surface = fonts["TITLE_NEW"].render(
        "Last Updated: September 2026",
        True,
        FAQ_DATE_COLOR
    )

    screen.blit(
        date_surface,
        (
            privacy_box.x + 40,
            int(y)
        )
    )

    y += 70

    # ========================================================
    # WELCOME
    # ========================================================

    welcome_text = (
        "Welcome to Mental Math Challenge."
    )

    welcome_surface = fonts["date"].render(
        welcome_text,
        True,
        FAQ_ANSWER_COLOR
    )

    screen.blit(
        welcome_surface,
        (
            privacy_box.x + 40,
            int(y)
        )
    )

    y += 55

    # ========================================================
    # DESCRIPTION
    # ========================================================

    description_lines = [
        "This FAQ provides answers to common questions about",
        "the current version of the game, its features, gameplay,",
        "profiles, settings, and future updates."
    ]

    for line in description_lines:

        surface = fonts["date"].render(
            line,
            True,
            FAQ_ANSWER_COLOR
        )

        screen.blit(
            surface,
            (
                privacy_box.x + 40,
                int(y)
            )
        )

        y += 45

    y += 35

    # ========================================================
    # FAQ ITEMS
    # ========================================================

    for index, (question, answer) in enumerate(FAQ_ITEMS):

        # ====================================================
        # QUESTION
        # ====================================================

        question_surface = fonts["date"].render(
            question,
            True,
            FAQ_QUESTION_COLOR
        )

        question_rect = question_surface.get_rect(
            x=privacy_box.x + 40,
            y=int(y)
        )

        # ====================================================
        # SAVE QUESTION RECT
        # ====================================================

        faq_question_rects.append(
            (
                index,
                question_rect
            )
        )

        # ====================================================
        # DRAW QUESTION
        # ====================================================

        screen.blit(
            question_surface,
            question_rect
        )

        y += 50

        # ====================================================
        # ANSWER
        # ====================================================

        if open_faq_index == index:

            answer_lines = answer.split("\n")

            for answer_line in answer_lines:

                answer_surface = fonts["date"].render(
                    answer_line,
                    True,
                    FAQ_ANSWER_COLOR
                )

                answer_rect = answer_surface.get_rect(
                    x=privacy_box.x + 60,
                    y=int(y)
                )

                screen.blit(
                    answer_surface,
                    answer_rect
                )

                y += 45

            # =================================================
            # SPACE AFTER ANSWER
            # =================================================

            y += 20

        else:

            # =================================================
            # SPACE BETWEEN QUESTIONS
            # =================================================

            y += 25

    # ========================================================
    # CONTENT HEIGHT
    # ========================================================

    content_bottom = y


    # ========================================================
    # CONTENT HEIGHT
    # ========================================================

    content_bottom = y + scroll_y

    # ========================================================
    # MAX SCROLL
    # ========================================================

    max_scroll = max(
        0,
        content_bottom
        - privacy_box.bottom
        + 300
    )

    # ========================================================
    # BOTTOM LIMIT
    # ========================================================

    if scroll_y > max_scroll:

        scroll_y = max_scroll
        scroll_velocity = 0
    # ========================================================
    # BOTTOM LIMIT
    # ========================================================

    if scroll_y > max_scroll:

        scroll_y = max_scroll
        scroll_velocity = 0

    # ========================================================
    # REMOVE CLIP
    # ========================================================

    screen.set_clip(None)

# ============================================================
# FAQ EVENT
# ============================================================

def FAQ_event(event):

    global scroll_velocity
    global open_faq_index

    # ========================================================
    # MOUSE WHEEL
    # ========================================================

    if event.type == pygame.MOUSEWHEEL:

        scroll_velocity += event.y * 20

    # ========================================================
    # LEFT CLICK
    # ========================================================

    if event.type == pygame.MOUSEBUTTONDOWN:

        if event.button == 1:

            mouse_pos = event.pos

            # =================================================
            # CHECK QUESTIONS
            # =================================================

            for index, rect in faq_question_rects:

                if rect.collidepoint(mouse_pos):

                    # -----------------------------------------
                    # اگر همین سؤال باز است → ببند
                    # -----------------------------------------

                    if open_faq_index == index:

                        open_faq_index = None

                    # -----------------------------------------
                    # اگر بسته است → باز کن
                    # -----------------------------------------

                    else:

                        open_faq_index = index

                    break


# ============================================================
# RESET FAQ
# ============================================================

def reset_FAQ():

    global scroll_y
    global scroll_velocity
    global open_faq_index
    global faq_question_rects

    scroll_y = 0

    scroll_velocity = 0

    open_faq_index = None

    faq_question_rects = []


# ============================================================
# FAQ SIDE EFFECT
# ============================================================

def draw_FAQ_side_effect(screen, rect):

    # --------------------------------------------------------
    # FAQ BOX
    # --------------------------------------------------------

    privacy_box = pygame.Rect(

        rect.centerx - 440,
        rect.centery - 330,

        870,
        810
    )

    # --------------------------------------------------------
    # DRAW FAQ
    # --------------------------------------------------------

    draw_FAQ(
        screen,
        privacy_box
    )