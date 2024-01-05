# intro.py
import pygame

def display_intro():
    # Initialize Pygame
    pygame.init()

    # Set up some constants
    WIDTH, HEIGHT = 1000, 800

    # Create the window
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    # Load the image
    intro_image = pygame.image.load("assets/images/intro.jpg").convert_alpha()

    # Scale the image to fit the window
    intro_image = pygame.transform.scale(intro_image, (WIDTH, HEIGHT))

    # Display the image
    window.blit(intro_image, (0, 0))
    pygame.display.flip()  # Use flip() instead of update() to update the entire window
    pygame.time.delay(100)  # Small delay to give the window time to update

    # Main delay
    pygame.time.delay(3000)  # Delay for 3 seconds

    # Clear the screen
    window.fill((0, 0, 0))
    pygame.display.flip()

if __name__ == "__main__":
    display_intro()