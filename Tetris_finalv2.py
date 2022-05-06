import pygame
import random
import copy
import numpy as np
# from Nnet import Nnet
from defs import *
colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]

class FigureType0: #Figure 0(Straight piece)
    type = [[1, 5, 9, 13], [4, 5, 6, 7]]
    orientation = 0
    figure_shape = 0
    def __init__(self):
        self.orientation = random.randint(0, len(self.type)-1)
    def get_type(self):
        return self.type[self.orientation]

    def set_type(self, value):
        self.orientation = value
        return self.type[self.orientation]

    def rotate(self):
        self.orientation = (self.orientation + 1) % len(self.type)

class FigureType1:  #Figure 1
    #type = [[4, 5, 9, 10], [2, 6, 5, 9], [6, 7, 9, 10], [1, 5, 6, 10]]
    type = [[4,5,9,10], [9,5,6,2], [9, 10, 6, 7], [1,5,6,10]]
    orientation = 0
    figure_shape = 1
    def __init__(self):
        self.orientation = random.randint(0, len(self.type)-1)
    def get_type(self):
        return self.type[self.orientation]
    def set_type(self, value):
        #self.type[value]
        self.orientation = value
        
        return self.type[self.orientation]
    def rotate(self):
        self.orientation = (self.orientation + 1) % len(self.type)

class FigureType2:  #Figure 2(L piece)
    #type = [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]]
    type = [[5,9,1,2], [4,0,5,6],[8,9,5,1],[10,4,5,6]]
    orientation = 0
    figure_shape = 2
    def __init__(self):
        self.orientation = random.randint(0, len(self.type)-1)
    def get_type(self):
        return self.type[self.orientation]
    def set_type(self, value):
        #self.type[value]
        self.orientation = value
        
        return self.type[self.orientation]
    def rotate(self):
        self.orientation = (self.orientation + 1) % len(self.type)

class FigureType3:  #Figure 3(L piece)
    #type = [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]]
    type = [[10,6,2,1],[9,5,6,7],[10,11,6,2],[5,6,7,3]]
    orientation = 0
    figure_shape = 3
    def __init__(self):
        self.orientation = random.randint(0, len(self.type)-1)
    def get_type(self):
        return self.type[self.orientation]
    def set_type(self, value):
        #self.type[value]
        self.orientation = value
        
        return self.type[self.orientation]
    def rotate(self):
        self.orientation = (self.orientation + 1) % len(self.type)

class FigureType4:  #Figure 4 T-piece
    #type = [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]]
    type = [[4,5,1,6],[4,5,9,1],[4,5,6,9],[9,5,6,1]]
    orientation = 0
    figure_shape = 4
    def __init__(self):
        self.orientation = random.randint(0, len(self.type)-1)
    def get_type(self):
        return self.type[self.orientation]
    def set_type(self, value):
        #self.type[value]
        self.orientation = value
       
        return self.type[self.orientation]
    def rotate(self):
        #self.orientation = random.randint(0, len(self.type)-1)
        self.orientation = (self.orientation + 1) % len(self.type)
    
class FigureType5:   #Figure 5 Block Piece
    type = [[1, 2, 5, 6]]
    orientation = 0
    figure_shape = 5
    def __init__(self):
        self.orientation = 0
    def get_type(self):
        return self.type[self.orientation]
    def set_type(self, value):
        #self.type[value]
        self.orientation = value
        
        return self.type[self.orientation]
    def rotate(self):
        self.orientation = (self.orientation + 1) % len(self.type)

FigureType0 = FigureType0()
FigureType1 = FigureType1()
FigureType2 = FigureType2()
FigureType3 = FigureType3()
FigureType4 = FigureType4()
FigureType5 = FigureType5()

class Figure:
    x = 0
    y = 0
    #includes rand rotation value
    figures = [FigureType0, FigureType1, FigureType2, FigureType3, FigureType4, FigureType5]

    def __init__(self, x, y): #Initializes the figure of the game
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1) #Randomly choose a type of figure from the array
        self.color = random.randint(1, len(colors) - 1) #Randomly choose a color from the array
        self.fitness = 0

    def assign_fitness(self, value):
        self.fitness = value

    def return_fitness(self):
        return self.fitness

    def image(self):            
        return self.figures[self.type].get_type()
        #The arrays are set to be [type of piece][rotation]

    def return_type(self):
        return self.figures[self.type].figure_shape

    def return_shape(self):
        return self.figures[self.type].orientation

    def set_shape(self, value):
        self.type = value

    def set_orientation(self, type, value):
        self.figures[type].set_type(value)
        return self.figures[type].get_type()
        
        
    #returns the location of the piece
    # def location_y(self):
    #     y_field = self.figure.y + 1
    #     return y_field

    def get_rand_figure(self):
        return self.type

    def rotate_fig(self):
        self.figures[self.type].rotate()

    def location(self):
        curr = []
        curr.append(self.x)
        curr.append(self.y)
        print(curr)
        #return curr

