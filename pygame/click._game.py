blob = Actor("person")
blob.topright = 0, 10

WIDTH = 300
HEIGHT = blob.height + 20


def draw():
    screen.clear()
    screen.fill((128, 0, 0))
    blob.draw()


def update():
    blob.left = blob.left + 2
    if blob.left > WIDTH:
        blob.right = 0
