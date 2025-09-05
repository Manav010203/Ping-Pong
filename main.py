import pygame
from strikers import Striker
from balls import Ball
from constants import *
pygame.init()
font20 = pygame.font.Font('freesansbold.ttf',20)
pygame.display.set_caption("Reset Button Example")

screen = pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption("PING PONG")
reset_button = pygame.Rect(250, 150, 100, 50) # x, y, width, height
clock = pygame.time.Clock()
def draw_button(screen, rect, text):
    """Draws a button with text on the screen."""
    pygame.draw.rect(screen, GREEN, rect, border_radius=10)
    font20 = pygame.font.Font('freesansbold.ttf', 20)
    text_surface = font20.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def main():
    """Main game loop."""
    pygame.init()
    screen = pygame.display.set_mode((WIDHT, HEIGHT))
    pygame.display.set_caption("Ping Pong")
    clock = pygame.time.Clock()
    
    # Initialize game objects
    geek1 = Striker(20, HEIGHT // 2 - 50, 10, 100, 10, GREEN)
    geek2 = Striker(WIDHT - 30, HEIGHT // 2 - 50, 10, 100, 10, GREEN)
    ball = Ball(WIDHT // 2, HEIGHT // 2, 7, 7, WHITE)
    
    # Game state variables
    geek1score, geek2score = 0, 0
    geek1YFAC, geek2YFAC = 0, 0
    ball_active = True
    running = True

    # Define the reset button
    reset_button = pygame.Rect(WIDHT // 2 - 50, HEIGHT // 2 + 100, 100, 50)

    while running:
        screen.fill(BLACK)
        
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Key presses for striker movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    geek2YFAC = -1
                if event.key == pygame.K_DOWN:
                    geek2YFAC = 1
                if event.key == pygame.K_w:
                    geek1YFAC = -1
                if event.key == pygame.K_s:
                    geek1YFAC = 1
            
            # Key releases to stop striker movement
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    geek2YFAC = 0
                if event.key in [pygame.K_w, pygame.K_s]:
                    geek1YFAC = 0
            
            # Mouse click for the reset button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_button.collidepoint(event.pos):
                    # Reset the scores and the ball position for a new game
                    geek1score, geek2score = 0, 0
                    ball.reset()
                    ball_active = True
        
        # --- Game Logic ---
        geek1.update(geek1YFAC)
        geek2.update(geek2YFAC)

        if ball_active:
            # Check for collision with strikers
            if pygame.Rect.colliderect(ball.getRect(), geek1.getRect()):
                ball.hit()
            if pygame.Rect.colliderect(ball.getRect(), geek2.getRect()):
                ball.hit()
            
            # Update ball position and check for a score
            point = ball.update()
            if point == 1:
                geek2score += 1
                ball.reset() # ✅ Automatically reset the ball to continue the game
            elif point == -1:
                geek1score += 1
                ball.reset() # ✅ Automatically reset the ball to continue the game
        
        # --- Drawing ---
        geek1.display()
        geek2.display()
        
        # Only draw the ball if it's active
        if ball_active:
            ball.display()

        # Display scores
        geek1.displayscore("Player 1: ", geek1score, 100, 20, WHITE)
        geek2.displayscore("Player 2: ", geek2score, WIDHT - 100, 20, WHITE)

        # Draw the button
        draw_button(screen, reset_button, "Reset Game")
        
        # Update the full display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
