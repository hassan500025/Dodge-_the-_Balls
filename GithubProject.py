    # Dodge the Balls :
    # Pygame Libarry :
    
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Dodge the Balls')

# Player properties
player_size = 50
player_pos = [screen_width//2, screen_height-2*player_size]
player_speed = 10

# Ball properties
ball_size = 30
ball_pos = [random.randint(0, screen_width-ball_size), 0]
ball_speed = 10

# Score
score = 0

# Clock
clock = pygame.time.Clock()

# Game loop
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < screen_width - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < screen_height - player_size:
        player_pos[1] += player_speed

    screen.fill(black)

    ball_pos[1] += ball_speed
    if ball_pos[1] > screen_height:
        game_over = True  # End the game if the ball reaches the bottom

    if (player_pos[0] < ball_pos[0] < player_pos[0] + player_size or player_pos[0] < ball_pos[0] + ball_size < player_pos[0] + player_size) and \
       (player_pos[1] < ball_pos[1] < player_pos[1] + player_size or player_pos[1] < ball_pos[1] + ball_size < player_pos[1] + player_size):
        score += 1
        ball_pos = [random.randint(0, screen_width-ball_size), 0]

    pygame.draw.rect(screen, white, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.circle(screen, red, (ball_pos[0] + ball_size//2, ball_pos[1] + ball_size//2), ball_size//2)

    font = pygame.font.SysFont(None, 35)
    text = font.render(f"Score: {score}", True, white)
    screen.blit(text, (10, 10))

    pygame.display.flip()

    clock.tick(30)

# Display Game Over message
font = pygame.font.SysFont(None, 75)
text = font.render("Game Over", True, red)
screen.blit(text, (screen_width//2 - text.get_width()//2, screen_height//2 - text.get_height()//2))
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.wait(3000)

pygame.quit()