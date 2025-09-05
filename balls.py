import random
from constants import *
class Ball:
    """Represents the ball in the game."""
    def __init__(self, x, y, radius, speed, color):
        """Initializes the ball with position, radius, speed, and color."""
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.color = color
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)
        self.x_fac = random.choice([1, -1])  # Initial horizontal direction
        self.y_fac = random.choice([1, -1])  # Initial vertical direction

    def update(self):
        """Moves the ball and handles collisions with walls, returning a score point if a player scores."""
        self.x += self.x_fac * self.speed
        self.y += self.y_fac * self.speed
        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius
        
        # Check for collision with top/bottom walls
        if self.y <= self.radius or self.y >= HEIGHT - self.radius:
            self.y_fac *= -1

        # Check for scoring (left/right walls)
        if self.x <= self.radius:
            return 1  # Player 2 scores
        if self.x >= WIDHT - self.radius:
            return -1 # Player 1 scores

        return 0 # No point scored yet

    def hit(self):
        """Reverses the ball's horizontal direction after hitting a striker."""
        self.x_fac *= -1

    def reset(self):
        """Resets the ball to the center of the screen with a new random direction."""
        self.x = WIDHT // 2
        self.y = HEIGHT // 2
        self.x_fac = random.choice([1, -1])
        self.y_fac = random.choice([1, -1])

    def display(self):
        """Draws the ball on the screen."""
        pygame.draw.circle(pygame.display.get_surface(), self.color, (self.x, self.y), self.radius)

    def getRect(self):
        """Returns the pygame.Rect object for collision detection."""
        return self.rect