#FigureCollection Here
class FigureCollection:
    def __init__(self):
        self.collection = []
    def add_collection(self, figure):
        self.collection.append(figure)
        #print(len(self.collection))
    def clean_collection(self):
        self.collection = []
    def choose_most_fit(self):
        lowest = 200        #place holder value
        fitness_scores = []
        index = 0
        index_storage = []
        for i in range(len(self.collection)- 1):
            fitness_scores.append(self.collection[i].fitness)
            if self.collection[i].fitness < lowest:
                lowest = self.collection[i].fitness
                index = i
            if self.collection[i].fitness == lowest:
                index_storage.append(i)
            
      
        print("Lowest: " + str(lowest))
        duplicate = fitness_scores.count(lowest)
        print(duplicate)
        if duplicate != 1:
            if len(index_storage) > 2:
                del index_storage[0]
                max_y = 100
                index_selected = 0
                y_collection = []
                tie = []
                for ii in range(len(index_storage)):
                    y_collection.append(self.collection[index_storage[ii]].y)
                    if self.collection[index_storage[ii]].y < max_y:
                        max_y = self.collection[index_storage[ii]].y
                        index_selected = index_storage[ii]
                    else:
                        tie.append(index_storage[ii])
                print(y_collection)
                print(index_storage)
                print(index_selected)
                index = index_selected

                
             
        #      index = randnum
    
        #print("Fitness x: " + str(self.collection[index].x))
        #print("Fitness Shape: " + str(self.collection[index].return_shape()))
        
        return self.collection[index]           #return figure with the lowest score


   
        #Create fitness scores for each figure then iterate through and grab the most fit
    

#Tetris Game Collection Class
class GameCollection:
    def __init__(self):
        self.games = [] #store previous games here(Total Empty Space)
        self.curr_iteration = 0 #current game iteration 

    def update(self, emptySpace, lSpace, rSpace):     #will store the info used for the neural net 
        self.games.append(emptySpace)
        self.curr_iteration += 1    #increase current iteration 
        print(self.curr_iteration)


FigureCollection = FigureCollection()


