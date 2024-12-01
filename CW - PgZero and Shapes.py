import pgzrun

#Setting Width and Height
WIDTH = 500
HEIGHT = 500

def draw():
    screen.fill('black')
    rect1 = Rect((0, 0), (100, 50)) 
    rect1.center = (250, 250)
    screen.draw.rect(rect1, 'red')
    screen.draw.circle((100, 100), 30, 'lime')
    screen.draw.line((150, 150), (200, 200), (0, 255, 255))



pgzrun.go()