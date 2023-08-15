import pygame
import random

# SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# PYGAME
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# MUSIC
pizzaMusic = "pizza.mp3"
pygame.mixer.init()
pygame.mixer.music.load(pizzaMusic)
pygame.mixer.music.play(-1)

bara_bereSort = pygame.mixer.Sound("bara_Sort.mp3")
baraLong = pygame.mixer.Sound("bara.mp3")
baraCounter = 0

# FPS
clock = pygame.time.Clock()
fps = 59

wantToAppendBalls = True

# BOX
box_x = SCREEN_WIDTH // 2
box_y = 500
box_speed = 0
box_height = 20
box_width = 100
box = pygame.Rect(box_x, box_y, box_width, box_height)

# BALL
ball_x = box_x # ball's start position
ball_y = box_y - 50 # ball's start position
ball_height = 10 # balls height
ball_width = 10 # balls width
ball_number = 1 # how much ball do we want?
balls = [] # how many ball we have?
for i in range(ball_number):
    ball = pygame.Rect(ball_x, ball_y, ball_width, ball_height)
    balls.append(ball) # let's create balls

balls_velocity_x = [] # balls x velocity
balls_velocity_y = [] # balls y velocity
for i in range(len(balls)): # let's give them random velocity
    balls_velocity_x.append(random.randint(-1, 1))
    balls_velocity_y.append(-random.randint(3, 5))

# BALL MULTIPLIER
ballMultiplierList = [] # this list is useful end of tho code. if we hit luckyNumber, then an element will be added this list!

# GAME_BOARD
game_board = [  

                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,

            ]
# zeros, there is no brick
# ones, there will be brick

brick_width = 25
brick_height = 25
brick_x = 0
brick_y = 0
bricks = []
rowChecker = 1 # this is useful for handle with 0's and 1's..
brick_color = (67, 0, 0)
luckyNumber = 3 # we'll check this later for ballMultiplier
luckyBallsList = []

unbreakableBrick_color = (15, 15, 15)
unbreakableBricks = []

for i in game_board:
 
    if i == 0: # if there is 0, then 
        brick_x += 25 # skip the next cell

    elif i == 1: # if there is 1, then
        brick = pygame.Rect(brick_x, brick_y, brick_width, brick_width) # create a brick
        bricks.append(brick) # create a brick
        brick_x += 25 # skip next cell

    elif i == 2: # if there is 1, then
        brick = pygame.Rect(brick_x, brick_y, brick_width, brick_width) # create a brick
        unbreakableBricks.append(brick) # create a brick
        brick_x += 25 # skip next cell
    
    if rowChecker % 32 == 0: # skip the next row
        brick_x = 0 # reset the x value
        brick_y += 25 # skip the next row

    rowChecker += 1 # this is useful for handle with rows.

# FUNCTIONS