class Tetris:
    level = 2
    score = 0
    state = "start" #Game status
    field = [] #*** Field of the game 
    

    #New Addition
    field_copy = []

    height = 0
    width = 0
    x = 100     #10 rows * 10
    y = 60      #20       *3 
    zoom = 20   
    figure = None
    

    def __init__(self, height, width): #Initializes the tetris game
        self.height = height
        self.width = width
        self.field = []
        self.empty_field = []
        self.score = 0
        self.state = "start"
        self.eSpace = 0         #this is the remaining amount of empty space left on the grid 
        self.lSpace = 0
        self.rSpace = 0     #right space
        self.old_field = None
        self.fitness = 0        #Fitness Funciton
        self.figure_iteration = 0
        self.figure_copy = 0 
        self.fit_figure_boolean = False     #if the fit figure is created should be true
        #Fit figure
        self.fit_figure_x = 0
        self.fit_figure_orientation = 0
        self.fit_figure_type = 0 
        #Fitness 
        self.prev_height = 0
        self.prev_lSpace = 0
        self.prev_rSpace = 0
        
        for i in range(height): #Nested for loop creates a field with height x width (Grid)
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)
            

    def reset_grid(self, grid):     #resets all the numbers in the field to 0 
        for i, e in enumerate(grid):
            if isinstance(e, list):
                self.reset_grid(e)
            else:
                grid[i] = 0
    
    def reset_figure(self):
        self.figure = None

    def save_grid(self,grid):
        #print(self.old_field)
        self.old_field = np.copy(grid)
        #print(self.old_field)

    def new_figure(self):
        self.figure_iteration = 0
        FigureCollection.collection = []
        
        
        self.save_grid(self.field)      #save the grid before copying the figure to simulate generation 
        #print(self.figure_iteration)
        self.figure = Figure(3, 0) #Creates a figure at position (3,0)
        self.figure_copy = self.figure.return_type()
        self.rand_slide()

    def new_figure_copy(self):
        self.field = np.copy(self.old_field)        #everytime the copy is initialized reset the field
        self.figure = Figure(3,0)
        #if(self.figure_iteration % 2 == 0):
            #self.figure.rotate_fig()
        #print(self.figure.)
        self.figure.set_shape(self.figure_copy)
        self.figure.rotate_fig()
        
        self.rand_slide()
        #if((self.figure_iteration % 9) == 0):
        if(self.figure_iteration == 9):
            self.fit_figure_boolean = True
        
        
    def fit_figure(self):
        print("Fit Figure Generated")
        self.field = np.copy(self.old_field)
        self.save_grid(self.field)      #save the grid before copying the new_figure to simulate generation
        
        
        print(self.figure.return_type())
        self.figure = Figure(3,0)
        self.figure.set_shape(self.fit_figure_type)
        self.figure.set_orientation(self.fit_figure_type, self.fit_figure_orientation)
        print(self.figure.return_type())
        #self.figure = Figure(3,0)
        
        self.figure.x = self.fit_figure_x 
        
        #print("Placed Figure Properties(Orientation): " + str(self.figure.return_shape()))
        #print("Fit x: " + str(self.figure.x))
        self.fit_figure_boolean = False

    def save_fit_figure(self, figure):
        #print("Before Orientation: " + str(self.fit_figure_orientation))
        self.fit_figure_x = figure.x
        #self.fit_figure_shape = figure.return_shape()
        self.fit_figure_type = figure.return_type()
        self.fit_figure_orientation = self.figure.return_shape()
        
        #print("After Orientation: " + str(self.fit_figure_orientation))
        #print(self.fit_figure_orientation)


    def find_tot_height(self):      #find the total height when a figure is dropped
        height = []
        for i in range(self.height):
            counter = 0 
            for j in range(self.width):
                if self.field[i][j] > 0:
                    counter = counter + 1
            if(counter > 0):   
                height.append(abs(i-19))
        #print(height)
        #print("Max Height: " + str(height[0] + 1))
        return height[0] + 1 #Max height of the recent figure, add 1 to accomodate for the starting index being 0 

    def find_holes(self):       #Works for gaps too 
        holes = 0
        for i in range(self.height):
            for j in range(self.width):
                if j != 0 and j!=9:  #The Middle of the field array(row)
                    if (self.field[i][j-1] > 0) and (self.field[i][j] == 0) and (self.field[i][j+1] > 0): #checks if the space on the left and right are empty
                        holes = holes + 1
                if j == 0:
                    if (self.field[i][j] == 0) and (self.field[i][1] > 0): #chcks if the space the edge(first block of the row) is empty and the right side is occupied 
                        holes = holes + 1
                if j == 9:
                    if (self.field[i][8] > 0) and (self.field[i][j]  == 0): #checks the same as above but on the left side of the field
                        holes = holes + 1
        #print("Holes Detected: " + str(holes))
        return holes
        #print("Holes Detected: " + str(holes))
    
    def boundary_placement(self, figure):
        edge = False
        value = 0
        for i in range(4): #creates a 4x4 cell to analyze
            for j in range(4):
                if i * 4 + j in self.figure.image():
                        if j + self.figure.x == self.width - 1 or \
                            j + self.figure.x == 0:
                            edge = True
        #print("Edge Placement: " + str(edge))
        if edge == True:
            value = -1
        else:
            value = 1
        return value
    
    def figure_height_score(self):
        if 20 - (self.figure.y)  == self.prev_height:
            value = 0
        elif 20 - (self.figure.y)< self.prev_height:
            value = -1
        else:
            value = 1
        return value

    def specific_fig_height(self):  #Returns difference in height compared to the prev height
        current_height = (20-self.figure.y) - self.prev_height
        return current_height

    def area_placement(self):
        value = 0
        if self.prev_lSpace < self.prev_rSpace:
            if self.figure.x < 2:
                value = 1
            if self.figure.x == 3:
                value = 0
            if self.figure.x > 4:
                value = -1
                
        if self.prev_lSpace > self.prev_rSpace:
             if self.figure.x > 4:
                 value = 1
             if self.figure.x == 3:
                value = 0
             if self.figure.x < 2:
                value = -1
        return value

    def flush(self):
        empty_space = 0
        rows = []
        cols = []
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    rows.append(i + self.figure.y)
                    #print(self.field[i + self.figure.y][j + self.figure.x]), this will return the color of the field in location, 
                    #will be greater than 0 because it is in image
                    cols.append(j + self.figure.x)
        row_set = sorted(list(set(rows)))       #turning the array into a set removes duplicates and we sort just in case of no duplicates(no duplicates result in no sorted array)
        col_set = sorted(list(set(cols)))
        column_length = len(col_set)
        row_length = len(row_set)
        #Checks the length of the row/col due to different figuretypes result in different ranges(ex. square piece vs straight piece)
        if row_length > 1 and column_length > 1:
            for r in range(row_length):
                for c in range(column_length - 1):
                    if self.field[row_set[r]][col_set[c]] == 0:
                        empty_space += 1
            #not at the beginning of the row so I can check the block before first occurence of the block
            if col_set[0] > 0:
                for rr in range(row_length):
                    if self.field[row_set[rr]][col_set[0]-1] == 0:
                        empty_space += 1
            #not at the end of the row so I can check the block after the last occurence
            if col_set[column_length - 1] < 9:
                for rrr in range(row_length):
                    if self.field[row_set[rrr]][col_set[column_length - 1] + 1] == 0:
                        empty_space += 1

        
        #print(empty_space)
        return empty_space
    
    def cover_holes(self):
        holes = 0
        for i in range(self.height):
            for j in range(self.width):
                if i != 0 and i != 1: #if the column is not 0 or 1 
                    if self.field[i][j] == 0 and self.field[i-1][j] > 0:    # chck if the block above a empty space is there if so it is covered
                        holes += 1
                    if self.field[i][j] == 0 and self.field[i-1][j] == 0 and self.field[i-2][j] > 0:
                        holes += 2
        #print("Covered Holes Detected: " + str(holes))
        return holes

    def check_ground(self):
        rows = []
    
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():    #create a 4x4 grid of the figure
                    rows.append(i + self.figure.y)
                    #print(self.field[i + self.figure.y][j + self.figure.x]), this will return the color of the field in location, 
                    #will be greater than 0 because it is in image
                    
        row_set = sorted(list(set(rows)))
        
        count = row_set.count(19)       #after appending the rows it occurs and creating a set, if the 19 is present in the row it is touching the ground
        if count >= 1:
            value = -1
        else:
            value = 0
        return value

    def generate_fitness(self, figure):
       
        fitness = 0
        holes = self.find_holes()
        # print("Figure Fitness Scores:")
        # print("holes: "  + str(holes))
        height = self.find_tot_height()
        # print("Tot Height: "  + str(height))
        # if height < 6:
        #     height = height - 5
        figure_height_score = self.figure_height_score()
        # print("Cur Fig Height: "  + str(figure_height_score))
        boundary_score = self.boundary_placement(figure)
        #print("Boundary Score: "  + str(boundary_score))
        space = self.area_placement()
        # print("Space: "  + str(space))
        flush = self.flush()
        specific_fig_height = self.specific_fig_height()
        covered_holes = self.cover_holes()
        bottom = self.check_ground()
        if flush == 0:
            specific_fig_height = specific_fig_height * 1.5
            holes = holes * 2
            boundary_score = boundary_score * 2
        # print("Bottom: "  + str(bottom))
        #fitness = (holes) + (height * 4) + (boundary_score)  + (figure_height_score * 3) + (bottom * 3)  + (space * 2) - (self.score * 5) + flush + specific_fig_height + covered_holes
        fitness = holes + height + boundary_score  + figure_height_score  + bottom  + space - self.score + flush + specific_fig_height + covered_holes
        # print("Total Fitness Score: " + str(fitness))
        # print("")
        # print("")
        figure.assign_fitness(fitness) 
        #print(fitness)

    

    def rand_slide(self):
        randnum = random.randint(NEG_RANGE, POS_RANGE)
        self.go_side(randnum)

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self):
        self.figure.y += 1
        if self.intersects():   #automatically false 
            
            self.figure.y -= 1
            self.freeze()


    def check_grid(self):
        grid = []
        print("Grid: ")
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(self.field[i][j])
            grid.append(row)
            print(grid[i])
        #print("New Grid: ")
        
          
    def intersects(self): #
        intersection = False    #if the intersection becomes true then it results in a game over
        for i in range(4): #creates a 4x4 cell to analyze
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True 
        return intersection

    #scanning row by row to the top of the game height and width #self.height and width are the height and width of the Tetris game
    def break_lines(self):  
        lines = 0
        space = 0         #this is the remaining amount of space left on the grid 
        self.eSpace = 0
        self.lSpace = 0
        self.rSpace = 0 
        
        for i in range(1, self.height):
            zeros = 0
            currSpace = 0 #number of location of the block it is checking
            
            for j in range(self.width):
                if self.field[i][j] == 0:           #if this is true then the space given is currently empty
                    currSpace += 1 
                    zeros += 1
                    space += 1
                    self.eSpace +=1
                    if currSpace < 6:
                        self.lSpace += 1 
                    else:
                        self.rSpace += 1

            if zeros == 0: #if this is true then this must mean that the given row is full or flush 
                lines += 1
                #if (self.fit_figure_boolean or (self.figure_iteration % 10 == 0)):
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                            self.field[i1][j] = self.field[i1 - 1][j] #shifting the previous lines below??
        self.score += lines ** 2
        

        #print(space)
        #print(self.eSpace)


    def freeze(self): #When the brick collides this will freeze in place
        
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
                    
        #Maybe two different break lines so no scores occur for the copied figures??? or maybe not def test
        self.break_lines() #checks for scoring
        
        if(not self.fit_figure_boolean):
            self.figure_iteration = self.figure_iteration + 1
        
        
        #print("Iteration: " + str(self.figure_iteration))
        #print("Iteration mod: " + str(self.figure_iteration % 10))

        #Initialize Collection Here  
        #if((self.figure_iteration % 10) != 0):  #to change how many figures to produce change this value and the value in new_figure_copy

        if(self.figure_iteration  != 10):  #to change how many figures to produce change this value and the value in new_figure_copy
            if(not self.fit_figure_boolean):
                self.generate_fitness(self.figure)
                print("Fitness: " + str(self.figure.fitness))
                #self.figure.location()
                #self.cover_holes()


                FigureCollection.add_collection(self.figure)
                #print("Index in Array: " + str(len(FigureCollection.collection)))
                
                self.new_figure_copy()
            if(self.fit_figure_boolean):
               
                self.save_fit_figure(FigureCollection.choose_most_fit())
                self.fit_figure()
            

        else:
            #Spawn fit piece here 
            #self.fit_figure(FigureCollection.choose_most_fit())
            #self.find_tot_height()
            self.prev_height = self.find_tot_height()
            self.prev_lSpace = self.lSpace
            self.prev_rSpace = self.rSpace
            self.new_figure()
            
         

        if self.intersects(): #checks the playing area if the brick exceeds the playing area(returns true or false)
            self.state = "gameover"


