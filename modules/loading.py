import pygame
import time


        
        
        
        
       

class LoadingManager:

    def __init__(self, screen):

        self.screen = screen

        self.width, self.height = screen.get_size()

        self.tasks = []

        self.total = 0

        # -------------------------
        # Background
        # -------------------------

        background = pygame.image.load(
            "asset/image/loadd.png"
        ).convert_alpha()

        self.background = pygame.transform.smoothscale(
            background,
            (
                self.width,
                self.height
            )
        )
        # -------------------------
        # Loading Image
        # -------------------------

        image = pygame.transform.smoothscale(pygame.image.load(
            "asset/image/icon.png"),(20,20)
        ).convert_alpha()

        self.loading_image = image


        # -------------------------
        # Music
        # -------------------------

        pygame.mixer.music.load(
            "asset/image/loading.mp3"
        )
        pygame.mixer.music.set_volume(0.01)

    # ==================================================
    # Add
    # ==================================================

    def add(self, function):

        self.tasks.append(
            function
        )

        self.total = len(
            self.tasks
        )


    # ==================================================
    # Draw
    # ==================================================

    def draw(self, progress):

        # -------------------------
        # Background
        # -------------------------

        self.screen.blit(
            self.background,
            (0, 0)
        )


        # -------------------------
        # Loading Bar
        # -------------------------

        bar_width = int(
            self.width * 0.45
        )

        bar_height = 20

        bar_x = (
            self.width - bar_width
        ) // 2

        bar_y = (
            self.height * 0.85
        )


        # -------------------------
        # Bar Background
        # -------------------------

        pygame.draw.rect(
            self.screen,
            (60, 60, 60),
            (
                bar_x,
                int(bar_y),
                bar_width,
                bar_height
            ),
            border_radius=10
        )


        # -------------------------
        # Progress
        # -------------------------

        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            (
                bar_x,
                int(bar_y),
                int(
                    bar_width * progress
                ),
                bar_height
            ),
            border_radius=10
        )
        # -------------------------
        # Loading Image
        # -------------------------

        image_rect = self.loading_image.get_rect(
            center=(
                self.width // 2,
                self.height // 2
            )
        )

        self.screen.blit(
            self.loading_image,
            image_rect
        )

        pygame.display.flip()


    # ==================================================
    # Run
    # ==================================================

    def run(self):

        if self.total == 0:

            return


        for index, function in enumerate(
            self.tasks
        ):

            # -------------------------
            # Events
            # -------------------------

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()

                    raise SystemExit


            # -------------------------
            # Before Task
            # -------------------------

            progress = (
                index / self.total
            )

            self.draw(
                progress
            )


            # -------------------------
            # Run Task
            # -------------------------

            function()


            # -------------------------
            # After Task
            # -------------------------

            progress = (
                (index + 1)
                / self.total
            )

            self.draw(
                progress
            )


            # -------------------------
            # Small Delay
            # -------------------------

            pygame.time.delay(
                20
            )
     
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
import importlib
   
loader=None

def LOADING(screen):
    global loader
    loader = LoadingManager(
        screen
    )
    # ==================================================
    # Add Modules
    # ==================================================
    loader.add(
        lambda: importlib.import_module(
            "event_handler"
        )
    )

    loader.add(
        lambda: importlib.import_module(
            "modules.time_screen"
        )
    )

    loader.add(
        lambda: importlib.import_module(
            "modules.game_engine"
        )
    )

    loader.add(
        lambda: importlib.import_module(
            "modules.timer"
        )
    )



    loader.add(
        lambda: importlib.import_module(
            "modules.button"
        )
    )


    loader.add(
        lambda: importlib.import_module(
            "modules.design"
        )
    )

    loader.add(
        lambda: importlib.import_module(
            "modules.language"
        )
    )

    loader.add(
        lambda: importlib.import_module(
            "modules.sound"
        )
    )

    loader.add(
        lambda: importlib.import_module(
            "modules.font"
        )
    )

    loader.add(
        lambda: importlib.import_module(
            "modules.ACCOUNT.player_profile"
        )
    )

    loader.add(
        lambda: importlib.import_module(
            "modules.screen"
        )
    )




    loader.add(
        lambda: importlib.import_module(
            "modules.ceill_screen"
        )
    )

    loader.add(
        lambda: importlib.import_module(
            "modules.ACCOUNT.profile_"
        )
    )

    loader.add(
        lambda: importlib.import_module(
            "modules.mode"
        )
    )

    loader.add(
        lambda: importlib.import_module(
            "modules.SUPPORT.support"
        )
    )

    loader.add(
        lambda: importlib.import_module(
            "modules.MORE.more"
        )
    )

    loader.add(
        lambda: importlib.import_module(
            "modules.GAMES.FIND_NUMBER"
        )
    )

    loader.add(
        lambda: importlib.import_module(
            "modules.GAMES.MEMORY"
        )
    )

    loader.add(
        lambda: importlib.import_module(
            "modules.GAMES.REPEAT_AFTER_ME"
        )
    )

    loader.add(
        lambda: importlib.import_module(
            "modules.GAMES.MORE_LESS_EQUAL"
        )
    )

    loader.run()
