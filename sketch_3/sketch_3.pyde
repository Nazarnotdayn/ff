'''
Света решила сделать проект про цветочек.
Сначала на холсте только фон, но постепенно
Сквозь фон проглядывает цветок, он всё
виднее и виднее. Но почему-то цветок не появляется.
Как это исправить?
'''


sat = 30

def setup():
    size(600,400)
    colorMode(HSB, 360, 50, 100)
    background(280, 30, 100)
    
    
def draw():
    global sat
    fill(280,sat , 100)
    noStroke()
    translate(300,200)
    ellipse(0,0,30,30)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    
    rotate(radians(30))
    ellipse(80,0,100,40)
    rotate(radians(30))
    ellipse(80,0,100,40)
    
    sat = sat + 0.01
    if sat > 100:
        noLoop()
