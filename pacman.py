import pygame #impoting pygame
import random  #To generate random positions on the pygame window for the elements

class Pacman: #making a pacman class, to represent an instance of pacman for the main game loop
    def __init__(self, x, y, colour, radius, speed): #class constructer, initializes the object’s attributes based on parameters
        self.__x = x #position of pacman on the x axis, __ to show private attribute (same applies for the rest of them)
        self.__y = y #position of pacman on the y axis
        self.__colour = colour #colour of pacman
        self.__radius = radius #size of pacman (his radius when hes on screen)
        self.__speed = speed #how fast pacman will move

        '''
        reason for instance vaiables and not class variables 
        better for each pacman instance to have its own values for x, y and radius as pacman will have his own unique position
        and size on the screen
        class variables  would have all instances of Pacman sharing the same position and size
        the same goes for the colour and speed of pacman, instance is needed to maintain independnece for other pacman objects 

        defense for the parameters written next to them 

        '''

    #Getter methods
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_colour(self):
        return self.__colour

    def get_radius(self):
        return self.__radius

    def get_speed(self):
        return self.__speed
    
    #all of the above getter methods is what allows the access to the private attributes of the pacman class
    #each getter displayed above refers to the attributes in the code above, eg def get_colour(self) is reffering to the colour of pacman and so on

    #Setter methods
    def set_position(self, x, y):
        self.__x = x
        self.__y = y

    def set_speed(self, speed):
        self.__speed = speed

    def set_colour(self, colour):
        self.__colour = colour

    #the setter methods above set the values of the private attributes in the pacman class
    #setters allow us to update pacman while still allowing private attributes 
    #the above setters allow us to modify what they list, eg the position, speed and colour 

    
    def __str__(self):
        return f"Pacman(Colour={self.__colour}, Coordinates=({self.__x}, {self.__y}))"
    
    #this string method allows the colour and coorindates to be printed to the screen when called in main.py

    def move_left(self, display_width): #this method allows for pacman to move left
        self.__x -= self.__speed #subtratcs self.__speed from self.__x to allow pacman to move left
        if self.__x + self.__radius < 0: #this line accounts for if pacman moves off the left side of the screen
            self.__x = display_width + self.__radius #he will reappear at the  right side of the screen

    def move_right(self, display_width): #this method allows for pacman to move right
        self.__x += self.__speed #adds self.__speed from self.__x to allow pacman to move right
        if self.__x - self.__radius > display_width:  #this line accounts for if pacman moves off the right side of the screen
            self.__x = -self.__radius #he will reappear at the left side of the screen

    def move_up(self, display_height): #this method allows for pacman to move up
        self.__y -= self.__speed #subtratcs self.__speed from self.__y to allow pacman to move up
        if self.__y + self.__radius < 0:  #this line accounts for if pacman moves off the top side of the screen
            self.__y = display_height + self.__radius #he will reappear at the bottom
 
    def move_down(self, display_height): #this method allows for pacman to move down
        self.__y += self.__speed #adds self.__speed from self.__y to allow pacman to move down
        if self.__y - self.__radius > display_height:  #this line accounts for if pacman moves off the bottom side of the screen
            self.__y = -self.__radius #he will reappear at the top

    def relocate(self, display_width, display_height): #relocate method allows for pacman to be randomly relocated within the bounds of the screen
        self.__x = random.randint(self.__radius, display_width - self.__radius)
        self.__y = random.randint(self.__radius, display_height - self.__radius)
      #above lines allow for a random number to be generated between the radius and the display_width and height - radius
      #pacman will relocate and not go off screen

    def draw(self, display): #method to draw pacman to the game display window
        pygame.draw.circle(display, self.__colour, (self.__x, self.__y), self.__radius) 
        #draws a circle with the specified color, position and radius on the display 

    def get_rect(self): #method to return a rectangle used for collision detection
        return pygame.Rect(self.__x - self.__radius, self.__y - self.__radius, self.__radius * 2, self.__radius * 2)
    #calculates the edges and width and height of the rectangle, *2 allows for the detection of the collision 

   








