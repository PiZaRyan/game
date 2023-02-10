blob = Actor("guy")
blob.topright = 0, 10
click = 0

WIDTH = 300
HEIGHT = blob.height + 20


def draw():
    screen.clear()
    screen.fill((72, 98, 130))
    blob.draw()


def update():
    blob.left = blob.left + 2
    if blob.left > WIDTH:
        blob.right = 0

def on_mouse_down(pos):
    global click
    if blob.collidepoint(pos) and click == 0:
        print("Eek!")
        blob.image = 'person'
        click = 1
    elif blob.collidepoint(pos) and click == 1:
        print("Eek!")
        blob.image = 'guy'
        click = 0
    else:
        print("You missed me!")
