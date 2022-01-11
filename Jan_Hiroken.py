# Mohammad Jan
# Dec 3 2020
# Hinoken V.1

##### INITIALIZATIONS

import random
import pygame
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning) # prevents a warning being given for subtracting pygame object positions by floats

pygame.init()

background = pygame.image.load('Background.jpg')
Kaji_img = [pygame.image.load('Kaji_base.png'), pygame.image.load('Kaji_beam.png'), pygame.image.load('Kaji_meteor.png'), pygame.image.load('Kaji_hurt.png'), pygame.image.load('Kaji_hurt_beam.png'), pygame.image.load('Kaji_hurt_meteor.png'), pygame.image.load('Beam.png'), pygame.image.load('Meteor.png'), pygame.image.load('Kaji_fume1.png'), pygame.image.load('Kaji_fume2.png'), pygame.image.load('Kaji_fume3.png'), pygame.image.load('Kaji_fume4.png'), pygame.image.load('Kaji_fume5.png'), pygame.image.load('Kaji_fume6.png'), pygame.image.load('Kaji_fume7.png'), pygame.image.load('Smoke.png')]
# Kaji_base: [0]
# Kaji_beam: [1]
# Kaji_meteor: [2]
# Kaji_hurt: [3]
# Kaji_hurt_beam: [4]
# Kaji_hurt_meteor: [5]
# Beam: [6]
# Meteor: [7]
#Kaji_fume1: [8]
#Kaji_fume2: [9]
#Kaji_fume3: [10]
#Kaji_fume4: [11]
#Kaji_fume5: [12]
#Kaji_fume6: [13]
#Kaji_fume7: [14]
#smog: [15]
Hiroken_img = [pygame.image.load('Hiroken_base.png'), pygame.image.load('Hiroken_jump.png'), pygame.image.load('Hiroken_hurt.png'), pygame.image.load('Hiroken_walk1.png'), pygame.image.load('Hiroken_walk2.png'), pygame.image.load('Hiroken_slash1.png'), pygame.image.load('Hiroken_slash2.png'), pygame.image.load('Hiroken_slash3.png'), pygame.image.load('Hiroken_base_rev.png'), pygame.image.load('Hiroken_jump_rev.png'), pygame.image.load('Hiroken_hurt_rev.png'), pygame.image.load('Hiroken_walk1_rev.png'), pygame.image.load('Hiroken_walk2_rev.png')]
#Hiroken_base: [0]
#Hiroken_jump: [1]
#Hiroken_hurt: [2]
#Hiroken_walk1: [3]
#Hiroken_walk2: [4]
#Hiroken_slash1: [5]
#Hiroken_slash2: [6]
#Hiroken_slash3: [7]
#Hiroken_base_rev: [8]
#Hiroken_jump_rev: [9]
#Hiroken_hurt_rev: [10]
#Hiroken_walk1_rev: [11]
#Hiroken_walk2_rev: [12]

screen_width = 500
screen_height = 294

Screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Hiroken')

fps = pygame.time.Clock() # will be used to set fps

flag = True # will be used in main game loop

##### CLASSES

class Menu(object):
    def __init__(self):
        self.menu_img = pygame.image.load('Menu.png') # menu image
        self.help_img = pygame.image.load('Help.png')
        
        self.menu_flag = True # will be used to loop menu screen
    
    def choose(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_s]:
            self.start = True
            self.menu_flag = False
        elif keys[pygame.K_h]:
            self.help = True
            self.menu_flag = False
        elif keys[pygame.K_q]:
            self.quit = True
            self.menu_flag = False
            
        if self.help:
            Screen.blit(self.help_img, (0,0))
            if keys[pygame.K_BACKSPACE]:
                self.help = False
                self.menu_flag = True
                
    def menu_display(self):
            Screen.blit(menu.menu_img, (0,0))
            
            self.start = False #booleans used to navigate the main menu
            self.help = False
            self.quit = False
            
            self.choose()

