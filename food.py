import pygame #importing pygame
import random #For random relocation

class Food: #food class to represent food in the game

    def __init__(self, x, y, colour=[255, 255, 200]): #class constructer, initializes the object’s attributes based on parameters
        self.__x = x 
        self.__y = y
        self.__colour = colour
        self.__width = 15  #Width of the food
        self.__height = 15  #Height of the food

        '''

        reason for instance vaiables and not class variables 
        better for food instance to have its own values for x, y and width and height as food will have his own unique position
        and size on the screen
        class variables  would have all instances of food sharing the same position and size
        the same goes for the colour, instance is needed to maintain independnece for other food objects
        class variable would be useful only if all food objects must have the same color and size

        defense for the parameters
        x and y neccesary for position of the food on the x and y axis, width and height needed to specify width and height of food
        colour needed to specify what colour food enemy will be 
        '''

    def __str__(self): #String representation of the food object
        return f"Food(Position: ({self.__x}, {self.__y}), Colour: {self.__colour})"
     #this string method allows the colour and coorindates to be printed to the screen when called in main.py

    def draw(self, display): #Draw the food on the screen
        pygame.draw.rect(display, self.__colour, [self.__x, self.__y, self.__width, self.__height]) #draws a rectangle with the specified color, position and size on the display

    def relocate(self, max_width, max_height): #Relocate food to a random position
        self.__x = random.randint(0, max_width - self.__width)  #random x position
        self.__y = random.randint(0, max_height - self.__height) #random y position

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_size(self):
        return [self.__width, self.__height]
    
    '''
    the above getters allow the access to the private attributes of the food class
    x refers to x axis, y refers to y axis and so on
    '''

    def get_rect(self): #Get the rectangle for collision detection
        return pygame.Rect(self.__x, self.__y, self.__width, self.__height)




