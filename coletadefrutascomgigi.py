import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Captura de frutas com GIGI")

background_image = pygame.image.load("fundo.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

hamster_image = pygame.image.load("hamster.png")
hamster_image = pygame.transform.scale(hamster_image, (70, 70))

fruta_images = [
    pygame.image.load("pera.png"),
    pygame.image.load("banana.png"),
    pygame.image.load("maca.png"),
    pygame.image.load("uva.png")
]

for i in range(len(fruta_images)):
    fruta_images[i] = pygame.transform.scale(fruta_images[i], (50, 50))

player = pygame.Rect(WIDTH // 2, HEIGHT - 80, 50, 50)
player_speed = 7

frutas = []
fruta_speed = 7
num_frutas = 1 

for _ in range(num_frutas):
    x = random.randint(0, WIDTH - 30)
    y = random.randint(-100, -30) 
    image = random.choice(fruta_images) 
    frutas.append({"rect": pygame.Rect(x, y, 30, 30), "image": image})

score = 0
goal = 10

running = True
while running:
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += player_speed

    for fruta in frutas:
        fruta["rect"].y += fruta_speed 
        if fruta["rect"].y > HEIGHT: 
            fruta["rect"].x = random.randint(0, WIDTH - fruta["rect"].width)
            fruta["rect"].y = random.randint(-100, -30)
            fruta["image"] = random.choice(fruta_images) 

        if player.colliderect(fruta["rect"]):
            score += 1
            fruta["rect"].x = random.randint(0, WIDTH - fruta["rect"].width)
            fruta["rect"].y = random.randint(-100, -30)
            fruta["image"] = random.choice(fruta_images) 

    screen.blit(hamster_image, (player.x, player.y))

    for fruta in frutas:
        screen.blit(fruta["image"], (fruta["rect"].x, fruta["rect"].y))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Frutas: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    if score >= goal:
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()