HEIGHT=1000
WIDTH=1000
score=0

game_over=False
pop = Actor("pop")
coin = Actor("coin")
coin.pos = 200, 200
pop.pos = 300, 80
def draw():
    screen.fill("blue")
    pop.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

if game_over:
    screen.fill("pink")
    screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

#from random import randint

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True
    clock.schedule(time_up, 7.0)

def update():
#global score
    if keyboard.a:
        pop.x = pop.x - 2
    elif keyboard.d:
        pop.x = pop.x + 2
    elif keyboard.w:
        pop.y = pop.y - 2
    elif keyboard.s:
        pop.y = pop.y + 2
coin_collected = pop.colliderect(coin)

if coin_collected:
    score = score + 10
    place_coin()