class Hiroken(object):
    def __init__(self):
        self. x = 100
        self.y = 207 # self.y + self.width should == to 255
        self. width = 22
        self.height = 48
        
        self.walk = 2
        self.jump_counter = 7 # this will determine the height the character jumps
        self.jump = False # boolean used to determine whether character is in the air/ currently jumping or not
        
        self.right = True
        self.left = False
        self.walk_counter = 0 # will cycle the walking animation
        self.walking = False # used for walking animation check
        
        self.health = 100
        self.slash = 3
        
        self.attack_range = 23
        self.attack_counter = 0
        self.regen = False
        self.attack = False
        
        self.burn = False
        self.pushed = False # will be used to determine if hiroken has hit kaji, and will not be able to do anything for a few seconds
        
    def action(self, hiroken_stamina, kaji, floor):
        
        keys = pygame.key.get_pressed()
        
        if not self.pushed and not self.burn:
        
            if not self.attack: # first if statement that contains all movement statements. Will check if the character is attacking before allowing movements to occur
            
                if keys[pygame.K_d]:
                    if self.x + self.width < kaji.x:
                        self.right = True # booleans will allow the attacks and animation to be in the correct direction
                        self.left = False
                        self.walking = True
                        self.x += self.walk
                
                elif keys[pygame.K_a]:
                    if self.x > 0:
                        self.left = True
                        self.right = False
                        self.walking = True
                        self.x -= self.walk
                
                else:
                    self.walking = False
                        
                if keys[pygame.K_j]:
                    if not self.regen and not self.jump:
                        self.attack = True
                        if (self.x + self.width + self.attack_range) >= (kaji.x): # makes sure the character is in range of attacking
                            kaji.health -= self.slash
                            kaji.hurt = True
                                    
                        if hiroken_stamina.width - 25 <= 0:
                            hiroken_stamina.width -= hiroken_stamina.width
                        else:
                            hiroken_stamina.width -= 25   # takes away stamina from hiroken. Stamina will not be regenerated until it is 0                           
                        
                if keys[pygame.K_SPACE]: 
                    if self.jump == False:
                        self.jump = True
                    
                if self.jump == True: # boolean check which will allow character to jump / fall
                    self.y -= self.jump_counter
                    self.jump_counter -= 0.5
                    if self.y + self.height == floor.y:
                        self.jump = False
                        self.jump_counter = 7
                        
                if not self.regen: # boolean's / if statements determining when to regenerate stamina
                    if hiroken_stamina.width <= 0:
                        self.regen =True
                elif self.regen:
                    if hiroken_stamina.width > 100:
                            self.regen = False
                    else:
                        hiroken_stamina.width +=0.5
                        
            elif self.attack: # nested if's to check whether the character is attacking or not. If it is (attack == True) a counter will go up every loop until 60 and only then the character can attack again
                if self.attack_counter < 60:
                    self.attack_counter+=1
                else:
                    self.attack = False
                    self.attack_counter = 0
                if self.attack_counter > 45:
                    if kaji.hurt == True:
                        kaji.hurt = False
                        
    def restore(self, hiroken_stamina):
        self. x = 100
        self.y = 207 # self.y + self.width should == to 255
        
        self.health = 100
        hiroken_stamina.width = 100
        
        self.jump = False
        self.pushed = False
        self.burn = False
        self.attack = False

    def draw(self):
        #pygame.draw.rect(Screen, (10,160,200), (self.x,self.y, self.width,self.height))
        if not self.jump and not self.pushed and not self.attack and not self.burn:
            if self.walking: # walking animation
                self.walk_counter +=1
                
                if self.walk_counter in range(0,12):
                    if self.right:
                        Screen.blit(Hiroken_img[3], (self.x, self.y))
                    elif self.left:
                        Screen.blit(Hiroken_img[11], (self.x, self.y))
                elif self.walk_counter in range(12,24):
                    if self.right:
                        Screen.blit(Hiroken_img[4], (self.x, self.y))
                    elif self.left:
                        Screen.blit(Hiroken_img[12], (self.x, self.y))
                else:
                    if self.right:
                        Screen.blit(Hiroken_img[0], (self.x, self.y))
                    elif self.left:
                        Screen.blit(Hiroken_img[8], (self.x, self.y))
                    self.walk_counter = 0
            else:
                if self.right:
                    Screen.blit(Hiroken_img[0], (self.x, self.y))
                elif self.left:
                    Screen.blit(Hiroken_img[8], (self.x, self.y))
                    
        elif self.pushed or self.burn:
            if self.right:
                Screen.blit(Hiroken_img[2], (self.x, self.y))
            elif self.left:
                Screen.blit(Hiroken_img[10], (self.x, self.y))
                    
        elif self.jump:
            if self.right:
                Screen.blit(Hiroken_img[1], (self.x, self.y))
            elif self.left:
                Screen.blit(Hiroken_img[9], (self.x, self.y))
                
        elif self.attack:
            if self.attack_counter in range(0,9): # loop for attack animation
                Screen.blit(Hiroken_img[5], (self.x, self.y))
            elif self.attack_counter in range(9,18):
                Screen.blit(Hiroken_img[6], (self.x, self.y))
            elif self.attack_counter in range(18,27):
                Screen.blit(Hiroken_img[7], (self.x, self.y))
            elif self.attack_counter in range(27,36):
                Screen.blit(Hiroken_img[6], (self.x, self.y))
            elif self.attack_counter in range(36,45):
                Screen.blit(Hiroken_img[5], (self.x, self.y))
            elif self.attack_counter in range(45,60):
                Screen.blit(Hiroken_img[0], (self.x, self.y))
            else:
                Screen.blit(Hiroken_img[0], (self.x, self.y))

