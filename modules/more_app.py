import pygame
from modules.font import fonts

privacy_text = """
How To play

________________________________________________________

Last Updated: September 2026


Welcome to Mental Math Challenge.

Your privacy is important to us. This Privacy Policy
explains how information is stored and handled in the
current version of our game.

The current version of Mental Math Challenge is an
offline game and does not require an online account.


________________________________________________________


1. Information We Collect

The current version of Mental Math Challenge stores
only limited profile information locally on your device.

This may include:

• Username
• Selected avatar
• Selected country flag

This information is used to display and personalize
your player profile inside the game.


The current offline version does not require or collect:

• Email address
• Password
• Phone number
• Home address
• Exact location
• Payment information


________________________________________________________


2. Local Game Data

The game may store certain information locally on
your device to provide its features.

This may include:

• Game progress
• Scores and records
• Achievements and statistics
• Game settings
• Language preferences
• Player profile settings
• Username
• Avatar
• Country flag


This information is stored locally on your device.


________________________________________________________


3. Offline Version

Mental Math Challenge is currently designed to work
as an offline game.

The current version does not provide:

• Online accounts
• Online multiplayer
• Cloud saves
• Online profiles
• Online leaderboards


An email address or password is not required to play
the current offline version.


________________________________________________________


4. Future Online Features

Future versions may introduce online features.

These features may include:

• Online accounts
• Email addresses
• Passwords
• Online multiplayer
• Cloud saves
• Online leaderboards
• Social features


If online features are introduced, this Privacy Policy
will be updated to explain what information is required
and how that information is handled.


________________________________________________________


5. Third-Party Services

The current offline version does not use third-party
services for:

• Advertising
• User tracking
• Analytics
• Online account management


If future versions use third-party services, this
Privacy Policy will be updated accordingly.


________________________________________________________


6. Children's Privacy

Mental Math Challenge is designed to be appropriate
for users of all ages.

The current offline version does not require users
to provide an email address or password.

We do not knowingly collect personal information
from children through the current offline version.


________________________________________________________


7. Data Security

We take reasonable measures to protect information
stored by the game.

However, no digital storage system can be guaranteed
to be completely secure.

Users should keep their devices protected with
appropriate security settings.


________________________________________________________


8. Data Deletion

You can remove locally stored game and profile data
by deleting the game's local data or uninstalling
the application.

Deleting local data may remove:

• Game progress
• Scores and records
• Settings
• Username
• Avatar
• Country flag


________________________________________________________


9. Changes to This Privacy Policy

We may update this Privacy Policy when the game
receives new features or when required by law.

If online features are introduced in a future version,
this Privacy Policy will be updated accordingly.

The Last Updated date will be changed whenever
this Privacy Policy is revised.


________________________________________________________


10. Contact Us

If you have questions or concerns about this Privacy
Policy, you can contact us:

Email:
nabavi447@gmail.com


Providing an email address is not required to play
the current offline version of Mental Math Challenge.


________________________________________________________
"""


PRIVACY_TITLE_COLOR = (60, 60, 60)
PRIVACY_DATE_COLOR = (120, 80, 40)
PRIVACY_SECTION_COLOR = (120, 80, 40)

PRIVACY_TEXT_COLOR = (60, 60, 60)

import re



scroll_y = 0
scroll_velocity = 0

friction = 0.94


def draw_how_to_play(screen, privacy_box):

    global scroll_y
    global scroll_velocity

    # ============================================================
    # SCROLL
    # ============================================================

    scroll_y += scroll_velocity

    scroll_velocity *= friction

    if abs(scroll_velocity) < 0.1:
        scroll_velocity = 0

    # ============================================================
    # LIMIT
    # ============================================================

    if scroll_y < 0:
        scroll_y = 0
        scroll_velocity = 0

    if scroll_y > 9000:
        scroll_y = 9000
        scroll_velocity = 0

    # ============================================================
    # CLIP
    # ============================================================

    screen.set_clip(privacy_box)

    # ============================================================
    # TEXT
    # ============================================================

    y = privacy_box.y + 40 - scroll_y

    for line in privacy_text.split("\n"):

        stripped_line = line.strip()

        # ========================================================
        # MAIN TITLE
        # ========================================================

        if stripped_line == "Privacy Policy":

            text = fonts["TITLE_NEW"].render(
                line,
                True,
                PRIVACY_TITLE_COLOR
            )

            line_height = 60

        # ========================================================
        # LAST UPDATED
        # ========================================================

        elif stripped_line.startswith("Last Updated:"):

            text = fonts["TITLE_NEW"].render(
                line,
                True,
                PRIVACY_DATE_COLOR
            )

            line_height = 50

        # ========================================================
        # SECTION TITLES
        # 1. / 2. / 3. / ... / 10.
        # ========================================================

        elif re.match(r"^\d+\.\s", stripped_line):

            text = fonts["date"].render(
                line,
                True,
                PRIVACY_SECTION_COLOR
            )

            line_height = 50

        # ========================================================
        # NORMAL TEXT
        # ========================================================

        else:

            text = fonts["date"].render(
                line,
                True,
                PRIVACY_TEXT_COLOR
            )

            line_height = 45

        # ========================================================
        # DRAW
        # ========================================================

        screen.blit(
            text,
            (
                privacy_box.x + 40,
                y
            )
        )

        y += line_height

    # ============================================================
    # REMOVE CLIP
    # ============================================================

    screen.set_clip(None)


def how_to_play_event(event):

    global scroll_velocity

    if event.type == pygame.MOUSEWHEEL:

        scroll_velocity += event.y * 20
    
    
    
    
    
    
    
    
    
    
    
    
    

# ============================================================
# PRIVACY POLICY 
# ============================================================

def draw_how_to_play_side_effect(screen, rect):

    # ------------------------------------------------------------
    # Privacy box نسبت به خود پنجره
    # ------------------------------------------------------------

    privacy_box = pygame.Rect(

        rect.centerx - 440,
        rect.centery - 330,

        1000,
        810
    )

    # ------------------------------------------------------------
    # Draw Privacy Policy
    # ------------------------------------------------------------

    draw_how_to_play(
        screen,
        privacy_box
    )
