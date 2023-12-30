#Pong_Game
#importing required libraries
import pygame as py
import random

def ball_animation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.top <=0 or ball.bottom >= screen_height:
        ball_speed_y = ball_speed_y * -1
    if ball.left <=0 or ball.right >= screen_width:
        ball_restart()
    
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x = ball_speed_x * -1

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2,screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
        
def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.top -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


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
player = py.Rect(screen_width - 10,screen_height/2 - 35,5,80)
opponent = py.Rect(0,screen_height/2 - 35,5,80)

bg_colour = py.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 6
ball_speed_y = 6
player_speed = 0
opponent_speed = 6


while running:
    #Handling the input 
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_DOWN:
                player_speed += 6
            if event.key == py.K_UP:
                player_speed -= 6
        if event.type == py.KEYUP:
            if event.key == py.K_DOWN:
                player_speed -= 6
            if event.key == py.K_UP:
                player_speed += 6
            
            
    ball_animation()
    player_animation()
    opponent_ai()
    
    
    
    
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






















