import pygame #import pygame
from food import Food #import food class
from enemy import Enemy #import enemy class
from pacman import Pacman  #Import the Pacman class

'''
event driven programming in pygame 
Pygame uses an event loop to handle user inputs and interactions and instead of running in a sequence, 
the game listens for "events" such as key presses or collisions and reacts to them
in my game its applied by:
`pygame.event.get()` loop checks for user inputs, such as quitting the game
pygame.key.get_pressed()` detects which arrow keys are pressed and moves Pacman
Collisions between objects (Pacman, Enemy, and Food) trigger specific events, like resetting positions
The enemy automatically moves towards the Food based on its position, without direct user control
'''

#Initialize pygame
pygame.init()

#Display setup
DISPLAY_WIDTH = 400
DISPLAY_HEIGHT = 400
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

#Colors
display_colour = [25, 25, 25]
pacman_colour = [255, 255, 0]  #Yellow for Pacman
enemy_colour = [0, 0, 255]  #Blue for Enemy

#Pacman setup
pacman = Pacman(x=100, y=200, colour=pacman_colour, radius=10, speed=3)

#Enemy setup
enemy = Enemy(x=150, y=150, colour=enemy_colour, radius=7, speed_x=1.2, speed_y=1.2)

#Food setup
food = Food(x=DISPLAY_WIDTH // 2, y=DISPLAY_HEIGHT // 2)

clock = pygame.time.Clock()
run_game = True

print(pacman) 
print(enemy)
print(food)
#prints the string reps to screen with colour and coorindates 

while run_game:
    display.fill(display_colour)  #Fill the screen with the background color

    #Draw elements to the display
    pacman.draw(display)
    enemy.draw(display)
    food.draw(display)

    #Event handling
    keys = pygame.key.get_pressed()

    #Move Pacman based on key input (arrows on keyboard)
    if keys[pygame.K_LEFT]: #if key is pressed
        pacman.move_left(DISPLAY_WIDTH) #pac man moves left with left key
    elif keys[pygame.K_RIGHT]:
        pacman.move_right(DISPLAY_WIDTH)
    elif keys[pygame.K_UP]:
        pacman.move_up(DISPLAY_HEIGHT)
    elif keys[pygame.K_DOWN]:
        pacman.move_down(DISPLAY_HEIGHT)
    #ending the game loop when game is quit 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

    #Enemy- Move towards the food
    if enemy.get_x() < food.get_x():
        enemy.move("RIGHT", DISPLAY_WIDTH, DISPLAY_HEIGHT)
    elif enemy.get_x() > food.get_x():
        enemy.move("LEFT", DISPLAY_WIDTH, DISPLAY_HEIGHT)
    if enemy.get_y() < food.get_y():
        enemy.move("DOWN", DISPLAY_WIDTH, DISPLAY_HEIGHT)
    elif enemy.get_y() > food.get_y():
        enemy.move("UP", DISPLAY_WIDTH, DISPLAY_HEIGHT)

        '''
        enemy moves in the way that the food is on the x or y axis 
        can move up down left or right 

        '''

    #Collision Detection
    if pacman.get_rect().colliderect(food.get_rect()):  #Pacman eats food
        food.relocate(DISPLAY_WIDTH, DISPLAY_HEIGHT) #food relocates 
        pacman.set_position(100, 200)  #Reset Pacman position

    if enemy.get_rect().colliderect(food.get_rect()):  #Enemy eats food
        food.relocate(DISPLAY_WIDTH, DISPLAY_HEIGHT) #food relocates
        enemy.set_position(150, 150)  #Reset enemy position

    if pacman.get_rect().colliderect(enemy.get_rect()):  #Enemy collides with Pacman
         pacman.set_position(100, 200) #reset pacmans position
         enemy.set_position(150, 150) #reset enemys position 

    #Update the display after drawing everything
    pygame.display.update()

    #Controlling the frame rate
    clock.tick(60)

pygame.quit()








