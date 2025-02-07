import pygame
# import random

class MainModel(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        
        # Load character sprite
        self.original_image = pygame.image.load(image_path)  # Store the original image
        self.current_scaled_image = pygame.transform.scale(self.original_image, (50, 50))  # Keep track of the scaled image
        self.image = self.current_scaled_image  # Default size



        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 250
        self.speed = 5

        # self.color = (0, 255, 0)  # Initial color (Green)
        self.flip = False
        self.direction = None
        self.max_size = 500 
        self.min_size = 10

    def move_player(self, directions):
    # Updates position and direction based on movement.
        dx, dy = 0, 0

        if "LEFT" in directions:
            dx = -1
            self.flip = True
        if "RIGHT" in directions:
            dx = 1
            self.flip = False
        if "UP" in directions:
            dy = -1
        if "DOWN" in directions:
            dy = 1

        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            dx *= 0.707  # 1/sqrt(2)
            dy *= 0.707

        # Update position
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

        # Update direction if moving
        if directions:
            self.direction = directions[-1]  # Last key pressed is priority

        # Apply color based on direction
        # self.set_color_by_direction()

        # flip sprite if needed
        self.flip_sprite()


    def set_color_by_direction(self):
        if self.direction == "LEFT":
            self.color = (0, 0, 255)  # Blue for left
        elif self.direction == "RIGHT":
            self.color = (255, 0, 0)  # Red for right
        elif self.direction == "UP":
            self.color = (0, 255, 0)  # Green for up
        elif self.direction == "DOWN":
            self.color = (255, 255, 0)  # Yellow for down
    
    def flip_sprite(self):
        """Flips the sprite horizontally when moving left."""
        if self.flip:
            self.image = pygame.transform.flip(self.current_scaled_image, True, False)
        else:
            self.image = self.current_scaled_image  # Reset to normal when not moving left


    def change_size(self, sign):
        """Increase the size of the rectangle on left-click."""
        new_width = self.rect.width + (sign * 2)
        new_height = self.rect.height + (sign * 2)

        # Prevent shrinking below a minimum size
        if self.min_size <= new_width <= self.max_size:
        # Scale the currently displayed image (not the original)
            self.current_scaled_image = pygame.transform.scale(self.original_image, (new_width, new_height))

            # Maintain the flip state
            if self.direction == "LEFT":
                self.image = pygame.transform.flip(self.current_scaled_image, True, False)
            else:
                self.image = self.current_scaled_image

            # Update rect while keeping the center position
            self.rect = self.image.get_rect(center=self.rect.center)
    
    def reset_size(self):
        """Resets the character sprite to its original size while keeping its direction."""
        default_size = (50, 50)  # Reset to default 50x50 size

        # Scale back to the original size
        self.current_scaled_image = pygame.transform.scale(self.original_image, default_size)

        # Maintain the last facing direction
        self.flip_sprite()

        # Update rect while keeping the center position
        self.rect = self.image.get_rect(center=self.rect.center)
            