class Bars(object):
    def __init__(self):
        self.x = None
        self.y = None
        self.width = 100 # == hiroken.health / stamina
        self.height = 13
        self.frame_width = self.width + 4 # == self.width + 4
        self.frame_height = self.height + 4
        
    def reduce(self, entity):
        self.width = int(entity.health)
        
    def draw(self, x, y, colour):
        pygame.draw.rect(Screen, (60,50,50), (x-2, y-2, self.frame_width, self.frame_height))
        pygame.draw.rect(Screen, colour, (x, y, self.width, self.height))
    
class Floor(object):
    def __init__(self):
        self.x = 0
        self.y = 255
        self.width = 500
        self.height = 39
        
    def draw(self):
        Screen.blit(pygame.image.load('Floor.png'), (self.x, self.y))

class Kaji(object):
    def __init__(self):
        self.x = 300
        self.y = 205
        self.width = 33
        self.height = 50
        
        self.beam_x = self.x + 10
        self.beam_y = self.y + self.height//2 + 5
        self.beam_width = 20
        self.beam_height = 7
        self.beam_speed = 3
        self.beam_shot = False # boolean used to determine if the beam has been shot
        self.beam_hit = False # boolean used to determine if the beam has hit
        
        self.meteor_x = self.x + 10
        self.meteor_y = self.y + 3
        self.meteor_width = 20
        self.meteor_height = 20
        self.meteor_fall_y = random.randint(5,8)
        self.meteor_fall_x = random.randint(1,2)
        self.meteor_shot = False
        self.meteor_hit = False # ^ booleans used to prevent the character from taking the intended amount of damage when intended
        
        self.cloud_width = 35
        self.cloud_height = 30
        self.cloud_x = self.x
        self.cloud_y = 179
        self.cloud_active = False
        self.cloud_track = False
        self.cloud_counter = 0
        self.fume = False
        
        self.push_back = 5
        
        self.health = 100
        self.attack_counter = 0 # will be used to reach the random attack interval
        self.attack_interval = (random.randint(75,200))
        self.attack_choice = random.randint(1,3) # randomly chooses what attack the enemy will perform
        self.hurt = False
        
        self.animation_counter = 0 # will be used to show the animation before the attack occurs
        self.animation_interval = random.randint(30,60) # will separate the time between the animation and attack
        
    def attack(self, hiroken):
        if not hiroken.jump:
            if (hiroken.x + hiroken.width) >= self.x and hiroken.x < (self.x + self.width):
                hiroken.pushed = True
                hiroken.health -= 15
        
        if self.beam_shot:
            if self.beam_x <= (hiroken.x + hiroken.width) and (self.beam_x + self.beam_width) >= (hiroken.x): # nested if's to check if the beam has hit to prevent unwanted amounts of damage to be done
                if self.beam_y <= (hiroken.y + hiroken.height) and self.beam_y >= hiroken.y:
                    if not self.beam_hit:
                        self.beam_hit = True # boolean prevents the damage to be done again if the beam has already hit character
                        hiroken.burn = True
                        hiroken.health -= 15                        
                    
            elif self.beam_hit: # will only trigger if the beam is outside of the character hit zone
                self.beam_hit = False
        
        elif self.meteor_shot:        
            if self.meteor_x <= (hiroken.x + hiroken.width) and (self.meteor_x + self.meteor_width)  >= hiroken.x:
                if (self.meteor_y + self.meteor_height) >= hiroken.y and self.meteor_y<= (hiroken.y + hiroken.height):
                    if not self.meteor_hit:
                        self.meteor_hit = True
                        hiroken.pushed = True
                        hiroken.health -= 25
                        
            elif self.meteor_hit:
                self.meteor_hit = False   
            
        if hiroken.pushed:
            hiroken.x -= self.push_back
            if self.push_back > 0:
                self.push_back -= 0.1
            else:
                self.push_back = 5
                hiroken.pushed = False
                
        elif hiroken.burn: # lighter version of pushed back activated when the beam hits hiroken
            if hiroken.x >= 0:
                hiroken.x -= self.push_back//2
            if self.push_back > 3:
                self.push_back -= 0.1
            else:
                self.push_back = 5
                hiroken.burn = False
            
        self.attack_counter += 1
        
    def restore(self):
        self.meteor_shot = False
        self.meteor_y = self.y 
        self.meteor_x = self.x + 17            
        self.meteor_fall_y = random.randint(5,8)
        self.meteor_fall_x = random.randint(1,2) # restores changed meteor values
        
        self.beam_x = self.x + 10
        self.beam_shot = False # restores changed beam values
        
        self.fume = False
                    
        self.attack_counter = 0
        self.attack_interval = random.randint(75,200)
        self.attack_choice = random.randint(1,3) # restores changed attack values
        
        self.animation_interval = random.randint(30,60) # will separate the time between the animation and attack
        self.animation_counter = 0 # will be used to show the animation before the attack occurs
    
    def restore_cloud(self):
        self.cloud_counter = 0
        self.cloud_y = 179
        self.cloud_x = self.x
        self.cloud_active = False
        self.cloud_track = False
        
        hiroken.walk = 2
        
    def reset(self):
        self.restore()
        self.restore_cloud()
        
        self.health = 100
        self.hurt = False 
    
    def draw(self):
        if not self.beam_shot and not self.meteor_shot and not self.fume: # if not doing any action will blit base image of Kaji
            if self.hurt:
                Screen.blit(Kaji_img[3], (self.x, self.y)) # drawing of kaji when hurt
            else:
                Screen.blit(Kaji_img[0], (self.x, self.y)) # refer to comment lines (17 - 30) for list index image reference
        elif self.beam_shot: # Kaji beam shooting animation
            if self.hurt:
                Screen.blit(Kaji_img[4], (self.x, self.y))
            else:
                Screen.blit(Kaji_img[1], (self.x, self.y))
        elif self.meteor_shot: # Kaji meateor shooting animation
            if self.hurt:
                Screen.blit(Kaji_img[5], (self.x, self.y-3))
            else:
                Screen.blit(Kaji_img[2], (self.x, self.y-3))
        elif self.fume: # Kaji fuming animation
            if self.animation_counter in range(0,20):
                Screen.blit(Kaji_img[8], (self.x, self.y))
            elif self.animation_counter in range(20,40):
                Screen.blit(Kaji_img[9], (self.x, self.y))
            elif self.animation_counter in range(40,60):
                Screen.blit(Kaji_img[10], (self.x, self.y))
            elif self.animation_counter in range(60,80):
                Screen.blit(Kaji_img[11], (self.x, self.y))
            elif self.animation_counter in range(80,100):
                Screen.blit(Kaji_img[12], (self.x, 255 - 60))
            elif self.animation_counter in range(100,120):
                Screen.blit(Kaji_img[13], (self.x, 255 - 60))
            elif self.animation_counter in range(120,140):
                Screen.blit(Kaji_img[14], (self.x, 255 - 65))
            elif self.animation_counter in range(140,160):
                Screen.blit(Kaji_img[8], (self.x, self.y))
                Screen.blit(Kaji_img[15], (self.cloud_x, self.cloud_y))
                
            self.animation_counter += 1 # uses animation counter to cycle through images
            
            if self.animation_counter > 160: # once break point (100) is reached base image will be blit and cloud_active boolean will become true
                Screen.blit(Kaji_img[0], (self.x, self.y))
                self.cloud_active = True
                self.restore()
        
        if self.attack_counter >= self.attack_interval: # checks if the minimum interval has passed for the next attack to occur, then will randomly throw out the next attack           
            
            if self.attack_choice == 1: # if choice == 1 beam attack will ensue
                self.beam_shot = True
                self.animation_counter += 1
                if self.animation_counter >= self.animation_interval:
                    Screen.blit(Kaji_img[6], (self.beam_x, self.beam_y)) # drawing of beam
                    self.beam_x -= self.beam_speed
                    
                    if self.beam_x <= 0 or self.beam_hit:
                        self.restore() # restores all beam original values after it hits the end of the page
            
            elif self.attack_choice == 2: # else if the choice == 2 the meteor attack will proceed
                self.meteor_shot = True
                self.animation_counter += 1
                if self.animation_counter >= self.animation_interval:
                    Screen.blit(Kaji_img[7], (self.meteor_x, self.meteor_y)) # drawing of meteor
                    
                    self.meteor_y -= self.meteor_fall_y 
                    self.meteor_x -= self.meteor_fall_x 
                    self.meteor_fall_y -= 0.2 # parabolic movement of meteor                
                    
                    if self.meteor_y + 20 >= 255:
                        self.restore() # restores all original values of meteor after it has hit the ground
                
            elif self.attack_choice == 3: # elif the choice == 3 the
                if not self.cloud_active:
                    self.fume = True
                else:
                    self.restore()

        if self.cloud_active:
                Screen.blit(Kaji_img[15], (self.cloud_x, self.cloud_y))
                if self.cloud_y > 90 and not self.cloud_track:
                    self.cloud_y -= 1
                else:
                    self.cloud_track = True
                    
                    if self.cloud_y < hiroken.y + 2:
                        self.cloud_y  += 0.5
                    elif self.cloud_y > hiroken.y + 2:
                        self.cloud_y -= 0.5
                        
                    if self.cloud_x + (self.cloud_width/2) > hiroken.x + (hiroken.width/2):
                        self.cloud_x -= 0.5
                    elif self.cloud_x + (self.cloud_width/2) < hiroken.x + (hiroken.width/2):
                        self.cloud_x += 0.5
                        
                    if self.cloud_x < (hiroken.x + hiroken.width) and (self.cloud_x + self.cloud_width) > hiroken.x and (self.cloud_y + self.cloud_width) > hiroken.y:
                        hiroken.walk = 1
                        self.cloud_counter +=0.5
                        
                        if self.cloud_counter > 120:
                            self.restore_cloud()
                    else:
                        hiroken.walk = 2
                    #self.restore()
        