Game_Collection = GameCollection()      #Create a collection for the games here 
Game_Iteration = 1
bad_game_iteration = 0
#Nnet = Nnet(SIZE)

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tetris")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
fps = 25
game = Tetris(20, 10)  #game is the tetris object 


counter = 0

pressing_down = False

while not done:
    if game.figure is None:
        game.new_figure()
    counter += 1
    if counter > 100000:
        counter = 0

    if counter % (fps // game.level // 2) == 0 or pressing_down:
        if game.state == "start":
            game.go_down()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        #Movement here??
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
            if event.key == pygame.K_RIGHT:
               game.go_side(1)
            if event.key == pygame.K_SPACE:
                game.go_space()
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)

    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False

    screen.fill(WHITE)

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.color],
                                     [game.x + game.zoom * (j + game.figure.x) + 1,
                                      game.y + game.zoom * (i + game.figure.y) + 1,
                                      game.zoom - 2, game.zoom - 2])

    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(game.score), True, BLACK)
    text2 = font.render("Figure #: " + str(game.figure_iteration), True, BLACK)



    screen.blit(text, [0, 0])
    screen.blit(text2, [0, 30])
    if game.state == "gameover":

        if(game.eSpace > 93):
            bad_game_iteration = bad_game_iteration + 1
            bad_game_float = 0.05 * bad_game_iteration
            POS_FLOAT = random.uniform(0.90 + bad_game_float, 1.05 + bad_game_float)
            NEG_FLOAT = random.uniform(1.00 - bad_game_float, 1.05 -  bad_game_float) 


        game.__init__(20,10)
        game.reset_grid(game.field)
        game.reset_figure()
        
    
    pygame.display.flip()
    clock.tick(fps)
        


pygame.quit()
