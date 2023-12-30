
#importing required libraries
import pygame as py
import sys

def ball_animation():
    global ball_speed_x,ball_speed_y
    ball_speed_x = 6
    ball_speed_y = 6

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.top <=0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <=0 or ball.right >= screen_width:
        ball_speed_x *= -1
    
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1




#General setup
py.init()

clock = py.time.Clock()

#Setting up the main window
screen_width = 780
screen_height = 640
screen = py.display.set_mode((screen_width,screen_height))
py.display.set_caption('Pong')

running = True

ball = py.Rect(screen_width/2 - 10,screen_height/2 - 10,20,20)
player = py.Rect(screen_width - 15,screen_height/2 - 35,10,80)
opponent = py.Rect(10,screen_height/2 - 35,10,80)

bg_colour = py.Color('grey12')
light_grey = (200,200,200)


while running:
    #Handling the input 
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
            
    ball_animation()
    
    
    #Visuals
    screen.fill(bg_colour)
    py.draw.rect(screen,light_grey,player)
    py.draw.rect(screen,light_grey,opponent)
    py.draw.ellipse(screen,light_grey,ball)
    py.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))

    
    #Updating the window
    py.display.flip()
    clock.tick(60)
    

py.quit()
sys.exit()





