##### INSTANCES

menu = Menu()

hiroken = Hiroken()
kaji = Kaji()

hiroken_bar = Bars()
hiroken_stamina = Bars()
kaji_bar = Bars()

floor = Floor()

##### MAIN

game_loop = True

while game_loop:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
    
    fps.tick(60)
    
    if menu.menu_flag:
        menu.menu_display()
        
    elif menu.help:
        menu.choose()
    
    elif menu.start:
    
        hiroken.action(hiroken_stamina, kaji, floor)
        hiroken_bar.reduce(hiroken)
        
        kaji.attack(hiroken)
        kaji_bar.reduce(kaji)
        
        Screen.blit(background, (0,0))
        
        floor.draw()
        kaji.draw()
        hiroken.draw()
        
        hiroken_bar.draw(50,35, (0,255,255))
        kaji_bar.draw(350,35, (255,0,0))
        hiroken_stamina.draw(50, 65, (0,250,0))
        
        if kaji.health <= 0 or hiroken.health <= 0:
            menu.menu_flag = True
            
            hiroken.restore(hiroken_stamina)
            kaji.reset()
            
    elif menu.quit:
        game_loop = False
    
    pygame.display.update()
        
pygame.quit()

##### TO DO LIST

# Smoke cloud fade animation?
# Win/Lose screen