# LOOP
running = True
while running:

    # BACKGORUND COLOR
    screen.fill((0, 137, 43))

    # FPS
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                box_speed = -5
            elif event.key == pygame.K_RIGHT:
                box_speed = 5
            elif event.key == pygame.K_q:
                pygame.quit()
                quit()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                box_speed = 0
            if event.key == pygame.K_RIGHT:
                box_speed = 0

    # BOX CONTROL
    if box.x > SCREEN_WIDTH - box_width: # box's borders. (it moves only vertical direction)
        box.x = SCREEN_WIDTH - box_width
    if box.x < 0:
        box.x = 0

    box.x += box_speed # add the speed to box.

    for k in range(len(ballMultiplierList)):
            ballMultiplierList[k].y += 3 # move them in y direction

    for j in range(len(balls)): # FOR EVERY BALL

        # BALL CONTROL
        balls[j].x += balls_velocity_x[j] # add the veloctiyy to every ball in x direction
        balls[j].y += balls_velocity_y[j] # add the veloctiyy to every ball in y direction

        # Border for balls
        if balls[j].x > SCREEN_WIDTH - 10:
            balls_velocity_x[j] = -balls_velocity_x[j]
        if balls[j].x < 5:
            balls_velocity_x[j] = -balls_velocity_x[j]
        if balls[j].y > SCREEN_HEIGHT - ball_height:
            balls_velocity_x[j] = 0
            balls_velocity_y[j] = 0
            balls[j].x = 9888
            balls[j].y = 9888
        if balls[j].y < 5:
            balls_velocity_y[j] = -balls_velocity_y[j] 

        # Let's draw how many brick we have.
        for i in range(len(bricks)):
            pygame.draw.rect(screen, brick_color, bricks[i])

        for i in range(len(unbreakableBricks)):
            pygame.draw.rect(screen, unbreakableBrick_color, unbreakableBricks[i])

        # İf ball collides with box, then change its direction.
        collision_tolerance_for_ball_and_box = 10
        if box.colliderect(balls[j]):
            if abs(box.top - balls[j].bottom) < collision_tolerance_for_ball_and_box and balls_velocity_y[j] > 0:
                if box_speed == 0:
                    balls_velocity_y[j] *= -1
                elif box_speed * balls_velocity_x[j] < 0:
                    balls_velocity_x[j] = random.randint(-3, -1)
                    balls_velocity_y[j] *= -1
                elif box_speed * balls_velocity_x[j] > 0:
                    balls_velocity_x[j] = random.randint(1, 3)
                    balls_velocity_y[j] *= -1
                elif balls_velocity_x[j] * box_speed == 0:
                    if box_speed < 0:
                        balls_velocity_x[j] = random.randint(-3, -1)
                        balls_velocity_y[j] *= -1
                    elif box_speed > 0:
                        balls_velocity_x[j] = random.randint(1, 3)
                        balls_velocity_y[j] *= -1


            if abs(box.bottom - balls[j].top) < collision_tolerance_for_ball_and_box and balls_velocity_y[j] < 0:
                if box_speed == 0:
                    balls_velocity_y[j] *= -1
                elif box_speed * balls_velocity_x[j] < 0:
                    balls_velocity_x[j] = random.randint(-3, -1)
                    balls_velocity_y[j] *= -1
                elif box_speed * balls_velocity_x[j] > 0:
                    balls_velocity_x[j] = random.randint(1, 3)
                    balls_velocity_y[j] *= -1
                elif balls_velocity_x[j] * box_speed == 0:
                    if box_speed < 0:
                        balls_velocity_x[j] = random.randint(-3, -1)
                        balls_velocity_y[j] *= -1
                    elif box_speed > 0:
                        balls_velocity_x[j] = random.randint(1, 3)
                        balls_velocity_y[j] *= -1

            if abs(box.right - balls[j].left) < collision_tolerance_for_ball_and_box and balls_velocity_x[j] < 0:
                balls_velocity_x[j] *= -1

            if abs(box.left - balls[j].right) < collision_tolerance_for_ball_and_box and balls_velocity_x[j] > 0:
                balls_velocity_x[j] *= -1

        pygame.draw.rect(screen, (245, 145, 45), balls[j])

        for i in range(len(bricks)):
            if bricks[i].colliderect(balls[j]) and len(balls) < 10:

                pygame.mixer.music.stop()
                # Çarpışma efektini çal
                baraCounter += 1
                bara_bereSort.play()

                # Arka plan müziğini yükle ve çal
                pygame.mixer.music.load(pizzaMusic)
                pygame.mixer.music.play(-1)
            
        if len(balls) > 10:
            baraLong.play(-1)

        if len(balls) > 15:
            luckyNumber = 9999

    for j in range(len(balls)):
        # COLLISION BETWEEN BRICKS AND BALL
        collision_tolerance_for_brick_and_box = 10
        for i in range(len(bricks)):
            if bricks[i].colliderect(balls[j]):

                if abs(bricks[i].top - balls[j].bottom) < collision_tolerance_for_brick_and_box and balls_velocity_y[j] > 0:
                    balls_velocity_y[j] *= -1

                elif abs(bricks[i].bottom - balls[j].top) < collision_tolerance_for_brick_and_box and balls_velocity_y[j] < 0:
                    balls_velocity_y[j] *= -1

                elif abs(bricks[i].right - balls[j].left) < collision_tolerance_for_brick_and_box and balls_velocity_x[j] < 0:
                    balls_velocity_x[j] *= -1

                elif abs(bricks[i].left - balls[j].right) < collision_tolerance_for_brick_and_box and balls_velocity_x[j] > 0:
                    balls_velocity_x[j] *= -1

                # When there is collision between ball and bricks, then pick number.
                tried_number = random.randint(2, 4)
                if tried_number == luckyNumber and len(balls) < 30: # if it is same with lucky number, then
                    ballMultiplier = pygame.Rect(bricks[i].x + 5, bricks[i].y, 15, 15)
                    ballMultiplierList.append(ballMultiplier) # create an element for ballMultiplierList
                    luckyBallsList.append(balls[j])
                    
                bricks[i].x = 1000 #if there is collision between ball and bricks, then move them to infinity
                bricks[i].y = 1000 #if there is collision between ball and bricks, then move them to infinity
            
        # COLLISION BETWEEN UNBREAKABLEBRICKS AND BALL
        for i in range(len(unbreakableBricks)):
            if unbreakableBricks[i].colliderect(balls[j]):
                if abs(unbreakableBricks[i].top - balls[j].bottom) < collision_tolerance_for_brick_and_box and balls_velocity_y[j] > 0:
                    balls_velocity_y[j] *= -1

                if abs(unbreakableBricks[i].bottom - balls[j].top) < collision_tolerance_for_brick_and_box and balls_velocity_y[j] < 0:
                    balls_velocity_y[j] *= -1

                if abs(unbreakableBricks[i].right - balls[j].left) < collision_tolerance_for_brick_and_box and balls_velocity_x[j] < 0:
                    balls_velocity_x[j] *= -1

                if abs(unbreakableBricks[i].left - balls[j].right) < collision_tolerance_for_brick_and_box and balls_velocity_x[j] > 0:
                    balls_velocity_x[j] *= -1

        # for every element in ballMultiplierList
    for k in range(len(ballMultiplierList)):
        pygame.draw.rect(screen, (255, 255, 0), ballMultiplierList[k]) # draw a yellow box, and 

        if box.colliderect(ballMultiplierList[k]) and wantToAppendBalls:
        # if box collides with ballMultiplier
            for u in range(len(balls)):
                for i in range(3):
                    ball = pygame.Rect(balls[u].x, balls[u].y, ball_width, ball_height) #create a new ball
                    balls.append(ball) # draw it on the screen in the starting position
                    balls_velocity_x.append(random.randint(-5, 5)) # add velocity to it
                    balls_velocity_y.append(-random.randint(-5, 5))                   
            ballMultiplierList[k].x = 8000 # move this ballMultiplier box to infinity
            ballMultiplierList[k].y = 8000 # move this ballMultiplier box to infinity

                        # Let's draw balls and box
    pygame.draw.rect(screen, (0, 166, 255), box)

    if len(balls) > 30:
        wantToAppendBalls = False

    # UPDATE THE SCREEN
    pygame.display.update()

# CLOSE THE GAME
pygame.quit()
