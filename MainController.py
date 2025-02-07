import pygame

COLOR_CHANGE_EVENT = pygame.USEREVENT + 1

class MainController:
    
    def __init__(self, model):
        self.model = model
        # makes a map of keys pressed and what direction it should take you.
        self.key_map = {
            pygame.K_w: "UP",
            pygame.K_s: "DOWN",
            pygame.K_a: "LEFT",
            pygame.K_d: "RIGHT"
        }

        self.holding_click = False
        self.holding_click_sign = 1
        # pygame.time.set_timer(COLOR_CHANGE_EVENT, 500)  # Fire event every 500ms (30 ticks @ 60 FPS)

        
    def ControllerTick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 3:  # press left or right click
                    self.holding_click = True
                    if event.button == 1: 
                        self.sign = 1
                    else:
                        self.sign = -1
            elif event.type == pygame.MOUSEBUTTONUP:  # release left or right click
                if event.button == 1 or event.button == 3:
                    self.holding_click = False
        
        self.handle_keyboard()
        self.handle_mouse()
        return True
    
    def handle_keyboard(self):
        """Handles keyboard input for moving the player rectangle."""
        keys = pygame.key.get_pressed()

        directions = []

        for key, direction in self.key_map.items():
            if keys[key]:
                directions.append(direction)
                
         # Reset size when SPACE is pressed
        if keys[pygame.K_SPACE]:
            self.model.reset_size()

        self.model.move_player(directions)
    def handle_mouse(self):
        if self.holding_click:
            self.model.change_size(self.sign)

        
