import pygame
#window
pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("jajame 888")
clock = pygame.time.Clock()
running = True
dot = 10
Rect_1 = pygame.Rect(200, 100, 150, 100)

player_pos = pygame.Vector2(screen.get_width() / 2 , screen.get_height() / 2)

while running:
    #press X to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("Black")

    pygame.draw.circle(screen, "yellow" , player_pos, 20)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= dot
    if keys[pygame.K_s]:
        player_pos.y += dot
    if keys[pygame.K_a]:
        player_pos.x -= dot
    if keys[pygame.K_d]:
        player_pos.x += dot

    # x-axis
    if player_pos.x < 20:
        player_pos.x = 1280
    if player_pos.x > 1280 :
        player_pos.x = 20
    # y-axis
    if player_pos.y < 20:
        player_pos.y = 720
    if player_pos.y > 720:
        player_pos.y = 20

    pygame.draw.rect(screen,"white",Rect_1)

    pygame.display.flip()
     
    clock.tick(60)  # Limit FPS at 60

pygame.quit()
