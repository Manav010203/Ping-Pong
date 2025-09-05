import pygame
from constants import *
# from main import font20
pygame.init()
font20 = pygame.font.Font('freesansbold.ttf',20)
class Striker:
    """Represents a player's paddle."""
    def __init__(self, x, y, width, height, speed, color):
        """Initializes a striker with position, size, speed, and color."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, direction):
        """Moves the striker up or down within the screen boundaries."""
        self.y += direction * self.speed
        # Keep the striker within the screen height
        if self.y <= 0:
            self.y = 0
        if self.y + self.height >= HEIGHT:
            self.y = HEIGHT - self.height
        self.rect.y = self.y

    def display(self):
        """Draws the striker on the screen."""
        pygame.draw.rect(pygame.display.get_surface(), self.color, self.rect)

    def getRect(self):
        """Returns the pygame.Rect object for collision detection."""
        return self.rect
    
    def displayscore(self, text, score, x, y, color):
        """Displays the player's score on the screen."""
        font = pygame.font.Font('freesansbold.ttf', 20)
        score_text = font.render(f"{text}{score}", True, color)
        score_rect = score_text.get_rect()
        score_rect.center = (x, y)
        pygame.display.get_surface().blit(score_text, score_rect)
