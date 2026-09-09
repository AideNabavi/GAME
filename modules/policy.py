import pygame
from modules.font import fonts

privacy_text = """
Privacy Policy

==================================================

Last Updated: August 2026


Welcome to Mental Math Challenge.

Your privacy is important to us. This Privacy Policy
explains how we collect, use, protect, and handle
information when you use our game.

By using Mental Math Challenge, you agree to the
terms described in this Privacy Policy.

==================================================


1. Information We Collect

Mental Math Challenge is designed with privacy in mind.

We do not collect personal information such as:

- Full name
- Email address
- Phone number
- Home address
- Exact location
- Personal identification information

The game can store certain data locally on your device
to provide a better experience, including:

• Game progress
• Player profile settings
• Selected language
• Game preferences
• Scores and records
• Achievements and statistics


This information remains stored on your device and is
not transmitted to our servers.


==================================================


2. How We Use Information

The information stored by the game is used only for
improving your personal gaming experience.

This includes:

- Saving your progress
- Keeping your highest scores
- Remembering your settings
- Displaying achievements
- Improving gameplay features


We do not sell, rent, or share your personal
information with third parties.


==================================================


3. Local Data Storage

Mental Math Challenge may use local storage methods
provided by your device.

Local data allows the game to remember:

• Your game settings
• Your progress
• Your records
• Your preferences


You can remove this data at any time by uninstalling
the application or clearing the application data
through your device settings.


==================================================


4. Third-Party Services

Currently, Mental Math Challenge does not use
third-party services that collect personal information.

We do not use:

- Advertising networks
- Tracking services
- Data collection tools


If future updates introduce features such as:

• Online multiplayer
• Cloud saving
• Leaderboards
• Analytics
• Advertisements


this Privacy Policy will be updated to explain how
those services handle information.


==================================================


5. Children's Privacy

Mental Math Challenge is created to be safe and
appropriate for users of all ages.

We do not knowingly collect personal information
from children.

If we discover that personal information has been
collected unintentionally, we will take reasonable
steps to remove such information.


==================================================


6. Data Security

We take reasonable measures to protect information
stored by the game.

However, please understand that no digital storage
system can be guaranteed to be completely secure.

Users should always keep their devices protected
with appropriate security settings.


==================================================


7. Changes to This Privacy Policy

We may update this Privacy Policy from time to time
to reflect changes in the game, new features, or
legal requirements.

Any changes will be shown on this page with an
updated revision date.


==================================================


8. Contact Us

If you have any questions, suggestions, or concerns
about this Privacy Policy, you can contact us:

Email:
nabavi447@gmail.com


Thank you for playing
Mental Math Challenge.

We appreciate your trust and support.

==================================================
"""







scroll_y = 0
scroll_velocity = 0

friction = 0.94


def draw_privacy_policy(screen, privacy_box):

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

    if scroll_y > 8000:
        scroll_y = 8000
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

        text = fonts["more and support"].render(
            line,
            True,
            (60, 60, 60)
        )

        screen.blit(
            text,
            (
                privacy_box.x + 40,
                y
            )
        )

        y += 45

    # ============================================================
    # REMOVE CLIP
    # ============================================================

    screen.set_clip(None)


def privacy_event(event):

    global scroll_velocity

    if event.type == pygame.MOUSEWHEEL:

        scroll_velocity += event.y * 20
    
    
    
    
    
    
    
    
    
    
    
    
    

# ============================================================
# PRIVACY POLICY 
# ============================================================

def draw_privacy_side_effect(screen, rect):

    # ------------------------------------------------------------
    # Privacy box نسبت به خود پنجره
    # ------------------------------------------------------------

    privacy_box = pygame.Rect(

        rect.centerx - 370,
        rect.centery - 275,

        740,
        550
    )

    # ------------------------------------------------------------
    # Draw Privacy Policy
    # ------------------------------------------------------------

    draw_privacy_policy(
        screen,
        privacy_box
    )
