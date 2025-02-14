import pygame #importing pygame
import random  #For random relocation

class Enemy: #enemy class to represent enemy in the game

    def __init__(self, x, y, colour, radius, speed_x, speed_y): #class constructer, initializes the object’s attributes based on parameters
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__colour = colour
        self.__speed_x = speed_x
        self.__speed_y = speed_y

        '''
        reason for instance vaiables and not class variables 
        better for each enemy instance to have its own values for x, y and radius as enemy will have his own unique position
        and size on the screen
        class variables  would have all instances of enemy sharing the same position and size
        the same goes for the colour and speed of enemy, instance is needed to maintain independnece for other enemy objects 

        defense for the parameters
        x and y neccesary for position of the enemy on the x and y axis, radius needed to specify size of the enemy 
        colour needed to specify what colour the enemy will be 
        speed of x and y neccesary for the speed of the enemy on both axis 

        '''
    
    def draw(self, display): #method to draw the enemy to the screen
        pygame.draw.circle(display, self.__colour, [self.__x, self.__y], self.__radius) #draws a circle with the specified color, position and radius on the display 

    def move(self, direction, display_width=None, display_height=None): #move the enemy in specified direction
        #direction is up, down, left, right and width and height to ensure enemy comes back at opposite of display if he comes out of it

        if direction == "DOWN": 
            self.__y += self.__speed_y #moving enemy down
            if self.__y > display_height + self.__radius: #come back to top if it leaves bottom of screen
                self.__y = -self.__radius 
        elif direction == "UP":
            self.__y -= self.__speed_y #moving enemy up
            if self.__y < -self.__radius: #come back to bottom if it top bottom of screen
                self.__y = display_height + self.__radius
        elif direction == "LEFT": #moving enemy left
            self.__x -= self.__speed_x #come back to right if it leaves left of screen 
            if self.__x < -self.__radius:
                self.__x = display_width + self.__radius
        elif direction == "RIGHT": #moving enemy right
            self.__x += self.__speed_x #come back to left if it leaves right of screen 
            if self.__x > display_width + self.__radius:
                self.__x = -self.__radius

    def relocate(self, display_width, display_height): #Relocate the enemy to a random position
        new_x = random.randint(self.__radius, display_width - self.__radius) #random x position 
        new_y = random.randint(self.__radius, display_height - self.__radius) #random y position 
        self.set_position(new_x, new_y) #update the position 

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
    
    def get_radius(self):
        return self.__radius
    
    '''
    the above getters allow the access to the private attributes of the enemy class
    x refers to x axis, y refers to y axis and so on
    '''

    def set_position(self, x, y):
        self.__x = x
        self.__y = y

        #the above refers to the setter method 
        #set the values of the private attributes in the enemy class
    
    def get_rect(self):  #method to return a rectangle used for collision detection
        return pygame.Rect(self.__x - self.__radius, self.__y - self.__radius, self.__radius * 2, self.__radius * 2)
    #calculates the edges and width and height of the rectangle, *2 allows for the detection of the collision 

    def __str__(self):
        return f"Enemy(Position: ({self.__x}, {self.__y}), Colour: {self.__colour})"
    #this string method allows the colour and coorindates to be printed to the screen when called in main.py



    
